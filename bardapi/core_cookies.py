import os
import string
import random
from langdetect import detect
import json
import re
import requests
import base64
from deep_translator import GoogleTranslator
from bardapi.constants import ALLOWED_LANGUAGES, SESSION_HEADERS
import uuid
from httpx import AsyncClient
from deep_translator import GoogleTranslator
from google.cloud import translate_v2 as translate
from bardapi.constants import ALLOWED_LANGUAGES, SESSION_HEADERS
from bardapi.utils import extract_links, upload_image, extract_bard_cookie


class BardCookies:
    """
    Bard class for interacting with the Bard API.
    """

    def __init__(
        self,
        cookie_dict: dict = None,
        timeout: int = 20,
        proxies: dict = None,
        session: requests.Session = None,
        language: str = None,
        run_code: bool = False,
    ):
        """
        Initialize the Bard instance.

        Args:
            cookie_dict (dict): Bard cookies.
            timeout (int): Request timeout in seconds.
            proxies (dict): Proxy configuration for requests.
            session (requests.Session): Requests session object.
            language (str): Language code for translation (e.g., "en", "ko", "ja").
        """
        self.cookie_dict = cookie_dict
        self.proxies = proxies
        self.timeout = timeout
        self._reqid = int("".join(random.choices(string.digits, k=4)))
        self.conversation_id = ""
        self.response_id = ""
        self.choice_id = ""
        # Set session
        if session is None:
            self.session = requests.Session()
            self.session.headers = SESSION_HEADERS

            for k, v in self.cookie_dict.items():
                self.session.cookies.set(k, v)
        else:
            self.session = session
        self.SNlM0e = self._get_snim0e()
        self.language = language or os.getenv("_BARD_API_LANG")
        self.run_code = run_code or False

    def get_answer(self, input_text: str) -> dict:
        """
        Get an answer from the Bard API for the given input text.

        Example:
        >>> token = 'xxxxxxxxxx'
        >>> bard = Bard(token=token)
        >>> response = bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")
        >>> print(response['content'])

        Args:
            input_text (str): Input text for the query.

        Returns:
            dict: Answer from the Bard API in the following format:
                {
                    "content": str,
                    "conversation_id": str,
                    "response_id": str,
                    "factualityQueries": list,
                    "textQuery": str,
                    "choices": list,
                    "links": list
                    "images": set
                }
        """
        params = {
            "bl": "boq_assistant-bard-web-server_20230419.00_p1",
            "_reqid": str(self._reqid),
            "rt": "c",
        }
        # Set language (optional)
        if self.language is not None and self.language not in ALLOWED_LANGUAGES:
            translator_to_eng = GoogleTranslator(source="auto", target="en")
            input_text = translator_to_eng.translate(input_text)

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

        # Get response
        resp = self.session.post(
            "https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate",
            params=params,
            data=data,
            timeout=self.timeout,
            proxies=self.proxies,
        )

        # Post-processing of response
        resp_dict = json.loads(resp.content.splitlines()[3])[0][2]

        if not resp_dict:
            return {"content": f"Response Error: {resp.content}."}
        resp_json = json.loads(resp_dict)

        # Gather image links
        images = set()
        if len(resp_json) >= 3:
            if len(resp_json[4][0]) >= 4 and resp_json[4][0][4] is not None:
                for img in resp_json[4][0][4]:
                    try:
                        images.add(img[0][0][0])
                    except Exception:
                        pass
        parsed_answer = json.loads(resp_dict)

        # Translated by Google Translator (optional)
        if self.language is not None and self.language not in ALLOWED_LANGUAGES:
            translator_to_lang = GoogleTranslator(source="auto", target=self.language)
            parsed_answer[0][0] = translator_to_lang.translate(parsed_answer[0][0])
            parsed_answer[4] = [
                (x[0], translator_to_lang.translate(x[1][0])) for x in parsed_answer[4]
            ]

        # Get code
        try:
            code = parsed_answer[0][0].split("```")[1][6:]
        except Exception:
            code = None

        # Returnd dictionary object
        bard_answer = {
            "content": parsed_answer[4][0][1][0],
            "conversation_id": parsed_answer[1][0],
            "response_id": parsed_answer[1][1],
            "factualityQueries": parsed_answer[3],
            "textQuery": parsed_answer[2][0] if parsed_answer[2] else "",
            "choices": [{"id": x[0], "content": x[1]} for x in parsed_answer[4]],
            "links": extract_links(parsed_answer[4]),
            "images": images,
            "code": code,
        }
        self.conversation_id, self.response_id, self.choice_id = (
            bard_answer["conversation_id"],
            bard_answer["response_id"],
            bard_answer["choices"][0]["id"],
        )
        self._reqid += 100000

        # Excute Code
        if self.run_code and bard_answer["code"] is not None:
            try:
                print(bard_answer["code"])
                exec(bard_answer["code"])
            except Exception:
                pass

        return bard_answer

    def speech(self, input_text: str, lang="en-US") -> dict:
        """
        Get speech audio from Bard API for the given input text.

        Example:
        >>> token = 'xxxxxxxxxx'
        >>> bard = Bard(token=token)
        >>> audio = bard.speech("hello!")

        Args:
            input_text (str): Input text for the query.
            lang (str): Input language for the query

        Returns:
            bytes: audio in bytes format
            with format of audio/ogg
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
            "at": self.SNlM0e,
        }

        # Get response
        resp = self.session.post(
            "https://bard.google.com/_/BardChatUi/data/batchexecute",
            params=params,
            data=data,
            timeout=self.timeout,
            proxies=self.proxies,
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
        return audio_bytes

    def _get_snim0e(self) -> str:
        """
        Get the SNlM0e value from the Bard API response.

        Returns:
            str: SNlM0e value.
        Raises:
            Exception: If the __Secure-1PSID value is invalid or SNlM0e value is not found in the response.
        """
        resp = self.session.get(
            "https://bard.google.com/", timeout=self.timeout, proxies=self.proxies
        )
        if resp.status_code != 200:
            raise Exception(
                f"Response code not 200. Response Status is {resp.status_code}"
            )
        snim0e = re.search(r"SNlM0e\":\"(.*?)\"", resp.text)
        if not snim0e:
            raise Exception(
                "SNlM0e value not found in response. Check __Secure-1PSID value."
            )
        return snim0e.group(1)

    # def auth(self): #Idea Contribution
    #     url = 'https://bard.google.com'
    #     driver_path = "/path/to/chromedriver"
    #     options = uc.ChromeOptions()
    #     options.add_argument("--ignore-certificate-error")
    #     options.add_argument("--ignore-ssl-errors")
    #     options.user_data_dir = "path_to _user-data-dir"
    #     driver = uc.Chrome(options=options)
    #     driver.get(url)
    #     cookies = driver.get_cookies()
    #     # Find the __Secure-1PSID cookie
    #     for cookie in cookies:
    #         if cookie['name'] == '__Secure-1PSID':
    #             print("__Secure-1PSID cookie:")
    #             print(cookie['value'])
    #             os.environ['_BARD_API_KEY']=cookie['value']
    #             break
    #     else:
    #         print("No __Secure-1PSID cookie found")
    #     driver.quit()


class BardAsyncCookies:
    """
    Bard class for interacting with the Bard API using httpx[http2]
    """

    def __init__(
        self,
        cookie_dict: dict = None,
        timeout: int = 20,
        proxies: dict = None,
        google_translator_api_key: str = None,
        language: str = None,
        run_code: bool = False,
    ):
        """
        Initialize the Bard instance.

        Args:
            token (str): Bard API token.
            timeout (int): Request timeout in seconds.
            proxies (dict): Proxy configuration for requests.
            language (str): Language code for translation (e.g., "en", "ko", "ja").
        """
        self.cookie_dict = cookie_dict
        self.timeout = timeout
        self.proxies = proxies
        self._reqid = int("".join(random.choices(string.digits, k=4)))
        self.conversation_id = ""
        self.response_id = ""
        self.choice_id = ""
        # Making Httpx Async Client that will be used for all API calls
        self.client = AsyncClient(
            http2=True,
            cookies=self.cookie_dict,
            headers=SESSION_HEADERS,
            timeout=self.timeout,
            proxies=self.proxies,
        )
        self.language = language
        self.run_code = run_code or False
        self.google_translator_api_key = google_translator_api_key

    async def get_answer(self, input_text: str) -> dict:
        """
        Get an answer from the Bard API for the given input text.

        Example:
        >>> token = 'xxxxxxxxxx'
        >>> bard = Bard(token=token)
        >>> response = bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")
        >>> print(response['content'])

        Args:
            input_text (str): Input text for the query.

        Returns:
            dict: Answer from the Bard API in the following format:
                {
                    "content": str,
                    "conversation_id": str,
                    "response_id": str,
                    "factualityQueries": list,
                    "textQuery": str,
                    "choices": list,
                    "links": list
                    "images": set
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

        # Set language (optional)
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

        # Gather image links (optional)
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

        # Translated by Google Translator (optional)
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
        ## Official Google Cloud Translation API
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
            code = parsed_answer[4][0][1][0].split("```")[1][6:]
        except Exception as e:
            # TODO:
            #  handle exception using logging instead
            code = None

        # Returned dictionary object
        bard_answer = {
            "content": parsed_answer[4][0][1][0],
            "conversation_id": parsed_answer[1][0],
            "response_id": parsed_answer[1][1],
            "factualityQueries": parsed_answer[3],
            "textQuery": parsed_answer[2][0] if parsed_answer[2] else "",
            "choices": [{"id": x[0], "content": x[1]} for x in parsed_answer[4]],
            "links": extract_links(parsed_answer[4]),
            "images": images,
            "code": code,
            "status_code": resp.status_code,
        }

        self.conversation_id, self.response_id, self.choice_id = (
            bard_answer["conversation_id"],
            bard_answer["response_id"],
            bard_answer["choices"][0]["id"],
        )
        self._reqid += 100000

        # Execute Code
        if self.run_code and bard_answer["code"] is not None:
            try:
                print(bard_answer["code"])
                # TODO:
                #  find a way to handle this following warning
                #  EX100: Use of builtin exec function for dynamic input is insecure and can leave your application
                #  open to arbitrary code execution. Found in 'exec(bard_answer['code'])'.
                exec(bard_answer["code"])
            except Exception as e:
                # TODO:
                #  handle exception using logging instead
                print(f"Unable to execute the code: {e}")

        return bard_answer

    async def _get_snim0e(self):
        """
        The _get_snim0e function is used to get the SNlM0e value from the Bard website.

        The function uses a regular expression to search for the SNlM0e value in the response text.
        If it finds it, then it returns that value.

        :param self: Represent the instance of the class
        :return: (`str`) The snlm0e value
        """

        resp = await self.client.get(
            "https://bard.google.com/", timeout=self.timeout, follow_redirects=True
        )
        if resp.status_code != 200:
            raise Exception(
                f"Response code not 200. Response Status is {resp.status_code}"
            )
        snim0e = re.search(r"SNlM0e\":\"(.*?)\"", resp.text)
        if not snim0e:
            raise Exception(
                "SNlM0e value not found in response. Check __Secure-1PSID value."
            )
        return snim0e.group(1)

    async def ask_about_image(
        self, input_text: str, image: bytes, lang: str = None
    ) -> dict:
        """
        Send Bard image along with question and get answer async mode

        Example:
        >>> token = 'xxxxxxxxxx'
        >>> bard = Bard(token=token)
        >>> image = open('image.jpg', 'rb').read()
        >>> bard_answer = bard.analyze_image("what is in the image?", image)

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
                    "factualityQueries": list,
                    "textQuery": str,
                    "choices": list,
                    "links": list,
                    "imgaes": set,
                    "code": str
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

        # Set language (optional)
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
                [lang],
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
        if self.language is not None and self.google_translator_api_key is None:
            translator = GoogleTranslator(source="en", target=self.language)
            transl_content = translator.translate(content)

        elif lang is not None and self.google_translator_api_key is None:
            translator = GoogleTranslator(source="en", target=lang)
            transl_content = translator.translate(content)

        elif (
            lang is None and self.language is None
        ) and self.google_translator_api_key is None:
            us_lang = detect(input_text)
            translator = GoogleTranslator(source="en", target=us_lang)
            transl_content = translator.translate(content)

        elif self.language is not None and self.google_translator_api_key is not None:
            transl_content = google_official_translator.translate(
                content, target_language=self.language
            )
        elif lang is not None and self.google_translator_api_key is not None:
            transl_content = google_official_translator.translate(
                content, target_language=lang
            )
        elif (
            self.language is None and lang is None
        ) and self.google_translator_api_key is not None:
            us_lang = detect(input_text)
            transl_content = google_official_translator.translate(
                content, target_language=us_lang
            )

        # Returnd dictionary object
        bard_answer = {
            "content": transl_content,
            "conversation_id": parsed_answer[1][0],
            "response_id": parsed_answer[1][1],
            "factualityQueries": parsed_answer[3],
            "textQuery": parsed_answer[2][0] if parsed_answer[2] else "",
            "choices": [{"id": x[0], "content": x[1]} for x in parsed_answer[4]],
            "links": extract_links(parsed_answer[4]),
            "images": [""],
            "code": "",
        }
        self.conversation_id, self.response_id, self.choice_id = (
            bard_answer["conversation_id"],
            bard_answer["response_id"],
            bard_answer["choices"][0]["id"],
        )
        self._reqid += 100000
        return bard_answer

    async def speech(self, input_text: str, lang="en-US") -> dict:
        """
        Get speech audio from Bard API for the given input text.

        Example:
        >>> token = 'xxxxxxxxxx'
        >>> bard = Bard(token=token)
        >>> audio = bard.speech("hello!")

        Args:
            input_text (str): Input text for the query.
            lang (str): Input language for the query

        Returns:
            bytes: audio in bytes format
            with format of audio/ogg
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
        return audio_bytes
