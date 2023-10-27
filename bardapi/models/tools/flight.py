from bardapi.models.user_content import UserContent
from typing import List


class BardFlight:
    def __init__(self, input_list: List):
        self._input_list = input_list

    @property
    def url(self) -> str:
        if len(self._input_list) > 2:
            return self._input_list[2]
        else:
            return ""

    @property
    def price(self) -> str:
        if len(self._input_list) > 3:
            return self._input_list[3]
        else:
            return ""

    @property
    def airlines(self) -> List[str]:
        if len(self._input_list) > 0 and isinstance(self._input_list[0], list):
            return self._input_list[0]
        else:
            return []

    @property
    def airline_logo(self) -> str:
        return self._input_list[0][1]

    @property
    def departure_airport(self) -> str:
        return self._input_list[0][2]

    @property
    def arrival_airport(self) -> str:
        return self._input_list[0][3]

    @property
    def departure_time(self) -> str:
        return self._input_list[0][7]

    @property
    def arrival_time(self) -> str:
        return self._input_list[0][8]

    @property
    def duration(self) -> str:
        return self._input_list[0][9]

    @property
    def stops(self) -> str:
        return self._input_list[0][6]

    def __str__(self) -> str:
        return f'{",".join(self.airlines)} - {self.departure_airport} to {self.arrival_airport} - {self.departure_time} to {self.arrival_time} - {self.price}'


class BardFlightContent(UserContent):
    """http://googleusercontent.com/flight_content/"""

    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def key(self) -> str:
        return self._input_list[3][0]

    @property
    def title(self) -> str:
        return self._input_list[3][2]

    @property
    def search_url(self) -> str:
        return self._input_list[2]

    @property
    def flights(self) -> List[BardFlight]:
        return (
            [BardFlight(flight) for flight in self._input_list[1]]
            if self._input_list[1]
            else []
        )

    @property
    def from_airport(self) -> str:
        # 'OSL'
        return self._input_list[4]

    @property
    def to_airport(self) -> str:
        # 'MAD'
        return self._input_list[5]

    @property
    def from_date(self) -> str:
        # Jan 22
        return self._input_list[6]

    @property
    def to_date(self) -> str:
        # Jan 28
        return self._input_list[7]

    @property
    def who(self) -> str:
        # '1 adult'
        return self._input_list[8]

    def __getitem__(self, item) -> BardFlight:
        return self.flights[item]

    def __len__(self):
        return len(self.flights)

    def __str__(self) -> str:
        return self.title

    @property
    def markdown_text(self) -> str:
        return f"#### {self.title}\n\n" + "\n".join(
            [" * " + str(flight) for flight in self.flights]
        )
