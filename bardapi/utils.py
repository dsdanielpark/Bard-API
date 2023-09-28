# Util Functions for Async and Sync Core Cookie Modes
import json
from typing import Optional

import requests
from bardapi.constants import IMG_UPLOAD_HEADERS


def extract_links(data: list) -> list:
    """
    Extract links from the given data.

    Args:
        data: Data to extract links from.

    Returns:
        list: Extracted links.
    """
    links = []
    if isinstance(data, list):
        for item in data:
            if isinstance(item, list):
                # recursive
                links.extend(extract_links(item))
            elif (
                isinstance(item, str)
                and item.startswith("http")
                and "favicon" not in item
            ):
                links.append(item)
    return links


def upload_image(image: bytes, filename: str = "Photo.jpg"):
    """
    Upload image into bard bucket on Google API, do not need session.

    Returns:
        str: relative URL of image.
    """
    resp = requests.options("https://content-push.googleapis.com/upload/")
    resp.raise_for_status()
    size = len(image)

    headers = IMG_UPLOAD_HEADERS
    headers["size"] = str(size)
    headers["x-goog-upload-command"] = "start"

    data = f"File name: {filename}"
    resp = requests.post(
        "https://content-push.googleapis.com/upload/", headers=headers, data=data
    )
    resp.raise_for_status()
    upload_url = resp.headers["X-Goog-Upload-Url"]
    resp = requests.options(upload_url, headers=headers)
    resp.raise_for_status()
    headers["x-goog-upload-command"] = "upload, finalize"

    # It can be that we need to check returned offset
    headers["X-Goog-Upload-Offset"] = "0"
    resp = requests.post(upload_url, headers=headers, data=image)
    resp.raise_for_status()
    return resp.text


def extract_bard_cookie(cookies: bool = False) -> dict:
    """
    Extracts the specified Bard cookie(s) from the browser's cookies.

    This function searches for the specified Bard cookies in various web browsers
    installed on the system. It supports modern web browsers and operating systems.

    Args:
        cookies (bool, optional): If False, extracts only '__Secure-1PSID' cookie.
            If True, extracts '__Secure-1PSID', '__Secure-1PSIDTS', and '__Secure-1PSIDCC' cookies.
            Defaults to False.

    Returns:
        dict: A dictionary containing the extracted Bard cookies.

    Raises:
        Exception: If no supported browser is found or if there's an issue with cookie extraction.
    """
    import browser_cookie3

    supported_browsers = [
        browser_cookie3.chrome,
        browser_cookie3.chromium,
        browser_cookie3.opera,
        browser_cookie3.opera_gx,
        browser_cookie3.brave,
        browser_cookie3.edge,
        browser_cookie3.vivaldi,
        browser_cookie3.firefox,
        browser_cookie3.librewolf,
        browser_cookie3.safari,
    ]

    cookie_dict = {}

    for browser_fn in supported_browsers:
        try:
            cj = browser_fn(domain_name=".google.com")

            for cookie in cj:
                print(cookie.name)
                if cookie.name == "__Secure-1PSID" and cookie.value.endswith("."):
                    cookie_dict["__Secure-1PSID"] = cookie.value
                if cookies:
                    if cookie.name == "__Secure-1PSIDTS":
                        print(cookie.value)
                        cookie_dict["__Secure-1PSIDTS"] = cookie.value
                    elif cookie.name == "__Secure-1PSIDCC":
                        print(cookie.value)
                        cookie_dict["__Secure-1PSIDCC"] = cookie.value
                if len(cookie_dict) == 3:
                    return cookie_dict
        except Exception as e:
            # Ignore exceptions and try the next browser function
            continue

    if not cookie_dict:
        raise Exception("No supported browser found or issue with cookie extraction")

    print(cookie_dict)
    return cookie_dict


def max_token(text: str, n: int):
    """
    Print the first 'n' tokens (words) of the given text.

    Args:
        text (str): The input text to be processed.
        n (int): The number of tokens (words) to be printed from the beginning.

    Returns:
        None
    """
    word_count = 0
    for i, char in enumerate(text):
        if char.isspace():
            word_count += 1
            if word_count == n:
                print(text[:i])
                break
    else:
        print(text)


def max_sentence(text: str, n: int):
    """
    Print the first 'n' sentences of the given text.

    Args:
        text (str): The input text to be processed.
        n (int): The number of sentences to be printed from the beginning.

    Returns:
        None
    """
    punctuations = set("?!.")

    sentences = []
    sentence_count = 0
    for char in text:
        sentences.append(char)
        if char in punctuations:
            sentence_count += 1
            if sentence_count == n:
                print("".join(sentences).strip())
                return
    print("".join(sentences).strip())


def build_input_text_struct(
    input_text: str,
    conversation_id: Optional[str],
    response_id: Optional[str],
    choice_id: Optional[str],
    image_url: str = None,
    image_name: str = None,
    tools: list[list[str]] = None,
) -> list:
    image_arr = []
    if image_url is not None:
        image_arr = [[[image_url, 1], image_name]]

    if tools is None:
        tools = []

    return [
        [input_text, 0, None, image_arr, None, None, 0],
        ["en"],
        [conversation_id, response_id, choice_id, None, None, []],
        None,  # Unknown random string value (1000 characters +) - If needed, can replace with a random string generator
        None,  # Random uuidv4 (32 characters)
        None,
        [1],
        0,
        [],
        tools,
        1,
        0,
    ]


def build_input_replit_data_struct(instructions: str, code: str, filename: str) -> list:
    """
    Creates and returns the input_image_data_struct based on provided parameters.

    :param instructions: The instruction text.
    :param code: The code.
    :param filename: The filename.

    :return: The input_image_data_struct.
    """
    return [
        [
            [
                "qACoKe",
                json.dumps([instructions, 5, code, [[filename, code]]]),
                None,
                "generic",
            ]
        ]
    ]


def build_bard_answer(
    parsed_answer: list,
    images: list[str],
    program_lang: str,
    code: str,
    status_code: int,
) -> dict:
    return {
        "content": parsed_answer[4][0][1][0],
        "conversation_id": parsed_answer[1][0],
        "response_id": parsed_answer[1][1],
        "factuality_queries": parsed_answer[3],
        "text_query": parsed_answer[2][0] if parsed_answer[2] else "",
        "choices": [{"id": x[0], "content": x[1]} for x in parsed_answer[4]],
        "links": extract_links(parsed_answer[4]),
        "images": images,
        "program_lang": program_lang,
        "code": code,
        "status_code": status_code,
    }


def build_export_data_structure(
    conv_id: int, resp_id: int, choice_id: int, title: str
) -> list:
    return [
        [
            [
                "fuVx7",
                json.dumps(
                    [
                        [
                            None,
                            [
                                [
                                    [conv_id, resp_id],
                                    None,
                                    None,
                                    [[], [], [], choice_id, []],
                                ]
                            ],
                            [0, title],
                        ]
                    ]
                ),
                None,
                "generic",
            ]
        ]
    ]
