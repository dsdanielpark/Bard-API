from typing import Optional


class BardImage:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def original(self) -> dict:
        v = self._input_list[0]
        return {"urls": v[0], "width": v[2], "height": v[3], "alt": v[4]}

    @property
    def source(self) -> dict:
        v = self._input_list[1]
        return {"pages": v[0], "domain": v[1], "fav_icon": v[3]}

    @property
    def key(self) -> str:
        """ use this to replace the image in the markdown, several images can have the same key """
        return self._input_list[2]

    @property
    def thumbnail(self) -> dict:
        v = self._input_list[3]
        return {"urls": v[0], "width": v[2], "height": v[3]}

    @property
    def markdown(self) -> list:
        return self._input_list[7]

    @property
    def alt(self) -> str:
        return self.markdown[2]

    def __str__(self) -> str:
        return f"[{self.alt}]({self.original['urls'][0]})"


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


class BardMapContent:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def id(self) -> str:
        # map_content/0
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

    def __str__(self) -> str:
        return self.title


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


class BardYoutubeVideo:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def id(self) -> str:
        return self._input_list[1]

    @property
    def title(self) -> str:
        return self._input_list[0]

    @property
    def url(self) -> str:
        return self._input_list[2]

    @property
    def author(self) -> str:
        return self._input_list[3]

    @property
    def channel_logo(self) -> str:
        return self._input_list[4]

    @property
    def text(self) -> Optional[list[str]]:
        return self._input_list[5]

    def __str__(self) -> str:
        return self.title


class BardYoutubeContent:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def key(self) -> str:
        # http://googleusercontent.com/youtube_content/5
        return self._input_list[0][0]

    @property
    def search_query(self) -> str:
        return self._input_list[0][2]

    @property
    def search_url(self) -> str:
        return self._input_list[7]

    def __getitem__(self, item):
        return self.videos[item]

    def __len__(self):
        return len(self._input_list[4][0])

    @property
    def videos(self) -> list[BardYoutubeVideo]:
        return [BardYoutubeVideo(video) for video in self._input_list[4][0]] if self._input_list[4] else []

    def __str__(self) -> str:
        return self.search_query


class BardLink:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def key(self) -> str:
        return self._input_list[0][0]

    @property
    def url(self) -> str:
        return self._input_list[1]

    def __str__(self) -> str:
        return self.url


class BardToolDeclaimer:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def id(self) -> str:
        # 'http://googleusercontent.com/tool_disclaimer_content/1'
        return self._input_list[0][0]

    @property
    def markdown_text(self) -> str:
        return self._input_list[1]

    def __str__(self) -> str:
        return self.markdown_text


class BardFlight:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def url(self) -> str:
        return self._input_list[2]

    @property
    def price(self) -> str:
        return self._input_list[3]

    @property
    def airlines(self) -> list[str]:
        return self._input_list[0][0]

    @property
    def airline_logo(self) -> str:
        return self._input_list[0][1]

    @property
    def from_airport(self) -> str:
        return self._input_list[0][2]

    @property
    def to_airport(self) -> str:
        return self._input_list[0][3]

    @property
    def from_time(self) -> str:
        return self._input_list[0][7]

    @property
    def to_time(self) -> str:
        return self._input_list[0][8]

    @property
    def duration(self) -> str:
        return self._input_list[0][9]

    @property
    def stops(self) -> str:
        return self._input_list[0][6]

    def __str__(self) -> str:
        return f'{",".join(self.airlines)} - {self.from_airport} to {self.to_airport} - {self.from_time} to {self.to_time} - {self.price}'


class BardFlightContent:
    """http://googleusercontent.com/flight_content/0"""
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def id(self) -> str:
        return self._input_list[3][0]

    @property
    def title(self) -> str:
        return self._input_list[3][2]

    @property
    def search_url(self) -> str:
        return self._input_list[2]

    @property
    def flights(self) -> list[BardFlight]:
        return [BardFlight(flight) for flight in self._input_list[1]] if self._input_list[1] else []

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

    def __str__(self) -> str:
        return self.title


class BardChoice:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def id(self) -> str:
        return self._input_list[0]

    @property
    def text(self) -> str:
        return self._input_list[1][0]

    @property
    def images(self) -> list:
        # also in self._attachments[1]
        return [BardImage(img) for img in self._input_list[4]] if self._input_list[4] else []

    @property
    def language(self) -> str:
        # en
        return self._input_list[9]

    @property
    def _attachments(self) -> list:
        return self._input_list[12]

    @property
    def map_points(self) -> list[BardMapContent]:
        return [BardMapContent(a) for a in self._attachments[3]] if self._attachments[3] else []

    @property
    def gdocs(self) -> list[BardGDocsContent]:
        return [BardGDocsContent(a) for a in self._attachments[12][0][2]] if self._attachments[12] else []

    @property
    def youtube(self) -> list[BardYoutubeContent]:
        return [BardYoutubeContent(a) for a in self._attachments[4]] if self._attachments[4] else []

    @property
    def links(self) -> list[BardLink]:
        return [BardLink(a) for a in self._attachments[8]] if self._attachments[8] else []

    @property
    def tool_disclaimers(self) -> list[BardToolDeclaimer]:
        return [BardToolDeclaimer(a) for a in self._attachments[22]] if self._attachments[22] else []

    @property
    def flights(self) -> list[BardFlightContent]:
        return [BardFlightContent(a) for a in self._attachments[16]] if self._attachments[16] else []

    def __str__(self) -> str:
        return self.text
