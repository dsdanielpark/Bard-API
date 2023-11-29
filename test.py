from bardapi import Bard, SESSION_HEADERS
import requests
session = requests.Session()
token = '-'
session.cookies.set("__Secure-1PSID", token)
session.cookies.set( "__Secure-1PSIDCC", "-")
session.cookies.set("__Secure-1PSIDTS", "-")
session.headers = SESSION_HEADERS
bard = Bard(token=token, session=session, timeout=30)
new_cookies = bard.update_1PSIDTS()
print('New cookies:', new_cookies)
print(new_cookies.get("__Secure-1PSIDTS"))
print(new_cookies.get("__Secure-1PSIDCC"))
print(new_cookies.get("__Secure-3PSIDTS"))
