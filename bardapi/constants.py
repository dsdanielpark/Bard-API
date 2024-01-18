from enum import Enum

from colorama import Fore

# https://support.google.com/bard/answer/13575153?hl=en
ALLOWED_LANGUAGES = {
    "korean",
    "english",
    "japanese",
    "arabic",
    "bengali",
    "bulgarian",
    "chinese (simplified)",
    "chinese (traditional)",
    "croatian",
    "czech",
    "danish",
    "dutch",
    "english",
    "estonian",
    "farsi",
    "finnish",
    "french",
    "german",
    "greek",
    "gujarati",
    "hebrew",
    "hindi",
    "hungarian",
    "indonesian",
    "italian",
    "japanese",
    "kannada",
    "korean",
    "latvian",
    "lithuanian",
    "malayalam",
    "marathi",
    "norwegian",
    "polish",
    "portuguese",
    "romanian",
    "russian",
    "serbian",
    "slovak",
    "slovenian",
    "spanish",
    "swahili",
    "swedish",
    "tamil",
    "telugu",
    "thai",
    "turkish",
    "ukrainian",
    "urdu",
    "vietnamese",
    "ko",
    "en",
    "ja",
    "ar",
    "bn",
    "bg",
    "zh-cn",
    "zh-tw",
    "hr",
    "cs",
    "da",
    "nl",
    "en",
    "et",
    "fa",
    "fi",
    "fr",
    "de",
    "el",
    "gu",
    "he",
    "hi",
    "hu",
    "id",
    "it",
    "kn",
    "lv",
    "lt",
    "ml",
    "mr",
    "no",
    "pl",
    "pt",
    "ro",
    "ru",
    "sr",
    "sk",
    "sl",
    "es",
    "sw",
    "sv",
    "ta",
    "te",
    "th",
    "tr",
    "uk",
    "ur",
    "vi",
}

DEFAULT_LANGUAGE = "en"
SEPARATOR_LINE = "=" * 36
USER_PROMPT = Fore.BLUE + "You: " + Fore.RESET
TEXT_GENERATION_WEB_SERVER_PARAM = "boq_assistant-bard-web-server_20230912.07_p1"
POST_ENDPOINT = "https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate"


SESSION_HEADERS = {
    "Host": "bard.google.com",
    "X-Same-Domain": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://bard.google.com",
    "Referer": "https://bard.google.com/",
}

IMG_UPLOAD_HEADERS = {
    "authority": "content-push.googleapis.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.7",
    "authorization": "Basic c2F2ZXM6cyNMdGhlNmxzd2F2b0RsN3J1d1U=",  # Constant Authorization Key
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "origin": "https://bard.google.com",
    "push-id": "feeds/mcudyrk2a4khkz",  # Constant
    "referer": "https://bard.google.com/",
    "x-goog-upload-command": "start",
    "x-goog-upload-header-content-length": "",
    "x-goog-upload-protocol": "resumable",
    "x-tenant-id": "bard-storage",
}

REPLIT_SUPPORT_PROGRAM_LANGUAGES = {
    "python": "main.py",
    "javascript": "index.js",
    "go": "main.go",
    "java": "Main.java",
    "kotlin": "Main.kt",
    "php": "index.php",
    "c#": "main.cs",
    "swift": "main.swift",
    "r": "main.r",
    "ruby": "main.rb",
    "c": "main.c",
    "c++": "main.cpp",
    "matlab": "main.m",
    "typescript": "main.ts",
    "scala": "main.scala",
    "sql": "main.sql",
    "html": "index.html",
    "css": "style.css",
    "nosql": "main.nosql",
    "rust": "main.rs",
    "perl": "main.pl",
}


class Tool(Enum):
    GMAIL = ["workspace_tool", "Gmail"]
    GOOGLE_DOCS = ["workspace_tool", "Google Docs"]
    GOOGLE_DRIVE = ["workspace_tool", "Google Drive"]
    GOOGLE_FLIGHTS = ["google_flights_tool"]
    GOOGLE_HOTELS = ["google_hotels_tool"]
    GOOGLE_MAPS = ["google_map_tool"]
    YOUTUBE = ["youtube_tool"]
