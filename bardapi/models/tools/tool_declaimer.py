from bardapi.models.user_content import UserContent


class BardToolDeclaimer(UserContent):
    """http://googleusercontent.com/tool_disclaimer_content/"""

    def __init__(self, input_list: list):
        self._input_list = input_list
        self.text = self._input_list[1]

    @property
    def key(self) -> str:
        return self._input_list[0][0]

    @property
    def markdown_text(self) -> str:
        return "\n".join(["> " + line for line in self.text.split("\n")])

    def __str__(self) -> str:
        return self.text[:20]
