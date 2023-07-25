# Util Functions for Async and Sync Core Cookie Modes
import requests
import browser_cookie3
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


def upload_image(image: bytes, filename="Photo.jpg"):
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


def extract_bard_cookie():
    """
    Extract token cookie from browser.
    Supports all modern web browsers and OS


    Returns:
        str: __Secure-1PSID cookie value
    """

    # browser_cookie3.load is similar function but it's broken
    # So here we manually search accross all browsers
    browsers = [
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
    for browser_fn in browsers:
        # if browser isn't installed browser_cookie3 raises exception
        # hence we need to ignore it and try to find the right one
        try:
            cj = browser_fn(domain_name=".google.com")
            for cookie in cj:
                if cookie.name == "__Secure-1PSID" and cookie.value.endswith("."):
                    return cookie.value
        except:
            continue


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
    word_start = 0
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
