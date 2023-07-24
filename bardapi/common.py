# Common function in async and sync core, core cookie modes
import requests
import browser_cookie3

IMG_UPLOAD_HEADERS = {
    "authority": "content-push.googleapis.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.7",
    "authorization": "Basic c2F2ZXM6cyNMdGhlNmxzd2F2b0RsN3J1d1U=",  # constant authorization key
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "origin": "https://bard.google.com",
    "push-id": "feeds/mcudyrk2a4khkz",  # constant
    "referer": "https://bard.google.com/",
    "x-goog-upload-command": "start",
    "x-goog-upload-header-content-length": "",
    "x-goog-upload-protocol": "resumable",
    "x-tenant-id": "bard-storage",
}


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
