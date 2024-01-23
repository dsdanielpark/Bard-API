Development Status :: 5 - Production/Stable

# FAQ
Cookie values may only be valid for a limited time (approximately 15-20 minutes and may be subject to rate limiting even sooner). Again, it's challenging to implement this in official services. Also, this is not an official Google package, and its availability for future use is uncertain.

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



<br><br>

***

### Q: Why is the package structure so messy and unorganized like this?

### A: While rapidly adapting to Google's interface changes, various unexpected features were added, causing the structure to become messy. This package is not intended for providing stable services, and it may become unusable at any time based on Google's decisions, so it hasn't been heavily optimized. It would be advisable to use it temporarily for testing purposes only.

[#263](https://github.com/dsdanielpark/Bard-API/discussions/267)

Originally, Bard had very simple functionality as it was meant for experimental purposes. It used to fetch only a single response through a single cookie even in the 'get_answer' function. However, various additional features were added to Bard over time, such as uploading images, fetching image links, or executing code, among others. The Bard API package was developed quickly in Python to implement these features and perform lightweight testing.

In other words, the package initially lacked these diverse functionalities, and as unexpected features were added, the focus was solely on getting the functionality to work. This resulted in a messy package structure and less-than-clean code.

Additionally, implementing asynchronous functionality did not provide significant benefits, but it was added upon the requests of some developers to quickly implement the features. It was discovered that some users needed more than one cookie, so the goal was to implement these functionalities within the existing structure in the shortest possible time.

Overall, it was difficult to predict the interface or structure, and this package was created primarily for temporary and lightweight prototyping, as it was not meant for providing a stable service.

Therefore, it is very messy and not optimized, and this continues to be a major concern. The package's functionality may stop working at any time due to changes in Google's interface decisions.

Furthermore, adapting to new features or removing them is not straightforward. I feel a great responsibility for providing developers with unoptimized code that has caused inefficiencies, but developing a new package to address this issue has been challenging given the uncertainty of when the functionality might come to an end.

Nevertheless, I am making efforts to revise the package structure whenever possible. Your understanding is appreciated.

***

### #01. Response Error
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

***

### #02. Response Status is 429

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

***

### #03. Exception: SNlM0e value not found. Double-check __Secure-1PSID value or pass it as token='xxxxx'. #155, #99
- https://github.com/dsdanielpark/Bard-API/issues/155
- https://github.com/dsdanielpark/Bard-API/issues/99

***

### #04. Response Error: b')]}\\'\\n\\n38\\n[[\"wrb.fr\",null,null,null,null,[8]]]\\n54\\n[[\"di\",59],[\"af.httprm\",59,\"4239016509367430469\",0]]\\n25\\n[[\"e\",4,null,null,129]]\\n'. \nTemporarily unavailable due to traffic or an error in cookie values. Please double-check the cookie values and verify your network environment. #128
- https://github.com/dsdanielpark/Bard-API/issues/128

***

### #05. Using Proxy
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

***

### #06. How to output results sequentially without delay like ChatGPT?

- Short answer: Bard is currently not supported.

OpenAI provides immediate asynchronous returns of some generated text results (tokens) at the inference stage of the model. However, Bard does not yet support this feature. Bard returns the results to the user once the model has completed generating all text (tokens). There may be various reasons for this, but ultimately, the speed difference between the two is dependent on resources and may be challenging for users to address. In conclusion, consider exploring other ways to reduce perceived delays for users.

Note that for Hugging Face's Open LLM models, you can implement this using TextStreamer as follows.


```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

model_name = "meta-llama/Llama-2-70b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

output = model.generate(**inputs, streamer=streamer, use_cache=True)
```

Furthermore, since this package is an unofficial Python package that intercepts values returned by the web UI of Google Bard's official website, there is nothing more we can support at this package level.

***

### #07. The conversation keeps starting anew. Can this be resolved?

- Short answer: It seems unlikely. It might be possible, but it requires experimentation. If you find a solution, anyone can contribute through a pull request.
You can attempt to fix the session by referring to the contents of a reusable session or try to lock the returned values with a context ID. However, fundamentally, users need an option to fix the seed value, as seen in OpenAI's ChatGPT, to address this issue. Currently, Bard offers limited options to users, even temperature and basic settings, so it may take some time. To make the conversation memorable, you can 1) code to summarize and store the conversation in a database, ensuring the queue changes approximately every 3-5 turns, and 2) transmit the summarized conversation and response to Bard along with a new question. Other models like ChatGPT also remember conversations through similar methods (with more diverse solutions).

In conclusion, users cannot adjust the seed option in model inference, and some additional coding work is needed to remember the conversation. However, using a reusable session allowed retrieving previous responses, showing some effectiveness. To maintain full context like GPT, a large database and resources would be needed, and even models like OpenAI's GPT or Meta's LLaMA-2 struggle to consistently answer. (Refer to LLaMA-2's ghost attention and some appendix examples; it's important to know that making a model operate as a single persona is difficult and costly. Thus, we should remember that general models like Bard or GPT can't be expected to function like specific counselors.)

If anyone has made progress on this, they are welcome to contribute.

Thank you. We always welcome your contributions.
