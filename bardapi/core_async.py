import os
import json
import uuid
import string
import random
import base64
from re import search
from langdetect import detect
from httpx import AsyncClient
from deep_translator import GoogleTranslator
from google.cloud import translate_v2 as translate
from bardapi.constants import ALLOWED_LANGUAGES, SESSION_HEADERS
from bardapi.utils import extract_links, upload_image, extract_bard_cookie


class BardAsync:
    """
    Bard class for interacting with the Bard API using httpx[http2]
    """

    def __init__(
        self,
        token: str = None,
        timeout: int = 20,
        proxies: dict = None,
        google_translator_api_key: str = None,
        language: str = None,
        run_code: bool = False,
        token_from_browser=False,
    ):
        """
        Initialize the Bard instance.

        Args:
            token (str): Bard API token.
            timeout (int): Request timeout in seconds.
            proxies (dict): Proxy configuration for requests.
            google_translator_api_key (str): Google cloud translation API key.
            language (str): Natural language code for translation (e.g., "en", "ko", "ja").
            run_code (bool): Whether to directly execute the code included in the answer (Python only)
            token_from_browser (bool): Gets a token from the browser
        """
        self.token = token or os.getenv("_BARD_API_KEY")
        if not self.token and token_from_browser:
            self.token = extract_bard_cookie()
            if not self.token:
                raise Exception(
                    "\nCan't extract cookie from browsers.\nPlease sign in first at\nhttps://accounts.google.com/v3/signin/identifier?followup=https://bard.google.com/&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
                )
        self.proxies = proxies
        self.timeout = timeout
        self._reqid = int("".join(random.choices(string.digits, k=4)))
        self.conversation_id = ""
        self.response_id = ""
        self.choice_id = ""
        # Making httpx async client that will be used for all API calls
        self.client = AsyncClient(
            http2=True,
            headers=SESSION_HEADERS,
            cookies={"__Secure-1PSID": self.token},
            timeout=self.timeout,
            proxies=self.proxies,
        )
        self.language = language
        self.cookie_dict = {"__Secure-1PSID": self.token}
        self.run_code = run_code or False
        self.google_translator_api_key = google_translator_api_key

    async def get_answer(self, input_text: str) -> dict:
        """
        Get an answer from the Bard API for the given input text.

        Example:
        >>> import asyncio
        >>>
        >>> async def main():
        >>>     token = 'xxxxxx'
        >>>     bard = BardAsync(token=token)
        >>>     response = await bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")
        >>>     print(response['content'])
        >>>
        >>> asyncio.run(main())

        Args:
            input_text (str): Input text for the query.

        Returns:
            dict: Answer from the Bard API in the following format:
                {
                    "content": str,
                    "conversation_id": str,
                    "response_id": str,
                    "factuality_queries": list,
                    "text_query": str,
                    "choices": list,
                    "links": list
                    "images": set,
                    "program_lang": str,
                    "code": str,
                    "status_code": int
                }
        """
        self.SNlM0e = await self._get_snim0e()
        if not isinstance(self.SNlM0e, str):
            self.SNlM0e = await self.SNlM0e
        params = {
            "bl": "boq_assistant-bard-web-server_20230419.00_p1",
            "_reqid": str(self._reqid),
            "rt": "c",
        }
        if self.google_translator_api_key is not None:
            google_official_translator = translate.Client(
                api_key=self.google_translator_api_key
            )

        # [Optional] Set language
        if (
            self.language is not None
            and self.language not in ALLOWED_LANGUAGES
            and self.google_translator_api_key is None
        ):
            translator_to_eng = GoogleTranslator(source="auto", target="en")
            input_text = translator_to_eng.translate(input_text)
        elif (
            self.language is not None
            and self.language not in ALLOWED_LANGUAGES
            and self.google_translator_api_key is not None
        ):
            input_text = google_official_translator.translate(
                input_text, target_language="en"
            )

        # Make post data structure and insert prompt
        input_text_struct = [
            [input_text],
            None,
            [self.conversation_id, self.response_id, self.choice_id],
        ]
        data = {
            "f.req": json.dumps([None, json.dumps(input_text_struct)]),
            "at": self.SNlM0e,
        }

        resp = await self.client.post(
            "https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate",
            params=params,
            data=data,
            timeout=self.timeout,
            follow_redirects=True,
            headers=SESSION_HEADERS,
            cookies=self.cookie_dict,
        )

        # Post-processing of response
        resp_dict = json.loads(resp.content.splitlines()[3])[0][2]

        if not resp_dict:
            return {"content": f"Response Error: {resp.content}."}
        resp_json = json.loads(resp_dict)

        # [Optional] Gather image links
        try:
            images = set()
            if len(resp_json) >= 3:
                if len(resp_json[4][0]) >= 4 and resp_json[4][0][4] is not None:
                    for img in resp_json[4][0][4]:
                        try:
                            images.add(img[0][0][0])
                        except Exception as e:
                            # TODO:
                            #  handle exception using logging instead
                            print(f"Unable to parse image from the response: {e}")
        except:
            pass
        parsed_answer = json.loads(resp_dict)

        # [Optional] Translated by google translator
        ## Unofficial for testing
        if (
            self.language is not None
            and self.language not in ALLOWED_LANGUAGES
            and self.google_translator_api_key is None
        ):
            translator_to_lang = GoogleTranslator(source="auto", target=self.language)
            parsed_answer[4] = [
                [x[0], [translator_to_lang.translate(x[1][0])] + x[1][1:], x[2]]
                for x in parsed_answer[4]
            ]
        ## Official google cloud translation API
        elif (
            self.language is not None
            and self.language not in ALLOWED_LANGUAGES
            and self.google_translator_api_key is not None
        ):
            parsed_answer[4] = [
                [
                    x[0],
                    [google_official_translator(x[1][0], target_language=self.language)]
                    + x[1][1:],
                    x[2],
                ]
                for x in parsed_answer[4]
            ]

        # Get code
        try:
            program_lang = (
                parsed_answer[4][0][1][0].split("```")[1].split("\n")[0].strip()
            )
            code = parsed_answer[4][0][1][0].split("```")[1][len(program_lang) :]
        except Exception:
            program_lang, code = None, None

        # Returned dictionary object
        bard_answer = {
            "content": parsed_answer[4][0][1][0],
            "conversation_id": parsed_answer[1][0],
            "response_id": parsed_answer[1][1],
            "factuality_queries": parsed_answer[3],
            "text_query": parsed_answer[2][0] if parsed_answer[2] else "",
            "choices": [{"id": x[0], "content": x[1]} for x in parsed_answer[4]],
            "links": extract_links(parsed_answer[4]),
            "images": images,
            "program_lang": program_lang,
            "code": code,
            "status_code": resp.status_code,
        }

        self.conversation_id, self.response_id, self.choice_id = (
            bard_answer["conversation_id"],
            bard_answer["response_id"],
            bard_answer["choices"][0]["id"],
        )
        self._reqid += 100000

        # Execute code
        if self.run_code and bard_answer["code"] is not None:
            try:
                print(bard_answer["code"])
                # TODO:
                #  find a way to handle this following warning
                #  EX100: use of builtin exec function for dynamic input is insecure and can leave your application
                #  open to arbitrary code execution. Found in 'exec(bard_answer['code'])'.
                exec(bard_answer["code"])
            except Exception as e:
                # TODO:
                #  handle exception using logging instead
                print(f"Unable to execute the code: {e}")

        return bard_answer

    async def speech(self, input_text: str, lang: str = "en-US") -> dict:
        """
        Get speech audio from Bard API for the given input text.

        Example:
        >>> import asyncio
        >>>
        >>> async def main():
        >>>     token = 'xxxxxx'
        >>>     bard = BardAsync(token=token)
        >>>     audio = await bard.speech("Hello")
        >>>     with open("bard.ogg", "wb") as f:
        >>>         f.write(bytes(audio['audio']))
        >>>
        >>> asyncio.run(main())

        Args:
            input_text (str): Input text for the query.
            lang (str): Input language for the query

        Returns:
            dict: Answer from the Bard API in the following format:
            {
                "audio": bytes,
                "status_code": int
            }
        """
        params = {
            "bl": "boq_assistant-bard-web-server_20230419.00_p1",
            "_reqid": str(self._reqid),
            "rt": "c",
        }

        input_text_struct = [
            [["XqA3Ic", json.dumps([None, input_text, lang, None, 2])]]
        ]

        data = {
            "f.req": json.dumps(input_text_struct),
            "at": await self._get_snim0e(),
        }

        # Get response
        resp = await self.client.post(
            "https://bard.google.com/_/BardChatUi/data/batchexecute",
            params=params,
            data=data,
            timeout=self.timeout,
        )

        # Post-processing of response
        resp_dict = json.loads(resp.content.splitlines()[3])[0][2]
        if not resp_dict:
            return {
                "content": f"Response Error: {resp.content}. "
                f"\nTemporarily unavailable due to traffic or an error in cookie values. "
                f"Please double-check the cookie values and verify your network environment."
            }
        resp_json = json.loads(resp_dict)
        audio_b64 = resp_json[0]
        audio_bytes = base64.b64decode(audio_b64)
        return {"audio": audio_bytes, "status_code": resp.status_code}

    async def _get_snim0e(self):
        """
        The _get_snim0e function is used to get the SNlM0e value from the Bard website.

        The function uses a regular expression to search for the SNlM0e value in the response text.
        If it finds it, then it returns that value.

        :param self: Represent the instance of the class
        :return: (`str`) The snlm0e value
        """
        if not self.token or self.token[-1] != ".":
            raise Exception(
                "__Secure-1PSID value must end with a single dot. Enter correct __Secure-1PSID value."
            )

        resp = await self.client.get(
            "https://bard.google.com/", timeout=self.timeout, follow_redirects=True
        )
        if resp.status_code != 200:
            raise Exception(
                f"Response status code is not 200. Response Status is {resp.status_code}"
            )
        snim0e = search(r"SNlM0e\":\"(.*?)\"", resp.text)
        if not snim0e:
            raise Exception(
                "SNlM0e value not found in response. Check __Secure-1PSID value."
            )
        return snim0e.group(1)

    async def export_conversation(self, bard_answer, title: str = "") -> str:
        """
        Get Share URL for specifc answer from bard

        Example:
        >>> import asyncio
        >>>
        >>> async def main():
        >>>     token = 'xxxxxx'
        >>>     bard = BardAsync(token=token)
        >>>     bard_answer = await bard.get_answer("hello!")
        >>>     url = await bard.export_conversation(bard_answer, title="Export Conversation")
        >>>     print(url['url'])
        >>>
        >>> asyncio.run(main())

        Args:
            bard_answer (dict): bard_answer returned from get_answer
            title (str): Title for URL
        Returns:
            dict: Answer from the Bard API in the following format:
            {
                "url": str,
                "status_code": int
            }
        """
        conv_id = bard_answer["conversation_id"]
        resp_id = bard_answer["response_id"]
        choice_id = bard_answer["choices"][0]["id"]
        params = {
            "rpcids": "fuVx7",
            "source-path": "/",
            "bl": "boq_assistant-bard-web-server_20230713.13_p0",
            # '_reqid': str(self._reqid),
            "rt": "c",
        }
        input_data_struct = [
            [
                [
                    "fuVx7",
                    json.dumps(
                        [
                            [
                                None,
                                [
                                    [
                                        [conv_id, resp_id],
                                        None,
                                        None,
                                        [[], [], [], choice_id, []],
                                    ]
                                ],
                                [0, title],
                            ]
                        ]
                    ),
                    None,
                    "generic",
                ]
            ]
        ]
        data = {
            "f.req": json.dumps(input_data_struct),
            "at": await self._get_snim0e(),
        }
        resp = await self.client.post(
            "https://bard.google.com/_/BardChatUi/data/batchexecute",
            params=params,
            data=data,
            timeout=self.timeout,
        )
        # Post-processing of response
        resp_dict = json.loads(resp.content.splitlines()[3])
        url_id = json.loads(resp_dict[0][2])[2]
        url = f"https://g.co/bard/share/{url_id}"
        # Increment request ID
        self._reqid += 100000
        return {
            "url": url,
            "status_code": resp.status_code,
        }

    async def export_replit(
        self, code: str, program_lang: str = None, filename: str = None, **kwargs
    ) -> str:
        """
        Get export URL to repl.it from code

        Example:
        >>> import asyncio
        >>>
        >>> async def main():
        >>>     token = 'xxxxxx'
        >>>     bard = BardAsync(token=token)
        >>>     bard_answer = await bard.get_answer("Give me python code to print hello world")
        >>>     url = await bard.export_replit(bard_answer['code'], bard_answer['program_lang'])
        >>>     print(url['url'])
        >>>
        >>> asyncio.run(main())

        Args:
            code (str): source code
            program_lang (str): programming language
            filename (str): filename
            **kwargs: instructions, source_path
        Returns:
            dict: Answer from the Bard API in the following format:
            {
                "url": str,
                "status_code": int
            }

        """
        params = {
            "rpcids": "qACoKe",
            "source-path": kwargs.get("source_path", "/"),
            "bl": "boq_assistant-bard-web-server_20230718.13_p2",
            "_reqid": str(self._reqid),
            "rt": "c",
        }
        support_langs = {
            "python": "main.py",
            "javascript": "index.js",
            "go": "main.go",
            "java": "Main.java",
            "kotlin": "Main.kt",
            "php": "index.php",
            "c#": "main.cs",
            "swift": "main.swift",
            "r": "main.r",
            "ruby": "main.rb",
            "c": "main.c",
            "c++": "main.cpp",
            "matlab": "main.m",
            "typescript": "main.ts",
            "scala": "main.scala",
            "sql": "main.sql",
            "html": "index.html",
            "css": "style.css",
            "nosql": "main.nosql",
            "rust": "main.rs",
            "perl": "main.pl",
        }
        # Reference: https://github.com/jincheng9/markdown_supported_languages
        if program_lang not in support_langs and filename is None:
            raise Exception(
                f"Language {program_lang} not supported, please set filename manually."
            )

        filename = (
            support_langs.get(program_lang, filename) if filename is None else filename
        )
        input_data_struct = [
            [
                [
                    "qACoKe",
                    json.dumps(
                        [kwargs.get("instructions", ""), 5, code, [[filename, code]]]
                    ),
                    None,
                    "generic",
                ]
            ]
        ]
        data = {
            "f.req": json.dumps(input_data_struct),
            "at": await self._get_snim0e(),
        }

        resp = await self.client.post(
            "https://bard.google.com/_/BardChatUi/data/batchexecute",
            params=params,
            data=data,
            timeout=self.timeout,
        )

        resp_dict = json.loads(resp.content.splitlines()[3])
        url = json.loads(resp_dict[0][2])[0]
        # Increment request ID
        self._reqid += 100000

        return {"url": url, "status_code": resp.status_code}

    async def ask_about_image(
        self, input_text: str, image: bytes, lang: str = None
    ) -> dict:
        """
        Send Bard image along with question and get answer async mode

        >>> import asyncio
        >>>
        >>> async def main():
        >>>     token = 'xxxxxx'
        >>>     bard = BardAsync(token=token)
        >>>     image = open('image.jpg', 'rb').read()
        >>>     bard_answer = await bard.ask_about_image("what is in the image?", image)
        >>>     print(bard_answer['content'])
        >>>
        >>> asyncio.run(main())

        Args:
            input_text (str): Input text for the query.
            image (bytes): Input image bytes for the query, support image types: jpeg, png, webp
            lang (str): Language to use.

        Returns:
            dict: Answer from the Bard API in the following format:
                {
                    "content": str,
                    "conversation_id": str,
                    "response_id": str,
                    "factuality_queries": list,
                    "text_query": str,
                    "choices": list,
                    "links": list,
                    "images": set,
                    "program_lang": str,
                    "code": str,
                    "status_code": int
                }
        """
        self.SNlM0e = await self._get_snim0e()
        if not isinstance(self.SNlM0e, str):
            self.SNlM0e = await self.SNlM0e

        if self.google_translator_api_key is not None:
            google_official_translator = translate.Client(
                api_key=self.google_translator_api_key
            )
        else:
            translator_to_eng = GoogleTranslator(source="auto", target="en")

        # [Optional] Set language
        if (
            (self.language is not None or lang is not None)
            and self.language not in ALLOWED_LANGUAGES
            and self.google_translator_api_key is None
        ):
            translator_to_eng = GoogleTranslator(source="auto", target="en")
            transl_text = translator_to_eng.translate(input_text)
        elif (
            (self.language is not None or lang is not None)
            and self.language not in ALLOWED_LANGUAGES
            and self.google_translator_api_key is not None
        ):
            transl_text = google_official_translator.translate(
                input_text, target_language="en"
            )
        elif (
            (self.language is None or lang is None)
            and self.language not in ALLOWED_LANGUAGES
            and self.google_translator_api_key is None
        ):
            translator_to_eng = GoogleTranslator(source="auto", target="en")
            transl_text = translator_to_eng.translate(input_text)

        # Supported format: jpeg, png, webp
        image_url = upload_image(image)

        input_data_struct = [
            None,
            [
                [transl_text, 0, None, [[[image_url, 1], "uploaded_photo.jpg"]]],
                [lang if lang is not None else self.language],
                ["", "", ""],
                "",  # Unknown random string value (1000 characters +)
                uuid.uuid4().hex,  # Should be random uuidv4 (32 characters)
                None,
                [1],
                0,
                [],
                [],
            ],
        ]
        params = {
            "bl": "boq_assistant-bard-web-server_20230716.16_p2",
            "_reqid": str(self._reqid),
            "rt": "c",
        }
        input_data_struct[1] = json.dumps(input_data_struct[1])
        data = {
            "f.req": json.dumps(input_data_struct),
            "at": self.SNlM0e,
        }

        resp = await self.client.post(
            "https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate",
            params=params,
            data=data,
        )

        # Post-processing of response
        resp_dict = json.loads(resp.content.splitlines()[3])[0][2]
        if not resp_dict:
            return {
                "content": f"Response Error: {resp.content}. "
                f"\nUnable to get response."
                f"\nPlease double-check the cookie values and verify your network environment or google account."
            }
        parsed_answer = json.loads(resp_dict)
        content = parsed_answer[4][0][1][0]
        try:
            if self.language is not None and self.google_translator_api_key is None:
                translator = GoogleTranslator(source="en", target=self.language)
                translated_content = translator.translate(content)

            elif lang is not None and self.google_translator_api_key is None:
                translator = GoogleTranslator(source="en", target=lang)
                translated_content = translator.translate(content)

            elif (
                lang is None and self.language is None
            ) and self.google_translator_api_key is None:
                us_lang = detect(input_text)
                translator = GoogleTranslator(source="en", target=us_lang)
                translated_content = translator.translate(content)

            elif (
                self.language is not None and self.google_translator_api_key is not None
            ):
                translated_content = google_official_translator.translate(
                    content, target_language=self.language
                )
            elif lang is not None and self.google_translator_api_key is not None:
                translated_content = google_official_translator.translate(
                    content, target_language=lang
                )
            elif (
                self.language is None and lang is None
            ) and self.google_translator_api_key is not None:
                us_lang = detect(input_text)
                translated_content = google_official_translator.translate(
                    content, target_language=us_lang
                )
        except Exception as e:
            print(f"Translation failed, and the original text has been returned. \n{e}")
            translated_content = content

        # Returnd dictionary object
        bard_answer = {
            "content": translated_content,
            "conversation_id": parsed_answer[1][0],
            "response_id": parsed_answer[1][1],
            "factuality_queries": parsed_answer[3],
            "text_query": parsed_answer[2][0] if parsed_answer[2] else "",
            "choices": [{"id": x[0], "content": x[1]} for x in parsed_answer[4]],
            "links": extract_links(parsed_answer[4]),
            "images": [""],
            "program_lang": "",
            "code": "",
            "status_code": resp.status_code,
        }
        self.conversation_id, self.response_id, self.choice_id = (
            bard_answer["conversation_id"],
            bard_answer["response_id"],
            bard_answer["choices"][0]["id"],
        )
        self._reqid += 100000
        return bard_answer
