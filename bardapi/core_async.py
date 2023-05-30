from json import loads, dumps
from re import search

from httpx import AsyncClient

from bardapi.core import Bard


class BardAsync(Bard):
    def __init__(self, token: str = None, timeout: int = 20, proxies: dict = None):
        """
        Initialize Bard Async Version

        :param token: (`str`, *optional*)
            __Secure-1PSID value. default to os.getenv("_BARD_API_KEY")
        :param timeout: (`int`, *optional*)
            Timeout in seconds when connecting bard server. The timeout is used on each request.
        :param proxies: (`Dict[str, str]`, *optional*)
            A dictionary of proxy servers to use by protocol or endpoint, e.g., `{'http': 'foo.bar:3128',
            'http://hostname': 'foo.bar:4012'}`. The proxies are used on each request.
        """
        super().__init__(token=token, timeout=timeout, proxies=proxies)
        self.client = AsyncClient(
            http2=True,
            headers=self.HEADERS,
            cookies={"__Secure-1PSID": self.token},
            timeout=self.timeout,
            proxies=self.proxies
        )

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

        resp = await self.client.get("https://bard.google.com/", timeout=self.timeout, follow_redirects=True)
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

    async def get_answer(self, input_text: str) -> dict:
        """
                Get the answer from Bard based on the input text.

                Example:
                >>> token = 'xxxxxxxxxx'
                >>> bard = Bard(token=token)
                >>> response = bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")
                >>> print(response['content'])

                :param input_text: (`str`)
                    The input text for which the answer is requested.

                :return: (`dict`)
                    The dictionary containing the response from Bard with the following keys:
                    - "content": The content of the answer.
                    - "conversation_id": The conversation ID.
                    - "response_id": The response ID.
                    - "factualityQueries": Factuality queries (if any).
                    - "textQuery": The text query used for the answer.
                    - "choices": The choices available (if any).
                    - "status_code": Response Status code,
                """
        if not isinstance(self.SNlM0e, str):
            self.SNlM0e = await self.SNlM0e
        params = {
            "bl": "boq_assistant-bard-web-server_20230419.00_p1",
            "_reqid": str(self._reqid),
            "rt": "c",
        }
        input_text_struct = [
            [input_text],
            None,
            [self.conversation_id, self.response_id, self.choice_id],
        ]
        data = {
            "f.req": dumps([None, dumps(input_text_struct)]),
            "at": self.SNlM0e,
        }

        resp = await self.client.post(
            "https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate",
            params=params,
            data=data,
            timeout=self.timeout,
            follow_redirects=True,
            headers=self.HEADERS,
            cookies={"__Secure-1PSID": self.token},
        )

        resp_dict = loads(resp.content.splitlines()[3])[0][2]

        if not resp_dict:
            return {"content": f"Response Error: {resp.content}."}
        parsed_answer = loads(resp_dict)
        bard_answer = {
            "content": parsed_answer[0][0],
            "conversation_id": parsed_answer[1][0],
            "response_id": parsed_answer[1][1],
            "factualityQueries": parsed_answer[3],
            "textQuery": parsed_answer[2][0] if parsed_answer[2] else "",
            "choices": [{"id": i[0], "content": i[1]} for i in parsed_answer[4]],
            "status_code": resp.status_code,
        }
        self.conversation_id, self.response_id, self.choice_id = (
            bard_answer["conversation_id"],
            bard_answer["response_id"],
            bard_answer["choices"][0]["id"],
        )
        self._reqid += 100000

        return bard_answer
