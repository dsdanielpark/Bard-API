from bardapi.models.user_content import UserContent
from typing import List


class BardHotel:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def name(self) -> str:
        return self._input_list[0]

    @property
    def images(self) -> List[str]:
        return self._input_list[1]

    @property
    def stars(self) -> int:
        return self._input_list[2]

    @property
    def rating_count(self) -> int:
        return self._input_list[3]

    @property
    def stars_text(self) -> int:
        return self._input_list[4]

    @property
    def description(self) -> int:
        return self._input_list[5]

    @property
    def url(self) -> int:
        return self._input_list[7]

    @property
    def price(self) -> int:
        return self._input_list[8]

    def __str__(self):
        return f"{self.name} {self.stars}★({self.rating_count})\n{self.description} {self.price}"

    def markdown_text(self):
        return (
            f"**{self.name}** {self.stars}★({self.rating_count}) - {self.price}\n   - ![]({self.images[0]})"
            f"\n   - {self.description}"
        )


class BardHotelContent(UserContent):
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def hotels(self) -> List[BardHotel]:
        return (
            [BardHotel(h) for h in self._input_list[0]] if self._input_list[0] else []
        )

    @property
    def key(self) -> str:
        return self._input_list[2][0]

    @property
    def full_title(self) -> str:
        return self._input_list[2][2]

    @property
    def tool_name(self):
        return self._input_list[2][6][1]

    @property
    def title(self) -> str:
        return self._input_list[3]

    @property
    def from_date(self) -> str:
        return self._input_list[4]

    @property
    def to_date(self) -> str:
        return self._input_list[5]

    @property
    def who(self) -> str:
        return self._input_list[8]

    def __str__(self):
        return self.full_title

    @property
    def markdown_text(self) -> str:
        return f"#### {self.full_title}\n\n" + "\n".join(
            ["1. " + flight.markdown_text() for flight in self.hotels]
        )
