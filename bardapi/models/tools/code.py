class CodeContent:
    # 32 items
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def request(self) -> str:
        return self._input_list[3]

    @property
    def output(self) -> str:
        return self._input_list[1]

    @property
    def code(self) -> str:
        return self._input_list[8]

    def __str__(self) -> str:
        return self.code
