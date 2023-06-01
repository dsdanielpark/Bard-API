import os
import string
import random
import json
import re
import requests
from deep_translator import GoogleTranslator
from bardapi.constants import ALLOWED_LANGUAGES, SESSION_HEADERS


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
                    "imgaes": set
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
            "content": parsed_answer[0][0],
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
            except Exception:
                pass

        return bard_answer

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
