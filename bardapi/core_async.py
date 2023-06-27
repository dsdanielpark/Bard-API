import os
import string
import random
import json
from re import search
from bardapi.constants import ALLOWED_LANGUAGES, SESSION_HEADERS
from deep_translator import GoogleTranslator
from google.cloud import translate_v2 as translate
from httpx import AsyncClient


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
    ):
        """
        Initialize the Bard instance.

        Args:
            token (str): Bard API token.
            timeout (int): Request timeout in seconds.
            proxies (dict): Proxy configuration for requests.
            language (str): Language code for translation (e.g., "en", "ko", "ja").
        """
        self.token = token or os.getenv("_BARD_API_KEY")
        self.proxies = proxies
        self.timeout = timeout
        self._reqid = int("".join(random.choices(string.digits, k=4)))
        self.conversation_id = ""
        self.response_id = ""
        self.choice_id = ""
        # Making Httpx Async Client that will be used for all API calls
        self.client = AsyncClient(
            http2=True,
            headers=SESSION_HEADERS,
            cookies={"__Secure-1PSID": self.token},
            timeout=self.timeout,
            proxies=self.proxies,
        )
        self.SNlM0e = self._get_snim0e()
        self.language = language or os.getenv("_BARD_API_LANG", "en")
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
                    "imgaes": set
                }
        """
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
            cookies={"__Secure-1PSID": self.token},
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
            print(f"Unable to parse answer from the response: {e}")

        # Returned dictionary object
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
        if not self.token or self.token[-1] != ".":
            raise Exception(
                "__Secure-1PSID value must end with a single dot. Enter correct __Secure-1PSID value."
            )

        resp = await self.client.get(
            "https://bard.google.com/", timeout=self.timeout, follow_redirects=True
        )
        if resp.status_code != 200:
            raise Exception(
                f"Response code not 200. Response Status is {resp.status_code}"
            )
        snim0e = search(r"SNlM0e\":\"(.*?)\"", resp.text)
        if not snim0e:
            raise Exception(
                "SNlM0e value not found in response. Check __Secure-1PSID value."
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
