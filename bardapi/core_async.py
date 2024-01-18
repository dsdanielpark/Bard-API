import os
import re
import json
import uuid
import string
import random
import base64
import logging
from re import search
from typing import Optional, Tuple, Union
from httpx import AsyncClient

try:
    from deep_translator import GoogleTranslator
    from google.cloud import translate_v2 as translate
    from langdetect import detect
except ImportError:
    pass

from bardapi.constants import (
    ALLOWED_LANGUAGES,
    SESSION_HEADERS,
    TEXT_GENERATION_WEB_SERVER_PARAM,
    Tool,
    POST_ENDPOINT,
)
from bardapi.models.result import BardResult
from bardapi.utils import (
    extract_links,
    build_input_replit_data_struct,
    build_export_data_structure,
    build_bard_answer,
    upload_image,
    extract_bard_cookie,
    build_input_text_struct,
)


class BardAsync:
    """
    BardAsync is a class for interacting with the Bard API asynchronously.

    Attributes:
        token (str): Bard API token.
        client (AsyncClient): Asynchronous client for making HTTP requests.
        conversation_id (str): ID to maintain the context of the conversation.
        google_translator_api_key (str): API key for Google Cloud Translation.
        language (str): The language in which the input text is written.
        run_code (bool): A flag to determine whether to execute code snippets.
        token_from_browser (bool): A flag to determine whether to get the token from the browser.
    """

    def __init__(
        self,
        token: Optional[str] = None,
        timeout: int = 30,
        proxies: Optional[dict] = None,
        client: Optional[AsyncClient] = None,
        conversation_id: Optional[str] = None,
        google_translator_api_key: Optional[str] = None,
        language: Optional[str] = None,
        run_code: bool = False,
        token_from_browser: bool = False,
    ):
        """
        Initialize the BardAsync class.

        Args:
            token (Optional[str]): Bard API token.
            timeout (int): Timeout for HTTP requests.
            proxies (Optional[dict]): Proxies for HTTP requests.
            client (Optional[AsyncClient]): Asynchronous client for making HTTP requests.
            conversation_id (Optional[str]): ID to maintain the context of the conversation.
            google_translator_api_key (Optional[str]): API key for Google Cloud Translation.
            language (Optional[str]): The language in which the input text is written.
            run_code (bool): A flag to determine whether to execute code snippets.
            token_from_browser (bool): A flag to determine whether to get the token from the browser.

        Raises:
            Exception: If the token is not provided and cannot be extracted from the environment variable.
        """
        self.token = self._get_token(token, token_from_browser)
        if not self.token:
            raise Exception(
                "Token must be provided either directly or through _BARD_API_KEY environment variable."
            )
        self.client = client or AsyncClient(
            http2=True,
            headers=SESSION_HEADERS,
            cookies={"__Secure-1PSID": self.token},
            timeout=timeout,
            proxies=proxies,
        )
        self.proxies = proxies
        self.timeout = timeout
        self._reqid = int("".join(random.choices(string.digits, k=4)))
        self.conversation_id = conversation_id or ""
        self.response_id = ""
        self.choice_id = ""
        self.client = client  # Will be initialized in async_setup
        self.language = language
        self.cookie_dict = {"__Secure-1PSID": self.token}
        self.run_code = run_code or False
        self.google_translator_api_key = google_translator_api_key
        self.SNlM0e = None

    async def async_setup(self) -> None:
        """
        Set up the BardAsync instance asynchronously.
        """
        self.SNlM0e = await self._get_snim0e()
        if not self.client:
            self.client = await self._get_client()  # Ensure this is awaited

    async def _get_snim0e(self) -> Optional[str]:
        """
        Get the SNlM0e value from the Bard website.

        Returns:
            Optional[str]: The SNlM0e value if found, otherwise None.
        """
        if isinstance(self.SNlM0e, str):
            return self.SNlM0e

        if not self.token or self.token[-1] != ".":
            print(
                "__Secure-1PSID value should end with a single dot. Enter correct __Secure-1PSID value."
            )

        resp = await self.client.get(
            "https://bard.google.com/", timeout=self.timeout, follow_redirects=True
        )
        if resp.status_code != 200:
            raise ConnectionError(
                f"Failed to fetch SNlM0e. Response status: {resp.status_code}"
            )
        snim0e_match = re.search(r"SNlM0e\":\"(.*?)\"", resp.text)
        if not snim0e_match:
            raise LookupError(
                "SNlM0e value not found in response. Check __Secure-1PSID value."
            )

        self.SNlM0e = snim0e_match.group(1)
        return self.SNlM0e

    async def _initialize_client(self) -> AsyncClient:
        """
        Initialize the AsyncClient instance.

        Returns:
            AsyncClient: The initialized AsyncClient instance.
        """
        return AsyncClient(
            http2=True,
            headers=SESSION_HEADERS,
            cookies=self.cookie_dict,
            timeout=self.timeout,
            proxies=self.proxies,
        )

    def _get_token(self, token: str, token_from_browser: bool) -> str:
        """
        Get the Bard API token either from the provided token or from the browser cookie.

        Args:
            token (str): Bard API token.
            token_from_browser (bool): Whether to extract the token from the browser cookie.

        Returns:
            str: The Bard API token.

        Raises:
            Exception: If the token is not provided and can't be extracted from the browser.
        """
        if token:
            return token
        elif os.getenv("_BARD_API_KEY"):
            return os.getenv("_BARD_API_KEY")
        elif token_from_browser:
            extracted_cookie_dict = extract_bard_cookie(cookies=False)
            if not extracted_cookie_dict:
                raise Exception("Failed to extract cookie from browsers.")
            return extracted_cookie_dict["__Secure-1PSID"]
        else:
            raise Exception(
                "Bard API Key must be provided as token argument or extracted from browser."
            )

    async def _get_client(self, session: Optional[AsyncClient]) -> AsyncClient:
        """
        Get or initialize the AsyncClient instance.

        Args:
            session (Optional[AsyncClient]): Existing AsyncClient instance.

        Returns:
            AsyncClient: The AsyncClient instance.
        """
        if session is None:
            async_client = AsyncClient(
                http2=True,
                headers=SESSION_HEADERS,
                cookies={"__Secure-1PSID": self.token},
                timeout=self.timeout,
                proxies=self.proxies,
            )
            return async_client
        else:
            assert type(session) == AsyncClient
            return session

    async def get_answer(self, input_text: str) -> dict:
        """
        Get the answer from the Bard API for the input text.

        Args:
            input_text (str): Text input for which the answer is sought.

        Returns:
            dict: The response from the Bard API.
        """
        params, data = self._prepare_request(input_text)
        resp = await self.client.post(
            POST_ENDPOINT,
            params=params,
            data=data,
            timeout=self.timeout,
            follow_redirects=True,
            headers=SESSION_HEADERS,
            cookies=self.cookie_dict,
        )
        return self._process_response(resp)

    def _prepare_request(self, input_text: str) -> Tuple[dict, dict]:
        """
        Prepare the request for the Bard API.

        Args:
            input_text (str): Text input for which the answer is sought.

        Returns:
            Tuple[dict, dict]: The parameters and data for the POST request.
        """
        # Translate the input text if the language is not allowed and a translator is available
        if self.language not in ALLOWED_LANGUAGES:
            if self.google_translator_api_key:
                # Translate using the official Google Cloud Translation API
                google_official_translator = translate.Client(
                    api_key=self.google_translator_api_key
                )
                input_text = google_official_translator.translate(
                    input_text, target_language="en"
                )
            else:
                # Translate using an unofficial translator
                translator_to_eng = GoogleTranslator(source="auto", target="en")
                input_text = translator_to_eng.translate(input_text)

        # Prepare the data structure for the POST request
        input_text_struct = [
            [input_text],
            None,
            [self.conversation_id, self.response_id, self.choice_id],
        ]
        data = {
            "f.req": json.dumps([None, json.dumps(input_text_struct)]),
            "at": self.SNlM0e,
        }

        # Prepare the parameters for the POST request
        params = {
            "bl": TEXT_GENERATION_WEB_SERVER_PARAM,
            "_reqid": str(self._reqid),
            "rt": "c",
        }
        return params, data

    def _process_response(self, resp) -> dict:
        """
        Process the response from the Bard API.

        Args:
            resp: The response from the Bard API.

        Returns:
            dict: The processed response.
        """
        if resp.status_code != 200:
            logging.error(f"Response status code: {resp.status_code}")
            return {"content": f"Response Error: {resp.content}."}

        resp_dict = json.loads(resp.content.splitlines()[3])[0][2]
        if not resp_dict:
            return {"content": f"Response Error: {resp.content}."}

        parsed_answer = json.loads(resp_dict)
        bard_answer = self._extract_answer(parsed_answer, resp)
        self._update_state(bard_answer)
        self._execute_code_if_needed(bard_answer)
        return bard_answer

    def _extract_answer(self, parsed_answer, resp) -> dict:
        """
        Extract the answer from the parsed response.

        Args:
            parsed_answer: The parsed response from the Bard API.
            resp: The original response from the Bard API.

        Returns:
            dict: The extracted answer.
        """
        # Assuming 'parsed_answer' is a dictionary that contains the required information
        bard_answer = {
            "content": parsed_answer[4][0][1][0],
            "conversation_id": parsed_answer[1][0],
            "response_id": parsed_answer[1][1],
            "factuality_queries": parsed_answer[3],
            "text_query": parsed_answer[2][0] if parsed_answer[2] else "",
            "choices": [{"id": x[0], "content": x[1]} for x in parsed_answer[4]],
            "links": self._extract_links(parsed_answer[4]),
            "images": [""],
            "program_lang": "",
            "code": "",
            "status_code": resp.status_code,
        }
        return bard_answer

    def _update_state(self, bard_answer) -> None:
        """
        Update the state with the latest conversation ID, response ID, and choice ID.

        Args:
            bard_answer (dict): The bard answer containing the state information.
        """
        self.conversation_id = bard_answer.get("conversation_id", "")
        self.response_id = bard_answer.get("response_id", "")
        choice_id = bard_answer.get("choices", [{}])[0].get("id", "")
        self.choice_id = choice_id if choice_id else self.choice_id
        self._reqid += 100000  # Increment _reqid for the next request

    def _execute_code_if_needed(self, bard_answer) -> None:
        """
        Execute code snippets if the `run_code` flag is set and code is present in the bard answer.

        Args:
            bard_answer (dict): The bard answer containing the code to execute.
        """
        if self.run_code and bard_answer.get("code"):
            code = bard_answer["code"]
            try:
                # Execute the code safely. It's important to consider security implications here.
                # You might want to restrict the types of code that can be executed.
                exec(code)
            except Exception as e:
                logging.error(f"Error executing code: {e}")

    def _extract_links(self, data: list) -> list:
        """
        Extract links from the given data.

        Args:
            data: Data to extract links from.

        Returns:
            list: Extracted links.
        """
        links = []
        if isinstance(data, list):
            for item in data:
                if isinstance(item, list):
                    links.extend(self._extract_links(item))
                elif (
                    isinstance(item, str)
                    and item.startswith("http")
                    and "favicon" not in item
                ):
                    links.append(item)
        return links

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
            lang (str, optional, default = "en-US"): Input language for the query

        Returns:
            dict: Answer from the Bard API in the following format:
            {
                "audio": bytes,
                "status_code": int
            }
        """
        params = {
            "bl": TEXT_GENERATION_WEB_SERVER_PARAM,
            "_reqid": str(self._reqid),
            "rt": "c",
        }

        input_text_struct = [
            [["XqA3Ic", json.dumps([None, input_text, lang, None, 2])]]
        ]

        data = {
            "f.req": json.dumps(input_text_struct),
            "at": self.SNlM0e,
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

    async def export_conversation(self, bard_answer, title: str = "") -> dict:
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
            title (str, optional, default = ""): Title for URL
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
            "bl": TEXT_GENERATION_WEB_SERVER_PARAM,
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
            "at": self.SNlM0e,
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
        self,
        code: str,
        program_lang: Optional[str] = None,
        filename: Optional[str] = None,
        **kwargs,
    ) -> dict:
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
            program_lang (str, optional): programming language
            filename (str, optional): filename
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
            "bl": TEXT_GENERATION_WEB_SERVER_PARAM,
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
            "at": self.SNlM0e,
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
        self, input_text: str, image: bytes, lang: Optional[str] = None
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
            lang (str, optional): Language to use.

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
                    "images": list,
                    "program_lang": str,
                    "code": str,
                    "status_code": int
                }
        """
        if not isinstance(self.SNlM0e, str):
            self.SNlM0e = await self.SNlM0e

        if self.google_translator_api_key is not None:
            google_official_translator = translate.Client(
                api_key=self.google_translator_api_key
            )
        else:
            translator_to_eng = GoogleTranslator(source="auto", target="en")

        # [Optional] Set language
        if self.language is None or lang is None:
            translated_input_text = input_text
        elif (
            (self.language is not None or lang is not None)
            and self.language not in ALLOWED_LANGUAGES
            and self.google_translator_api_key is None
        ):
            translator_to_eng = GoogleTranslator(source="auto", target="en")
            translated_input_text = translator_to_eng.translate(input_text)
        elif (
            (self.language is not None or lang is not None)
            and self.language not in ALLOWED_LANGUAGES
            and self.google_translator_api_key is not None
        ):
            translated_input_text = google_official_translator.translate(
                input_text, target_language="en"
            )
        elif (
            (self.language is None or lang is None)
            and self.language not in ALLOWED_LANGUAGES
            and self.google_translator_api_key is None
        ):
            translator_to_eng = GoogleTranslator(source="auto", target="en")
            translated_input_text = translator_to_eng.translate(input_text)

        # Supported format: jpeg, png, webp
        image_url = upload_image(image)

        input_data_struct = [
            None,
            [
                [
                    translated_input_text,
                    0,
                    None,
                    [[[image_url, 1], "uploaded_photo.jpg"]],
                ],
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
            "bl": TEXT_GENERATION_WEB_SERVER_PARAM,
            "_reqid": str(self._reqid),
            "rt": "c",
        }
        input_data_struct[1] = json.dumps(input_data_struct[1])
        data = {
            "f.req": json.dumps(input_data_struct),
            "at": self.SNlM0e,
        }

        resp = await self.client.post(
            POST_ENDPOINT,
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
            if self.language is None and self.google_translator_api_key is None:
                translated_content = content
            elif self.language is not None and self.google_translator_api_key is None:
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

    async def ask(
        self,
        text: str,
        image: Optional[bytes] = None,
        image_name: Optional[str] = None,
        tool: Optional[Tool] = None,
    ) -> BardResult:
        if not isinstance(self.SNlM0e, str):
            self.SNlM0e = await self.SNlM0e

        if image is not None:
            image_url = upload_image(image)
        else:
            image_url = None

        # Make post data structure and insert prompt
        input_text_struct = build_input_text_struct(
            text,
            self.conversation_id,
            self.response_id,
            self.choice_id,
            image_url,
            image_name,
            tools=[tool.value] if tool is not None else None,
        )

        # Get response
        resp = await self.client.post(
            POST_ENDPOINT,
            params={
                "bl": TEXT_GENERATION_WEB_SERVER_PARAM,
                "_reqid": str(self._reqid),
                "rt": "c",
            },
            data={
                "f.req": json.dumps([None, json.dumps(input_text_struct)]),
                "at": self.SNlM0e,
            },
            timeout=self.timeout,
        )

        if resp.status_code != 200:
            raise Exception(
                f"Response status code is not 200. Response Status is {resp.status_code}"
            )

        lines = [
            line for line in resp.content.splitlines() if line.startswith(b'[["wrb.fr')
        ]
        jsons = [json.loads(json.loads(line)[0][2]) for line in lines]
        # Post-processing of response
        resp_json = jsons[-1]

        if not resp_json:
            raise {
                "content": f"Response Error: {resp.content}. "
                f"\nUnable to get response."
                f"\nPlease double-check the cookie values and verify your network environment or google account."
            }

        res = BardResult(resp_json)
        if not res.drafts:
            res = BardResult(jsons[-2])

        # Update params
        self.conversation_id, self.response_id, self.choice_id = (
            res.conversation_id,
            res.response_id,
            res.drafts[0].id,
        )
        self._reqid += 100000

        return res
