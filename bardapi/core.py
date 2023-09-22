import os
import re
import json
import uuid
import base64
import string
import random
import requests
from typing import Optional
from langdetect import detect
from deep_translator import GoogleTranslator
from google.cloud import translate_v2 as translate
from bardapi.constants import (
    ALLOWED_LANGUAGES,
    SESSION_HEADERS,
    REPLIT_SUPPORT_PROGRAM_LANGUAGES,
    TEXT_GENERATION_WEB_SERVER_PARAM,
)
from bardapi.utils import (
    build_input_replit_data_struct,
    build_image_bard_answer,
    build_export_data_structure,
    build_bard_answer,
    upload_image,
    extract_bard_cookie,
    build_input_text_struct,
    build_input_image_struct,
)


class Bard:
    """
    Bard class for interacting with the Google Bard.
    """

    def __init__(
        self,
        token: Optional[str] = None,
        timeout: int = 20,
        proxies: Optional[dict] = None,
        session: Optional[requests.Session] = None,
        conversation_id: Optional[str] = None,
        google_translator_api_key: Optional[str] = None,
        language: Optional[str] = None,
        run_code: bool = False,
        token_from_browser: bool = False,
    ):
        """
        Initialize the Bard instance.

        Args:
            token (str, optional): Bard API token.
            timeout (int, optional, default = 20): Request timeout in seconds.
            proxies (dict, optional): Proxy configuration for requests.
            session (requests.Session, optional): Requests session object.
            conversation_id (str, optional): ID to fetch conversational context
            google_translator_api_key (str, optional): Google cloud translation API key.
            language (str, optional): Natural language code for translation (e.g., "en", "ko", "ja").
            run_code (bool, optional, default = False): Whether to directly execute the code included in the answer (Python only)
            token_from_browser (bool, optional, default = False): Gets a token from the browser
        """
        self.token = self._get_token(token, token_from_browser)
        self.proxies = proxies
        self.timeout = timeout
        self._reqid = int("".join(random.choices(string.digits, k=4)))
        self.conversation_id = conversation_id or ""
        self.response_id = ""
        self.choice_id = ""
        self.session = self._get_session(session)
        self.SNlM0e = self._get_snim0e()
        self.language = language or os.getenv("_BARD_API_LANG")
        self.run_code = run_code
        self.google_translator_api_key = google_translator_api_key

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

    def _get_session(self, session: Optional[requests.Session]) -> requests.Session:
        """
        Get the requests Session object.

        Args:
            session (requests.Session): Requests session object.

        Returns:
            requests.Session: The Session object.
        """
        if session is None:
            new_session = requests.Session()
            new_session.headers = SESSION_HEADERS
            new_session.cookies.set("__Secure-1PSID", self.token)
            new_session.proxies = self.proxies
            return new_session
        else:
            return session

    def _get_snim0e(self) -> str:
        """
        Get the SNlM0e value from the Bard API response.

        Returns:
            str: SNlM0e value.
        Raises:
            Exception: If the __Secure-1PSID value is invalid or SNlM0e value is not found in the response.
        """
        if not self.token or self.token[-1] != ".":
            raise Exception(
                "__Secure-1PSID value must end with a single dot. Enter correct __Secure-1PSID value."
            )
        resp = self.session.get(
            "https://bard.google.com/", timeout=self.timeout, proxies=self.proxies
        )
        if resp.status_code != 200:
            raise Exception(
                f"Response status code is not 200. Response Status is {resp.status_code}"
            )
        snim0e = re.search(r"SNlM0e\":\"(.*?)\"", resp.text)
        if not snim0e:
            raise Exception(
                "SNlM0e value not found. Double-check __Secure-1PSID value or pass it as token='xxxxx'."
            )
        return snim0e.group(1)

    def get_answer(self, input_text: str) -> dict:
        """
        Get an answer from the Bard API for the given input text.

        Example:
        >>> token = 'xxxxxx'
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
        params = {
            "bl": TEXT_GENERATION_WEB_SERVER_PARAM,
            "_reqid": str(self._reqid),
            "rt": "c",
        }
        if self.google_translator_api_key is not None:
            google_official_translator = translate.Client(
                api_key=self.google_translator_api_key
            )

        # [Optional] Language translation
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
        input_text_struct = build_input_text_struct(
            input_text, self.conversation_id, self.response_id, self.choice_id
        )

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
            return {
                "content": f"Response Error: {resp.content}. "
                f"\nUnable to get response."
                f"\nPlease double-check the cookie values and verify your network environment or google account."
            }
        resp_json = json.loads(resp_dict)

        # [Optional] Gather image links
        images = list()
        try:
            if len(resp_json) >= 3:
                nested_list = resp_json[4][0][4]
                for img in nested_list:
                    images.append(img[0][0][0])
        except (IndexError, TypeError, KeyError):
            pass

        # Parsed Answer Object
        parsed_answer = json.loads(resp_dict)

        # [Optional] Translated by google translator
        # Unofficial
        if self.language is not None and self.language not in ALLOWED_LANGUAGES:
            if self.google_translator_api_key is None:
                translator_func = GoogleTranslator(
                    source="auto", target=self.language
                ).translate
            else:

                def translator_func(text):
                    return google_official_translator(
                        text, target_language=self.language
                    )

            parsed_answer[4] = [
                [x[0], [translator_func(x[1][0])] + x[1][1:], x[2]]
                for x in parsed_answer[4]
            ]

        # [Optional] Get program_lang & code
        try:
            program_lang = (
                parsed_answer[4][0][1][0].split("```")[1].split("\n")[0].strip()
            )
            code = parsed_answer[4][0][1][0].split("```")[1][len(program_lang) :]
        except Exception:
            program_lang, code = None, None

        # Returnd dictionary object
        bard_answer = build_bard_answer(parsed_answer, images, program_lang, code, resp)

        # Update params
        self.conversation_id, self.response_id, self.choice_id = (
            bard_answer["conversation_id"],
            bard_answer["response_id"],
            bard_answer["choices"][0]["id"],
        )
        self._reqid += 100000

        # [Optional] Execute code
        if self.run_code and bard_answer["code"] is not None:
            try:
                print(bard_answer["code"])
                exec(bard_answer["code"])
            except Exception:
                pass

        return bard_answer

    def speech(self, input_text: str, lang: str = "en-US") -> dict:
        """
        Get speech audio from Bard API for the given input text.

        Example:
        >>> token = 'xxxxxx'
        >>> bard = Bard(token=token)
        >>> audio = bard.speech("hello!")
        >>> with open("bard.ogg", "wb") as f:
        >>>     f.write(bytes(audio['audio']))

        Args:
            input_text (str): Input text for the query.
            lang (str, optional, default = "en-US"): Input language for the query.

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
                f"\nUnable to get response."
                f"\nPlease double-check the cookie values and verify your network environment or google account."
            }
        resp_json = json.loads(resp_dict)
        audio_b64 = resp_json[0]
        audio_bytes = base64.b64decode(audio_b64)
        return {"audio": audio_bytes, "status_code": resp.status_code}

    def export_conversation(self, bard_answer, title: str = "") -> dict:
        """
        Get Share URL for specific answer from bard

        Example:
        >>> token = 'xxxxxx'
        >>> bard = Bard(token=token)
        >>> bard_answer = bard.get_answer("hello!")
        >>> url = bard.export_conversation(bard_answer, title="Export Conversation")
        >>> print(url['url'])

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
            "rt": "c",
        }

        # Build data structure
        export_data_structure = build_export_data_structure(
            conv_id, resp_id, choice_id, title
        )

        data = {
            "f.req": json.dumps(export_data_structure),
            "at": self.SNlM0e,
        }
        resp = self.session.post(
            "https://bard.google.com/_/BardChatUi/data/batchexecute",
            params=params,
            data=data,
            timeout=self.timeout,
            proxies=self.proxies,
        )

        # Post-processing of response
        resp_dict = json.loads(resp.content.splitlines()[3])
        url_id = json.loads(resp_dict[0][2])[2]
        url = f"https://g.co/bard/share/{url_id}"

        # Increment request ID
        self._reqid += 100000
        return {"url": url, "status_code": resp.status_code}

    def ask_about_image(
        self, input_text: str, image: bytes, lang: Optional[str] = None
    ) -> dict:
        """
        Send Bard image along with question and get answer

        Example:
        >>> token = 'xxxxxx'
        >>> bard = Bard(token=token)
        >>> image = open('image.jpg', 'rb').read()
        >>> bard_answer = bard.ask_about_image("what is in the image?", image)['content']

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
        if self.google_translator_api_key is not None:
            google_official_translator = translate.Client(
                api_key=self.google_translator_api_key
            )
        else:
            translator_to_eng = GoogleTranslator(source="auto", target="en")

        # [Optional] Set language
        language_exists = self.language is not None or lang is not None
        language_not_allowed = self.language not in ALLOWED_LANGUAGES

        if language_not_allowed:
            translator_to_use = None

            # Choose translator
            if language_exists and self.google_translator_api_key is None:
                translator_to_use = GoogleTranslator(source="auto", target="en")
            elif language_exists and self.google_translator_api_key is not None:
                transl_text = google_official_translator.translate(
                    input_text, target_language="en"
                )
            elif not language_exists and self.google_translator_api_key is None:
                translator_to_use = GoogleTranslator(source="auto", target="en")

            # Using GoogleTranslator
            if translator_to_use:
                transl_text = translator_to_use.translate(input_text)

        # Supported format: jpg, jpeg, png, webp
        image_url = upload_image(image)

        # Create input data struct
        input_image_data_struct = build_input_image_struct(
            transl_text, image_url, lang=language_exists, default_language="en"
        )

        params = {
            "bl": TEXT_GENERATION_WEB_SERVER_PARAM,
            "_reqid": str(self._reqid),
            "rt": "c",
        }
        input_image_data_struct[1] = json.dumps(input_image_data_struct[1])
        data = {
            "f.req": json.dumps(input_image_data_struct),
            "at": self.SNlM0e,
        }

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
            return {
                "content": f"Response Error: {resp.content}. "
                f"\nUnable to get response."
                f"\nPlease double-check the cookie values and verify your network environment or google account."
            }
        parsed_answer = json.loads(resp_dict)
        content = parsed_answer[4][0][1][0]

        # [Optional] Translation
        try:
            target_language = (
                self.language or lang
            )  # Default to self.language, else use lang
            use_google_api = self.google_translator_api_key is not None

            # Determine target language if none is provided
            if not target_language:
                target_language = detect(input_text)

            # Translate using the appropriate method
            if use_google_api:
                translated_content = google_official_translator.translate(
                    content, target_language=target_language
                )
            else:
                translator = GoogleTranslator(source="en", target=target_language)
                translated_content = translator.translate(content)
        except Exception as e:
            print(f"Translation failed, and the original text has been returned. \n{e}")
            translated_content = content

        # Returned dictionary object
        bard_answer = build_image_bard_answer(translated_content, parsed_answer, resp)

        self.conversation_id, self.response_id, self.choice_id = (
            bard_answer["conversation_id"],
            bard_answer["response_id"],
            bard_answer["choices"][0]["id"],
        )
        self._reqid += 100000
        return bard_answer

    def export_replit(
        self,
        code: str,
        program_lang: Optional[str] = None,
        filename: Optional[str] = None,
        **kwargs,
    ) -> dict:
        """
        Get export URL to repl.it from code

        Example:
        >>> token = 'xxxxxx'
        >>> bard = Bard(token=token)
        >>> bard_answer = bard.get_answer("Give me python code to print hello world")
        >>> url = bard.export_replit(bard_answer['code'], bard_answer['program_lang'])
        >>> print(url['url'])

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

        # Reference: https://github.com/jincheng9/markdown_supported_languages
        if program_lang not in REPLIT_SUPPORT_PROGRAM_LANGUAGES and filename is None:
            raise Exception(
                f"Language {program_lang} not supported, please set filename manually."
            )

        filename = (
            REPLIT_SUPPORT_PROGRAM_LANGUAGES.get(program_lang, filename)
            if filename is None
            else filename
        )
        input_replit_data_struct = build_input_replit_data_struct(
            kwargs.get("instructions", ""), code, filename
        )

        data = {
            "f.req": json.dumps(input_replit_data_struct),
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

        resp_dict = json.loads(resp.content.splitlines()[3])
        print(f"Response: {resp_dict}")

        url = json.loads(resp_dict[0][2])[0]

        # Increment request ID
        self._reqid += 100000

        return {"url": url, "status_code": resp.status_code}
