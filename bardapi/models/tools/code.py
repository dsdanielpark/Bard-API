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
    def output_image(self) -> str:
        # Don't know how to extract this, but it's
        # [['[image-tag: code_execution_image_1_1695640907.0254648.png]']]
        return self._input_list[27]

    @property
    def code(self) -> str:
        return self._input_list[8]

    def __str__(self) -> str:
        return self.code
