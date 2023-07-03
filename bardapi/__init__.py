# Copyright 2023 parkminwoo, MIT License

import os
from bardapi.core import Bard
from bardapi.constants import (
    SESSION_HEADERS,
    ALLOWED_LANGUAGES,
    DEFAULT_LANGUAGE,
    SEPARATOR_LINE,
    USER_PROMPT,
)
from bardapi.core_async import BardAsync

bard_api_key = os.environ.get("_BARD_API_KEY")

__all__ = [
    "Bard",
    "BardAsync",
    "bard_api_key",
    "SESSION_HEADERS",
    "ALLOWED_LANGUAGES",
    "DEFAULT_LANGUAGE",
    "SEPARATOR_LINE",
    "USER_PROMPT",
]
__version__ = "0.1.23a"
__author__ = "daniel park <parkminwoo1991@gmail.com>"
