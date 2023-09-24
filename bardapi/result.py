from typing import Optional

from bardapi.choice import BardChoice


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


class BardUserLocation:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def location_str(self) -> str:
        return self._input_list[0]

    @property
    def description(self) -> str:
        return self._input_list[1]

    @property
    def geo_position(self) -> list:
        return self._input_list[3][0][0][3]

    @property
    def image_url(self) -> str:
        return "https:" + self._input_list[4]

    def __str__(self) -> str:
        return self.location_str


class BardResult:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def conversation_id(self) -> str:
        return self._input_list[1][0]

    @property
    def response_id(self) -> str:
        return self._input_list[1][1]

    @property
    def search_query(self) -> list[str, int]:
        return self._input_list[2]

    @property
    def factuality_queries(self) -> Optional[list]:
        return self._input_list[3]

    @property
    def choices(self) -> list[BardChoice]:
        return [BardChoice(c) for c in self._input_list[4]] if self._input_list[4] else []

    @property
    def location(self) -> BardUserLocation:
        return BardUserLocation(self._input_list[5])

    @property
    def progress_tool(self) -> BardTool:
        return BardTool(self._input_list[6]) if self._input_list[6] else None

    @property
    def country(self) -> str:
        return self._input_list[8]

    @property
    def topic(self) -> Optional[str]:
        if len(self._input_list) < 11 or not self._input_list[10]:
            return None
        return self._input_list[10][0]

    @property
    def tools_applied(self) -> list[BardTool]:
        if len(self._input_list) < 12:
            return []
        return [BardTool(tool) for tool in self._input_list[11]] if self._input_list[11] else []
