from typing import List, Optional, Union, Dict, Tuple

from bardapi.models.user_content import UserContent


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
    def text(self) -> str:
        return self._input_list[5][0] if self._input_list[5] else ""

    def __str__(self) -> str:
        return self.title


class BardYoutubeContent(UserContent):
    """http://googleusercontent.com/youtube_content/"""

    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def key(self) -> str:
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
        return (
            [BardYoutubeVideo(video) for video in self._input_list[4][0]]
            if self._input_list[4]
            else []
        )

    def __str__(self) -> str:
        return self.search_query

    @property
    def markdown_text(self) -> str:
        videos = [
            f"1. [{video.title}]({video.url}) by {video.author}\n\n   - {video.text}"
            if video.text
            else f"1. [{video.title}]({video.url}) by {video.author}"
            for video in self.videos
        ]

        return (
            f"#### {self.search_query}\n\n"
            + "\n".join(videos)
            + f"\n\n _View related videos on_ [YouTube]({self.search_url})"
        )
