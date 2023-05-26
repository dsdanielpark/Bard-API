import os
from bardapi.core import Bard
from bardapi.chat import ChatBard
from bardapi.constants import (
    SESSION_HEADERS,
    ALLOWED_LANGUAGES,
    DEFAULT_LANGUAGE,
    SEPARATOR_LINE,
    USER_PROMPT,
)

bard_api_key = os.environ.get("_BARD_API_KEY")

__all__ = [
    "Bard",
    "ChatBard",
    "bard_api_key",
    "SESSION_HEADERS",
    "ALLOWED_LANGUAGES",
    "DEFAULT_LANGUAGE",
    "SEPARATOR_LINE",
    "USER_PROMPT",
]
__version__ = "0.1.14"
__author__ = "daniel park <parkminwoo1991@gmail.com>"
