Development Status :: 5 - Production/Stable

# FAQ

## Before using the Bard API
- Google Bard can return different responses based on various factors such as account, country, region, IP, etc., following Google's policies. This means that even well-functioning methods, especially the `ask_about_image` method, can encounter Response Errors, which are caused by various reasons related to Google's policies, not package errors. It cannot be resolved at the package level. (e.g., [CAPTCHA](https://en.wikipedia.org/wiki/CAPTCHA) or [HTTP 429 error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429))
- The API token(__Secure-1PSID cookie value) for this service is unofficial. Additionally, exposing it can allow others to easily use the Bard service with your Google ID, so never expose it.
- This service has very limited and variable call limits per unit of time, and exceeding rate limiting temporarily prevents obtaining normal response results.
- Sending the same question multiple times in requests can also temporarily prevent obtaining normal response results.
- Some regions may require additional cookie values besides __Secure-1PSID; refer to the issue page.
- The __Secure-1PSID cookie value may change frequently. Logout, restart your web browser, and enter the new __Secure-1PSID cookie value.
- Using this package for real-world applications is highly inappropriate. Due to rate limiting and variable API policies, it will only function temporarily.
- If the time interval between requests is very short, the Google API process may interpret it as performing a large number of requests and may not return normal responses.
- All these policies are subject to change, and the interface is also variable.
- The reason this Bard API's method names do not follow the typical inference format of general LLMs is to prevent confusion with the official API. This Python package merely serves as an unofficial API to fetch responses from Bard's website, so please do not be mistaken.
- The official API format for Bard will likely be as follows.
  <details>
  <summary>Click to view the text generative AI model API code template</summary>
  
  ```python
  bard.configure(api_key='YOUR_API_KEY')
  
  models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
  model = models[0].name
  print(model)
  
  prompt = "Who are you?"
  
  completion = bard.generate_text(
      model=model,
      prompt=prompt,
      temperature=0,
      # The maximum length of the response
      max_output_tokens=800,
  )
  ```
  </details>



<br>

## Troubleshooting Google Account-Related Issues with Bard API

<br>

### 1. Response Error
```python
Response Error: b')]}\\'\\n\\n38\\n[[\"wrb.fr\",null,null,null,null,[8]]]\\n54\\n[[\"di\",59],
[\"af.httprm\",59,\"4239016509367430469\",0]]\\n25\\n[[\"e\",4,null,null,129]]\\n'. 
Temporarily unavailable due to traffic or an error in cookie values. Please double-check the cookie values and verify your network environment.
```

The error you're experiencing isn't originating from the package itself; it's related to your Google account and may be due to various factors like your country or region settings, which can prevent you from receiving accurate results from Bard. Therefore, it's beyond the scope of the package to resolve, but please consider checking the following:

1. First, thoroughly read the readme and see if it pertains to cases of temporary abnormal responses from the package. Try again after some time or a few hours: [Before using Bard API](https://github.com/dsdanielpark/Bard-API/blob/main/README.md#before-using-the-bard-api)
2. Bypass proxies: [Behind a proxy](https://github.com/dsdanielpark/Bard-API#behind-a-proxy)
3. Try using an account from a different region or change the language settings of your Google account.
4. Restart your browser to refresh the cookie values and use the new __Secure-1PSID.
5. Try passing three or more cookies using [Multi-cookie Bard](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#multi-cookie-bard). If that doesn't work, consider passing almost all cookie values.

Please let me know if you need further assistance.

<br>

### 2. Response Status is 429

```
Traceback (most recent call last):
  File "/Users/arielolin/IAPP-server/server.py", line 20, in <module>
    bard = Bard(token=BARD_TOKEN, session=bard_session)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/bardapi/core.py", line 78, in __init__
    self.SNlM0e = self._get_snim0e()
                  ^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/bardapi/core.py", line 149, in _get_snim0e
    raise Exception(
Exception: Response status code is not 200. Response Status is 429
```

Both are not package-related issues and are unsolvable problems. It is recommended to work around them as much as possible. This is a problem at the level of Google's API, and while it would take a long time to develop software to work around it, even assuming that it could be developed, it is not worth developing because it is easily blocked. There are no plans to update it further. There is no package-level solution to prevent captcha or HTTP 429 errors other than efforts such as bypassing readme and proxy, and creating a time interval between requests to avoid rate limiting.
- `CAPTCHA`: a program or system intended to distinguish human from machine input, typically as a way of [thwarting](https://www.google.com/search?sca_esv=573532060&sxsrf=AM9HkKmd5Faz1q0x4sLsgIG3VgVR9V18iA:1697335053753&q=thwarting&si=ALGXSlbSiMNWMsv5Y0U_0sBS8EWzwSlNZdPczeDdDqrhgxYO86hMDzIqBVTJp6ZKxKdXeVsCSihVIJAH_MROqwPM7RtQB0OoEA%3D%3D&expnd=1) spam and automated extraction of data from websites.
- `The HTTP 429`: Too Many Requests response status code indicates the user has sent too many requests in a given amount of time ("rate limiting")

<br>

### 3. Exception: SNlM0e value not found. Double-check __Secure-1PSID value or pass it as token='xxxxx'. #155, #99
- https://github.com/dsdanielpark/Bard-API/issues/155
- https://github.com/dsdanielpark/Bard-API/issues/99

<br>

### 4. Response Error: b')]}\\'\\n\\n38\\n[[\"wrb.fr\",null,null,null,null,[8]]]\\n54\\n[[\"di\",59],[\"af.httprm\",59,\"4239016509367430469\",0]]\\n25\\n[[\"e\",4,null,null,129]]\\n'. \nTemporarily unavailable due to traffic or an error in cookie values. Please double-check the cookie values and verify your network environment. #128
- https://github.com/dsdanielpark/Bard-API/issues/128

<br>

### 5. Using Proxy
If you cannot receive a normal response in your area, try making the request through [Crawlbase](https://crawlbase.com/)'s anonymous [smart proxy service.](https://crawlbase.com/docs/smart-proxy/get/) (Still, be mindful of Google's rate limiting, so adjust the time between requests and avoid requesting duplicate responses.)

```
$ pip install bardapi
```

```python
from bardapi import Bard
import requests

# Get your proxy url at crawlbase https://crawlbase.com/docs/smart-proxy/get/
proxy_url = "http://xxxxxxxxxxxxxx:@smartproxy.crawlbase.com:8012" 
proxies = {"http": proxy_url, "https": proxy_url}

bard = Bard(token='xxxxxxx', proxies=proxies, timeout=30)
bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
```
