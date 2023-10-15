import json

from bardapi.models.user_content import UserContent


class JsonContent(UserContent):
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def object(self) -> str:
        return json.loads(self.json_text)

    @property
    def json_text(self) -> str:
        return self._input_list[1]

    @property
    def key(self) -> str:
        return self._input_list[0]

    @property
    def markdown_text(self) -> str:
        return "{json}"

    def __str__(self) -> str:
        return self.json_text[:20]
