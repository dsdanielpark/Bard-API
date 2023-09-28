class BardGDocsContent:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def id(self) -> str:
        return self._input_list[3][0]

    @property
    def title(self) -> str:
        return self._input_list[2]

    @property
    def url(self) -> str:
        return self._input_list[1]

    @property
    def author(self) -> str:
        return self._input_list[5]

    @property
    def date(self) -> str:
        return self._input_list[4]

    def __str__(self) -> str:
        return self.title
