from typing import Optional

from bardapi.models.user_content import UserContent


class BardMapsPoint:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def id(self) -> str:
        return self._input_list[1]

    @property
    def address(self) -> str:
        # '12170 Dornans Rd, Moose, WY 83012, USA'
        return self._input_list[8]

    @property
    def address_short(self) -> str:
        # 'Dornans, 12170 Dornans Rd, Moose'
        return self._input_list[50]

    @property
    def geo_position(self) -> list:
        return self._input_list[11]

    @property
    def geo_position_rect(self) -> list:
        return self._input_list[12]

    @property
    def rating(self) -> float:
        return self._input_list[13]

    @property
    def rating_count(self) -> int:
        return self._input_list[27]

    @property
    def gmaps_url(self) -> str:
        return self._input_list[14]

    @property
    def website_url(self) -> str:
        return self._input_list[15]

    @property
    def schedule(self) -> dict:
        v = self._input_list[20]
        return {
            "open": v[0],
            "value": v[1],
            "human": v[2],
        }

    @property
    def title(self) -> tuple[str, str]:
        # Albertsons, "en"
        return self._input_list[30]  # same [30], "en"

    def description(self) -> Optional[tuple[str, str]]:
        # ['Gourmet groceries, cheeses & baked goods are available at this casual deli in a resort setting.', 'en']
        return self._input_list[51]

    @property
    def kind(self) -> str:
        # supermarket
        return self._input_list[49]  # same [31], "en"

    @property
    def images(self) -> list:
        return [{"url": img[0], "author": img[3]} for img in self._input_list[53]] if self._input_list[53] else []

    def __str__(self) -> str:
        return f'{self.title[0]}, {self.rating}*({self.rating_count}) - {self.kind}'


class BardMapContent(UserContent):
    """http://googleusercontent.com/map_content/0"""

    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def key(self) -> str:
        return self._input_list[2][0]

    @property
    def title(self) -> str:
        # Places
        return self._input_list[2][2]

    @property
    def tool_human_name(self) -> str:
        # Google Maps
        return self._input_list[2][6][0]

    @property
    def points(self) -> list[BardMapsPoint]:
        return [BardMapsPoint(point) for point in self._input_list[0][1]] if self._input_list[0][1] else []

    def __getitem__(self, item) -> BardMapsPoint:
        return self.points[item]

    def __len__(self):
        return len(self.points)

    def __str__(self) -> str:
        return self.title

    def markdown_text(self) -> str:
        return f'# {self.title}\n\n' + '\n\n'.join([f'## {p.title[0]}\n\n{p.description()[0]}' for p in self.points])