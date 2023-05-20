import os
from bardapi.core import Bard
from bardapi.tranlsator import translate


bard_api_key = os.environ.get("_BARD_API_KEY")

__all__ = ["Bard", "bard_api_key", "translate"]
__version__ = "0.1.8"
__author__ = "daniel park <parkminwoo1991@gmail.com>"
