import os
import string
import random
import json
import re
import requests
from deep_translator import GoogleTranslator
from google.cloud import translate_v2 as translate
from bardapi.constants import ALLOWED_LANGUAGES, SESSION_HEADERS, IMG_UPLOAD_HEADERS
import base64
import browser_cookie3
import uuid

class Bard:
    """
    Bard class for interacting with the Bard API.
    """

    def __init__(
        self,
        token: str = None,
        timeout: int = 20,
        proxies: dict = None,
        session: requests.Session = None,
        conversation_id: str = None,
        google_translator_api_key: str = None,
        language: str = None,
        run_code: bool = False,
        token_from_browser = False
    ):
        """
        Initialize the Bard instance.

        Args:
            token (str): Bard API token.
            timeout (int): Request timeout in seconds.
            proxies (dict): Proxy configuration for requests.
            session (requests.Session): Requests session object.
            conversation_id: ID to fetch conversational context
            google_translator_api_key (str): Google cloud translation API key.
            language (str): Language code for translation (e.g., "en", "ko", "ja").
            run_code (bool): Whether to directly execute the code included in the answer (Python only)
        """
        self.token = token or os.getenv("_BARD_API_KEY")
        if not self.token and token_from_browser:
            self.token = self._extract_bard_cookie()
            if not self.token:
                raise Exception("\nCan't extract cookie from browsers.\nPlease sign in first at\nhttps://accounts.google.com/v3/signin/identifier?followup=https://bard.google.com/&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        self.proxies = proxies
        self.timeout = timeout
        self._reqid = int("".join(random.choices(string.digits, k=4)))
        self.conversation_id = ""
        self.response_id = ""
        self.choice_id = ""
        if conversation_id is not None:
            self.conversation_id = conversation_id
        # Set session or Get session
        if session is None:
            self.session = requests.Session()
            self.session.headers = SESSION_HEADERS
            self.session.cookies.set("__Secure-1PSID", self.token)
        else:
            self.session = session
        self.SNlM0e = self._get_snim0e()
        self.language = language or os.getenv("_BARD_API_LANG")
        self.run_code = run_code or False
        self.google_translator_api_key = google_translator_api_key

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
                    "links": list,
                    "imgaes": set,
                    "code": str
                }
        """
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
                           f"\nTemporarily unavailable due to traffic or an error in cookie values. "
                           f"Please double-check the cookie values and verify your network environment."
            }
        resp_json = json.loads(resp_dict)

        # Gather image links (optional)
        images = set()
        try:
            if len(resp_json) >= 3:
                nested_list = resp_json[4][0][4]
                for img in nested_list:
                    images.add(img[0][0][0])
        except (IndexError, TypeError, KeyError):
            pass

        # Parsed Answer Object
        parsed_answer = json.loads(resp_dict)

        # Translated by Google Translator (optional)
        # Unofficial for testing
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
        # Official Google Cloud Translation API
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

        # Get code (optional)
        try:
            code = parsed_answer[4][0][1][0].split("```")[1][6:]
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
            "links": self._extract_links(parsed_answer[4]),
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
            except:
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

        input_text_struct = [[["XqA3Ic", json.dumps([None, input_text, lang, None, 2])]]]

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

    def _upload_image(self, image: bytes, filename='Photo.jpg'):
        """
        Upload image into bard bucket on Google API

        Returns:
            str: relative URL of image.
        """
        resp = requests.options('https://content-push.googleapis.com/upload/')
        resp.raise_for_status()
        size = len(image)

        headers = IMG_UPLOAD_HEADERS
        headers['size'] = str(size)

        data = 'File name: Photo.jpg'
        resp = requests.post('https://content-push.googleapis.com/upload/', headers=headers, data=data)
        resp.raise_for_status()
        upload_url = resp.headers['X-Goog-Upload-Url']
        resp = requests.options(upload_url, headers=headers)
        resp.raise_for_status()
        headers['x-goog-upload-command'] = 'upload, finalize'

        # It can be that we need to check returned offset
        headers['X-Goog-Upload-Offset'] = '0'
        resp = requests.post(upload_url, headers=headers, data=image)
        resp.raise_for_status()
        return resp.text


    def ask_about_image(self, input_text: str, image: bytes, lang = 'en-GB', filename='Photo.jpg') -> dict:
        """
        Send Bard image along with question and get answer

        Example:
        >>> token = 'xxxxxxxxxx'
        >>> bard = Bard(token=token)
        >>> image = open('image.jpg', 'rb').read()
        >>> bard_answer = bard.analyze_image("what is in the image?", image)

        Args:
            input_text (str): Input text for the query.
            image (bytes): Input image bytes for the query, support image types: jpeg, png, webp

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

        # jpeg, png, webp
        image_url = self._upload_image(image)

        input_data_struct = [
            None,
            [
                [input_text, 0, None, [[[image_url, 1], filename]]], [lang], ['', '', ''],
                '', # Unknown random string value (1000 characters +)
                uuid.uuid4().hex, # should be random uuidv4 (32 characters)
                None, [1] ,0 , [], []
            ]
        ]
        params = {
            "bl": "boq_assistant-bard-web-server_20230419.00_p1",
            "_reqid": str(self._reqid),
            "rt": "c",
        }

        input_data_struct[1] = json.dumps(input_data_struct[1])
        data = {
            "f.req": json.dumps(input_data_struct),
            "at": self.SNlM0e,
        }

        resp = self.session.post(
            'https://bard.google.com/u/1/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate',
            params=params,
            data=data,
        )
        # Post-processing of response
        resp_dict = json.loads(resp.content.splitlines()[3])[0][2]
        if not resp_dict:
            return {
                "content": f"Response Error: {resp.content}. "
                           f"\nTemporarily unavailable due to traffic or an error in cookie values. "
                           f"Please double-check the cookie values and verify your network environment."
            }
        parsed_answer = json.loads(resp_dict)

        # Returnd dictionary object
        bard_answer = {
            "content": parsed_answer[4][0][1][0],
            "conversation_id": parsed_answer[1][0],
            "response_id": parsed_answer[1][1],
            "factualityQueries": parsed_answer[3],
            "textQuery": parsed_answer[2][0] if parsed_answer[2] else "",
            "choices": [{"id": x[0], "content": x[1]} for x in parsed_answer[4]],
            "links": self._extract_links(parsed_answer[4]),
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

    def export_conversation(self, bard_answer, title: str = ''):
        """
        Get Share URL for specifc answer from bard

        Example:
        >>> token = 'xxxxxxxxxx'
        >>> bard = Bard(token=token)
        >>> bard_answer = bard.get_answer("hello!")
        >>> url = bard.export_conversation(bard_answer, title="Export Conversation")

        Args:
            bard_answer (dict): bard_answer returned from get_answer
            title (str): Title for URL
        Returns:
            string: public URL you can share
        """
        conv_id = bard_answer['conversation_id']
        resp_id = bard_answer['response_id']
        choice_id = bard_answer['choices'][0]['id']
        params = {
            'rpcids': 'fuVx7',
            'source-path': '/',
            'bl': 'boq_assistant-bard-web-server_20230713.13_p0',
            # '_reqid': str(self._reqid),
            'rt': 'c',
        }
        input_data_struct = [
            [[
                'fuVx7',
                json.dumps([[None, [[[conv_id, resp_id], None, None, [[], [], [], choice_id, []]]], [0, title]]]),
                None,
                'generic'
            ]]
        ]

        data = {
            "f.req": json.dumps(input_data_struct),
            "at": self.SNlM0e,
        }

        resp = self.session.post(
            'https://bard.google.com/_/BardChatUi/data/batchexecute',
            params=params,
            data=data,
        )
        # Post-processing of response
        resp_dict = json.loads(resp.content.splitlines()[3])
        url_id = json.loads(resp_dict[0][2])[2]
        url = f'https://g.co/bard/share/{url_id}'
        # increment request ID
        self._reqid += 100000
        return url

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
                f"Response code not 200. Response Status is {resp.status_code}"
            )
        snim0e = re.search(r"SNlM0e\":\"(.*?)\"", resp.text)
        if not snim0e:
            raise Exception(
                "SNlM0e value not found. Double-check __Secure-1PSID value or pass it as token='xxxxx'."
            )
        return snim0e.group(1)

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


    def _extract_bard_cookie(self):
        """
        Extract token cookie from browser.
        Supports all modern web browsers and OS


        Returns:
            str: __Secure-1PSID cookie value
        """

        # browser_cookie3.load is similar function but it's broken
        # So here we manually search accross all browsers
        browsers = [
            browser_cookie3.chrome, 
            browser_cookie3.chromium, 
            browser_cookie3.opera, 
            browser_cookie3.opera_gx, 
            browser_cookie3.brave, 
            browser_cookie3.edge, 
            browser_cookie3.vivaldi, 
            browser_cookie3.firefox, 
            browser_cookie3.librewolf, 
            browser_cookie3.safari
        ]
        for browser_fn in browsers:
            cj = browser_fn(domain_name='.google.com')
            for cookie in cj:
                if cookie.name == '__Secure-1PSID' and cookie.value.endswith('.'):
                    return cookie.value