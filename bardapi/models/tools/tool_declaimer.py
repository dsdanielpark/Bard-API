from bardapi.models.user_content import UserContent


class BardToolDeclaimer(UserContent):
    """http://googleusercontent.com/tool_disclaimer_content/1"""

    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def key(self) -> str:
        return self._input_list[0][0]

    @property
    def markdown_text(self) -> str:
        return self._input_list[1]

    def __str__(self) -> str:
        return self.markdown_text
