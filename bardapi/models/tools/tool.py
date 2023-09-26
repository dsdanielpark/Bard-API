from typing import Optional


class BardTool:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def step(self) -> Optional[str]:
        # Finding your documents
        return self._input_list[0]

    @property
    def name(self) -> str:
        # google_map_tool
        return self._input_list[1][0]

    @property
    def human_name(self) -> str:
        # Google Maps
        return self._input_list[1][1][2]

    @property
    def logo(self) -> str:
        return self._input_list[1][1][3]

    def __str__(self) -> str:
        return f'{self.human_name} - {self.step or ""}'
