import json
import random
import re
import string
import os
import requests


class Bard:
    def __init__(self):
        headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
        self._reqid = int("".join(random.choices(string.digits, k=4)))
        self.conversation_id = ""
        self.response_id = ""
        self.choice_id = ""
        self.session = requests.Session()
        self.session.headers = headers
        self.session.cookies.set("__Secure-1PSID", os.environ["_BARD_API_KEY"])
        self.SNlM0e = self._get_snim0e()

    def _get_snim0e(self):
        resp = self.session.get(url="https://bard.google.com/", timeout=5)
        if resp.status_code != 200:
            raise Exception(f"Response Status: {resp.status_code}")
        return re.search(r"SNlM0e\":\"(.*?)\"", resp.text).group(1)

    def get_answer(self, question: str) -> dict:
        params = {
            "bl": "boq_assistant-bard-web-server_20230419.00_p1",
            "_reqid": str(self._reqid),
            "rt": "c",
        }
        question_struct = [
            [question],
            None,
            [self.conversation_id, self.response_id, self.choice_id],
        ]
        data = {
            "f.req": json.dumps([None, json.dumps(question_struct)]),
            "at": self.SNlM0e,
        }
        resp = self.session.post(
            "https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate",
            params=params,
            data=data,
            timeout=100,
        )

        resp_dict = json.loads(resp.content.splitlines()[3])[0][2]
        if resp_dict is None:
            return {"content": f"Response Error: {resp.content}."}
        parsed_answer = json.loads(resp_dict)
        bard_answer = {
            "content": parsed_answer[0][0],
            "conversation_id": parsed_answer[1][0],
            "response_id": parsed_answer[1][1],
            "factualityQueries": parsed_answer[3],
            "textQuery": parsed_answer[2][0] if parsed_answer[2] is not None else "",
            "choices": [{"id": i[0], "content": i[1]} for i in parsed_answer[4]],
        }
        self.conversation_id = bard_answer["conversation_id"]
        self.response_id = bard_answer["response_id"]
        self.choice_id = bard_answer["choices"][0]["id"]
        self._reqid += 100000

        return bard_answer
    
