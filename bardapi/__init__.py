# Copyright 2023 Daniel Park, MIT License

from os import environ
from bardapi.core import Bard
from bardapi.chat import ChatBard
from bardapi.core_async import BardAsync
from bardapi.core_cookies import BardCookies, BardAsyncCookies
from bardapi.constants import (
    SESSION_HEADERS,
    ALLOWED_LANGUAGES,
    DEFAULT_LANGUAGE,
    SEPARATOR_LINE,
    USER_PROMPT,
    IMG_UPLOAD_HEADERS,
    Tool,
)
from bardapi.utils import (
    extract_links,
    upload_image,
    extract_bard_cookie,
    max_token,
    max_sentence,
)

# Get the API key from the environment variable
bard_api_key = environ.get("_BARD_API_KEY")

__all__ = [
    "Bard",
    "ChatBard",
    "BardAsync",
    "BardCookies",
    "BardAsyncCookies",
    "SESSION_HEADERS",
    "ALLOWED_LANGUAGES",
    "DEFAULT_LANGUAGE",
    "IMG_UPLOAD_HEADERS",
    "SEPARATOR_LINE",
    "USER_PROMPT",
    "extract_links",
    "upload_image",
    "extract_bard_cookie",
    "max_token",
    "max_sentence",
    "Tool",
]
__version__ = "0.1.39"
__author__ = "daniel park <parkminwoo1991@gmail.com>"
