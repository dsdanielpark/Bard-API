import os

from bardapi.constants import ALLOWED_LANGUAGES, DEFAULT_LANGUAGE, SEPARATOR_LINE, SESSION_HEADERS, USER_PROMPT
from bardapi.core import Bard


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
__version__ = "0.1.11"
__author__ = "daniel park <parkminwoo1991@gmail.com>"
