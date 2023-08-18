import os
import re
import string
import random
import requests
from httpx import AsyncClient
from bardapi.core import Bard
from bardapi.core_async import BardAsync
from bardapi.constants import SESSION_HEADERS
from bardapi.utils import extract_bard_cookie


class BardCookies(Bard):
    """
    Bard class for interacting with the Bard API using cookies for authentication.
    """

    def __init__(
        self,
        cookie_dict: dict = None,
        timeout: int = 20,
        proxies: dict = None,
        session: requests.Session = None,
        conversation_id: str = None,
        google_translator_api_key: str = None,
        language: str = None,
        run_code: bool = False,
        token_from_browser: bool = False,
    ):
        """
        Initialize the BardCookies instance.

        Args:
            cookie_dict (dict, optional): Dictionary containing Bard cookies.
            timeout (int, optional): Request timeout in seconds.
            proxies (dict, optional): Proxy configuration for requests.
            session (requests.Session, optional): Requests session object.
            conversation_id (str, optional): Conversation ID.
            google_translator_api_key (str, optional): Google Cloud Translation API key.
            language (str, optional): Natural language code for translation.
            run_code (bool, optional): Whether to execute code included in the answer (Python only).
            token_from_browser (bool, optional): Whether to extract the token from browser cookies.
        """
        self.cookie_dict = cookie_dict or self._get_token("", token_from_browser)
        self.proxies = proxies
        self.timeout = timeout
        self._reqid = int("".join(random.choices(string.digits, k=4)))
        self.conversation_id = conversation_id or ""
        self.response_id = ""
        self.choice_id = ""

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
        self.google_translator_api_key = google_translator_api_key

    def _get_token(self, _, token_from_browser):
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
        if token_from_browser:
            extracted_cookie_dict = extract_bard_cookie(cookies=True)
            if not extracted_cookie_dict:
                raise Exception("Failed to extract cookie from browsers.")
            return extracted_cookie_dict
        else:
            raise Exception(
                "Bard API Key must be provided as token argument or extracted from browser."
            )

    def get_answer(self, input_text: str) -> dict:
        """
        Get an answer from the Bard API for the given input text.

        Args:
            input_text (str): Input text for the query.

        Returns:
            dict: Answer from the Bard API.
        """
        return super().get_answer(input_text)

    def speech(self, input_text: str, lang="en-US") -> dict:
        """
        Get speech audio from Bard API for the given input text.

        Example:
        >>> cookies = {
        >>>   "__Secure-1PSID": "",
        >>>   "__Secure-1PSIDTS": ""
        >>> }
        >>> bard = BardCookies(cookie_dict=cookies)
        >>> audio = bard.speech("hello!")
        >>> with open("bard.ogg", "wb") as f:
        >>>     f.write(bytes(audio['audio']))

        Args:
            input_text (str): Input text for the query.
            lang (str): Input language for the query.

        Returns:
            dict: Answer from the Bard API in the following format:
            {
                "audio": bytes,
                "status_code": int
            }
        """
        return super().speech(input_text, lang)

    def ask_about_image(self, input_text: str, image: bytes, lang: str = None) -> dict:
        """
        Example:
        >>> cookies = {
        >>>   "__Secure-1PSID": "",
        >>>   "__Secure-1PSIDTS": ""
        >>> }
        >>> bard = BardCookies(cookie_dict=cookies)
        >>> image = open('image.jpg', 'rb').read()
        >>> bard_answer = bard.ask_about_image("what is in the image?", image)['content']
        >>> print(bard_answer)

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
        return super().ask_about_image(input_text, image, lang)

    def export_conversation(self, bard_answer, title: str = ""):
        """
        Get Share URL for specific answer from bard

        Example:
        >>> cookies = {
        >>>   "__Secure-1PSID": "",
        >>>   "__Secure-1PSIDTS": ""
        >>> }
        >>> bard = BardCookies(cookie_dict=cookies)
        >>> bard_answer = bard.get_answer("hello!")
        >>> url = bard.export_conversation(bard_answer, title="Export Conversation")
        >>> print(url['url'])

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
        return super().export_conversation(bard_answer, title)

    def export_replit(
        self, code: str, program_lang: str = None, filename: str = None, **kwargs
    ):
        """
        Get export URL to repl.it from code

        Example:
        >>> cookies = {
        >>>   "__Secure-1PSID": "",
        >>>   "__Secure-1PSIDTS": ""
        >>> }
        >>> bard = BardCookies(cookie_dict=cookies)
        >>> bard_answer = bard.get_answer("code python to print hello world")
        >>> url = bard.export_replit(bard_answer['code'], bard_answer['program_lang'])
        >>> print(url['url'])

        Args:
            code (str): source code
            program_lang (str): programming language
            filename (str): filename for code
            **kwargs: instructions, source_path
        Returns:
            dict: Answer from the Bard API in the following format:
            {
                "url": str,
                "status_code": int
            }
        """
        return super().export_replit(code, program_lang, filename, **kwargs)

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
                f"Response status code is not 200. Response Status is {resp.status_code}"
            )
        snim0e = re.search(r"SNlM0e\":\"(.*?)\"", resp.text)
        if not snim0e:
            raise Exception(
                "SNlM0e value not found in response. Check __Secure-1PSID value."
            )
        return snim0e.group(1)


class BardAsyncCookies(BardAsync):
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
            cookie_dict (dict): Bard cookies.
            timeout (int): Request timeout in seconds.
            proxies (dict): Proxy configuration for requests.
            google_translator_api_key (str): Google cloud translation API key.
            language (str): Natural language code for translation (e.g., "en", "ko", "ja").
            run_code (bool): Whether to directly execute the code included in the answer (Python only)
        """
        self.cookie_dict = cookie_dict
        self.timeout = timeout
        self.proxies = proxies
        self._reqid = int("".join(random.choices(string.digits, k=4)))
        self.conversation_id = ""
        self.response_id = ""
        self.choice_id = ""
        # Making httpx async client that will be used for all API calls
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
        >>> import asyncio
        >>>
        >>> async def main():
        >>>     cookies = {
        >>>             "__Secure-1PSID": "",
        >>>             "__Secure-1PSIDTS": ""
        >>>         }
        >>>     bard = BardAsyncCookies(cookie_dict=cookies)
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
        return await super().get_answer(input_text)

    async def speech(self, input_text: str, lang: str = "en-US") -> dict:
        """
        Get speech audio from Bard API for the given input text.

        Example:
        >>> import asyncio
        >>>
        >>> async def main():
        >>>     cookies = {
        >>>             "__Secure-1PSID": "",
        >>>             "__Secure-1PSIDTS": ""
        >>>         }
        >>>     bard = BardAsyncCookies(cookie_dict=cookies)
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

        return await super().speech(input_text, lang)

    async def ask_about_image(
        self, input_text: str, image: bytes, lang: str = None
    ) -> dict:
        """
        Send Bard image along with question and get answer async mode

        Example:
        >>> import asyncio
        >>>
        >>> async def main():
        >>>     cookies = {
        >>>             "__Secure-1PSID": "",
        >>>             "__Secure-1PSIDTS": ""
        >>>         }
        >>>     bard = BardAsyncCookies(cookie_dict=cookies)
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
        return await super().ask_about_image(input_text, image, lang)

    async def export_conversation(self, bard_answer, title: str = "") -> str:
        """
        Get Share URL for specific answer from bard

        Example:
        >>> import asyncio
        >>>
        >>> async def main():
        >>>     cookies = {
        >>>             "__Secure-1PSID": "",
        >>>             "__Secure-1PSIDTS": ""
        >>>         }
        >>>     bard = BardAsyncCookies(cookie_dict=cookies)
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
        return await super().export_conversation(bard_answer, title)

    async def export_replit(
        self, code: str, program_lang: str = None, filename: str = None, **kwargs
    ) -> str:
        """
        Get export URL to repl.it from code

        Example:
        >>> import asyncio
        >>>
        >>> async def main():
        >>>     cookies = {
        >>>             "__Secure-1PSID": "",
        >>>             "__Secure-1PSIDTS": ""
        >>>         }
        >>>     bard = BardAsyncCookies(cookie_dict=cookies)
        >>>     bard_answer = await bard.get_answer("code python to print hello world")
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

        return await super().export_replit(code, program_lang, filename, **kwargs)

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
                f"Response status code is not 200. Response Status is {resp.status_code}"
            )
        snim0e = re.search(r"SNlM0e\":\"(.*?)\"", resp.text)
        if not snim0e:
            raise Exception(
                "SNlM0e value not found in response. Check __Secure-1PSID value."
            )
        return snim0e.group(1)
