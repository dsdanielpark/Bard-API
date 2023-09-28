from typing import Optional


class BardImage:
    def __init__(self, input_list: list):
        self._input_list = input_list
        self.urls = input_list[0]
        self.width = input_list[2]
        self.height = input_list[3]
        self.alt: Optional[str] = input_list[4] if len(input_list) > 4 else None

    def __str__(self) -> str:
        return f"{self.urls[0]} ({self.width}x{self.height})"


class BardImageContent:
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def original(self) -> BardImage:
        return BardImage(self._input_list[0])

    @property
    def source(self) -> dict:
        v = self._input_list[1]
        return {"pages": v[0], "domain": v[1], "fav_icon": v[3]}

    @property
    def key(self) -> str:
        """use this to replace the image in the markdown, several images can have the same key"""
        return self._input_list[2]

    @property
    def thumbnail(self) -> BardImage:
        return BardImage(self._input_list[3])

    @property
    def markdown(self) -> list:
        return self._input_list[7]

    @property
    def alt(self) -> str:
        return self.markdown[2]

    def __str__(self) -> str:
        return f"[{self.alt}]({self.original.urls[0]})"
