Development Status :: 5 - Production/Stable


# Google ~~Bard~~ Gemini API

<p align="left">
<a href="https://github.com/dsdanielpark/Bard-API"><img alt="PyPI package" src="https://img.shields.io/badge/pypi-BardAPI-black"></a>
<a href="https://pepy.tech/project/bardapi"><img alt="Downloads" src="https://pepy.tech/badge/bardapi"></a>
<!-- <a><img alt="commit update" src="https://img.shields.io/github/last-commit/dsdanielpark/Bard-API?color=black"></a> -->
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/dsdanielpark/Bard-API"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdsdanielpark%2FBARD_API&count_bg=%23000000&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=BardAPI&edge_flat=false"/></a>
<a href="https://github.com/dsdanielpark/Bard-API/stargazers"><img src="https://img.shields.io/github/stars/dsdanielpark/Bard-API?style=social"></a>
<a href="https://pypi.org/project/bardapi/"><img alt="PyPI" src="https://img.shields.io/pypi/v/bardapi"></a>
<!-- <a href="https://www.buymeacoffee.com/parkminwoo"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-orange.png" height="20px"></a> -->
  
</p>


> The python package that returns response of [Google ~~Bard~~ Gemini](https://gemini.google.com/) through value of cookie.

![](./assets/bard_api.gif)


**Please exercise caution and use this package responsibly. This python package is _UNOFFICIAL_.**

I referred to this github repository([github.com/acheong08/Bard](https://github.com/acheong08/Bard)) where inference process of Bard was reverse engineered. Using `__Secure-1PSID`, you can ask questions and get answers from Google Bard. Please note that the bardapi is not a free service, but rather a tool provided to assist developers with testing certain functionalities due to the delayed development and release of Google Bard's API. It has been designed with a lightweight structure that can easily adapt to the emergence of an official API. Therefore, I strongly discourage using it for any other purposes. If you have access to reliable official [PaLM-2 API](https://blog.google/technology/ai/google-palm-2-ai-large-language-model/) or [Google Generative AI API](https://github.com/GoogleCloudPlatform/generative-ai), replace the provided response with the corresponding official code. Check out https://github.com/dsdanielpark/Bard-API/issues/262.

<br>

- [Google  ~~Bard~~ Gemini API](#google--bard-api)
  - [What is Google ~~Bard~~ Gemini?](#what-is-google-gemini)
  - [Install](#install)
  - [Authentication](#authentication)
  - [Usage](#usage)
  - [Further](#further)
    - [Behind a proxy](#behind-a-proxy)
    - [Use rotating proxies](#use-rotating-proxies)
    - [Reusable session object](#reusable-session-object)
    - [Auto Cookie Bard](#auto-cookie-bard)
    - [Bard `ask_about_image` method](#bard-ask_about_image-method)
    - [Text To Speech(TTS) from Bard](#text-to-speechtts-from-bard)
  - [More features](#more-features)
  - [Amazing Bard Prompts Is All You Need!](#amazing-bard-prompts-is-all-you-need)
  - [The Python package hf-transllm](#the-python-package-hf-transllm)
  - [What is Google ~~Bard~~ Gemini?](#what-is-google-gemini)
  - [Google PaLM](#google-palm)
  - [FAQ](#faq)




<br>

## Updates 
- `2024.02.09` We are currently proceeding with a hotfix update due to the service name change from bard to Gemini. Please wait a moment.

<br>

## What is Google [Bard](https://gemini.google.com/chat)?
Bard is a conversational generative artificial intelligence chatbot developed by Google, based initially on the LaMDA family of LLMs(Large Language Models) and later the PaLM LLM. Please check official documents for [updates](https://gemini.google.com/updates) on Bard, including [available regions and languages](https://support.google.com/bard/answer/13575153?hl=en).


## Install
```
$ pip install bardapi
```
```
$ pip install git+https://github.com/dsdanielpark/Bard-API.git
```
Due to certain dependency packages that are not compatible with 64bit windows(OS), we are releasing a lightweight alpha release of bard that only returns responses for simple requests. This release is a continuation of the pypi `0.1.18` version, which was maintained with lightweight and simple functionality. See [alpha-release github branch](https://github.com/dsdanielpark/Bard-API/tree/alpha-release) for more details.
```
$ pip install bardapi==0.1.23a
```

<br>

## Authentication
> **Warning** Do not expose the `__Secure-1PSID`. For testing purposes only; avoid direct application use. Cookie values change periodically (every 15-20 minutes). Frequent session changes may briefly block access; headless mode is challenging. Rate limiting applies and changes often. If the cookie changes, log out of your Google account, close the browser, and enter the new cookie value. Or manually reset the cookie for a new value. See FAQ and issue pages for details.
1. Visit https://gemini.google.com/
2. F12 for console
3. Session: Application → Cookies → Copy the value of  `__Secure-1PSID` cookie.

Note that while I referred to `__Secure-1PSID` value as an API key for convenience, it is not an officially provided API key. 
Cookie value subject to frequent changes. Verify the value again if an error occurs. Most errors occur when an invalid cookie value is entered.

<br>

If you need to set multiple cookie values:

- [Multi-cookie Bard](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#multi-cookie-bard) - After confirming that multiple cookie values are required to receive responses reliably in certain countries, I will deploy it for testing purposes. Please debug and create a pull request.


<br>

## Usage 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zzzlTIh0kt2MdjLzvXRby1rWbHzmog8t?usp=sharing) 


Simple Usage

```python
from bardapi import Bard

token = 'xxxxxxx'
bard = Bard(token=token)
bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
```
Or you can use this
```python
from bardapi import Bard
import os
os.environ['_BARD_API_KEY'] = "xxxxxxx"

Bard().get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
```

To get reponse dictionary
```python
import bardapi

# set your __Secure-1PSID value to key
token = 'xxxxxxx'

# set your input text
input_text = "나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘"

# Send an API request and get a response.
response = bardapi.core.Bard(token).get_answer(input_text)
```



Addressing errors caused by delayed responses in environments like Google Colab and containers. If an error occurs despite following the proper procedure, utilize the timeout argument.
```python
from bardapi import Bard
import os
os.environ['_BARD_API_KEY']="xxxxxxx"

bard = Bard(timeout=30) # Set timeout in seconds
bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
```

<br>

## Further
### Behind a proxy
If you are working behind a proxy, use the following.
```python
from bardapi import Bard

# Change 'http://proxy.example.com:8080' to your http proxy
# timeout in seconds
proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
}

bard = Bard(token='xxxxxxx', proxies=proxies, timeout=30)
bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
```

### Use rotating proxies

If you want to **avoid blocked requests** and bans, then use [Smart Proxy by Crawlbase](https://crawlbase.com/docs/smart-proxy/?utm_source=github_ad&utm_medium=social&utm_campaign=bard_api). It forwards your connection requests to a **randomly rotating IP address** in a pool of proxies before reaching the target website. The combination of AI and ML make it more effective to **avoid CAPTCHAs and blocks**.

```python
from bardapi import Bard
import requests

# Get your proxy url at crawlbase https://crawlbase.com/docs/smart-proxy/get/
proxy_url = "http://xxxxxxxxxxxxxx:@smartproxy.crawlbase.com:8012" 
proxies = {"http": proxy_url, "https": proxy_url}

bard = Bard(token='xxxxxxx', proxies=proxies, timeout=30)
bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
```


### Reusable session object
You can continue the conversation using a reusable session. However, this feature is limited, and it is difficult for a package-level feature to perfectly maintain conversation_id and context. You can try to maintain the consistency of conversations same way as other LLM services, such as passing some sort of summary of past conversations to the DB.
```python
from bardapi import Bard
import requests
# import os
# os.environ['_BARD_API_KEY'] = 'xxxxxxx'
token = 'xxxxxxx'

session = requests.Session()
session.headers = {
            "Host": "gemini.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://gemini.google.com",
            "Referer": "https://gemini.google.com/",
        }
# session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 
session.cookies.set("__Secure-1PSID", token) 

bard = Bard(token=token, session=session, timeout=30)
bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']

# Continued conversation without set new session
bard.get_answer("What is my last prompt??")['content']
```

<details>
<summary>Async Bard Code (Click to expand)</summary>

```python
from httpx import AsyncClient
from bardapi import BardAsync
import os

# Uncomment and set your API key as needed
# os.environ['_BARD_API_KEY'] = 'xxxxxxx'
token = 'xxxxxxx'  # Replace with your actual token

SESSION_HEADERS = {
    "Host": "gemini.google.com",
    "X-Same-Domain": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://gemini.google.com",
    "Referer": "https://gemini.google.com/",
}
timeout = 30  # Example timeout
proxies = {}  # Replace with your proxies if needed

client = AsyncClient(
    http2=True,
    headers=SESSION_HEADERS,
    cookies={"__Secure-1PSID": token},
    timeout=timeout,
    proxies=proxies,
)

bard_async = BardAsync(token=token, client=client)

# Asynchronous function to get the answer
async def get_bard_answer(question):
    await bard_async.async_setup()  # Ensure async setup is done
    return await bard_async.get_answer(question)

response = await get_bard_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")
print(response['content'])
```

</details>


### Auto Cookie Bard
Using [browser_cookie3](https://github.com/borisbabic/browser_cookie3) we extract the `__Secure-1PSID` cookie from all browsers, and then we can use the API without passing the token. However, there are still incomplete dependency packages and various variables, so please seek assistance in the following [GitHub Issues](https://github.com/borisbabic/browser_cookie3/issues) or adjust your browser's version.
- Visit https://gemini.google.com/ in your browser and execute the following command while in the chat-enabled state. Refer to browser_cookie3 for details on how it works. If any issues arise, please restart the browser or log in to your Google account again. 
*Recommended to keep the browser open.*
```python
from bardapi import Bard

bard = Bard(token_from_browser=True)
response = bard.get_answer("Do you like cookies?")
print(response['content'])
```

### Bard `ask_about_image` method 
*It may not work as it is only available for certain accounts, regions, and other restrictions.*
As an experimental feature, it is possible to ask questions with an image. However, this functionality is only available for accounts with image upload capability in Bard's web UI. 

```python
from bardapi import Bard

bard = Bard(token='xxxxxxx')
image = open('image.jpg', 'rb').read() # (jpeg, png, webp) are supported.
bard_answer = bard.ask_about_image('What is in the image?', image)
print(bard_answer['content'])
```

### [Text To Speech(TTS)](https://cloud.google.com/text-to-speech?hl=ko) from Bard
Business users and high traffic volume may be subject to account restrictions according to Google's policies. Please use the [Official Google Cloud API](https://cloud.google.com/text-to-speech) for any other purpose. 
The user is solely responsible for all code, and it is imperative to consult Google's official services and policies. Furthermore, the code in this repository is provided under the MIT license, and it disclaims any liability, including explicit or implied legal responsibilities.
```python
from bardapi import Bard

bard = Bard(token='xxxxxxx')
audio = bard.speech('Hello, I am Bard! How can I help you today?')
with open("speech.ogg", "wb") as f:
  f.write(bytes(audio['audio']))
```

<br>

## [More features](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md)
Starting from version `0.1.18`, the GitHub version of BardAPI will be synchronized with the PyPI version and released simultaneously. However, the version undergoing QA can still be used from the GitHub repository.<br>
```
$ pip install git+https://github.com/dsdanielpark/Bard-API.git
```

- [Multi-cookie Bard](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#multi-cookie-bard)
- [Auto Cookie Bard](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#auto-cookie-bard)
- [TTS from Bard](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#text-to-speechtts)
- [Multi-language Bard API](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#multi-language-bard-api)
- [Get image links](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#get-image-links)
- [ChatBard](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#chatbard)
- [Export Conversation](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#export-conversation)
- [Export Code to Repl.it](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#export-code-to-replit)
- [Executing Python code received as a response from Bard](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#chatbard)
- [Using Bard Asynchronously](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#using-bard-asynchronously)
- [Bard Cookies](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#bard-which-can-get-cookies)
- [Fix Coversation ID (Fix Context)](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#fix-conversation-id-fix-context)
- [Max_token, Max_sentences](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#max_token-max_sentence)
- [Translation to another programming language](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#translation-to-another-programming-language)


<br>



##  [Amazing Bard Prompts](https://github.com/dsdanielpark/amazing-bard-prompts) Is All You Need!
- Helpful prompts for Google Bard

<br>

## [The Python package hf-transllm](https://github.com/dsdanielpark/hf-transllm)
If you want to comfortably use the open-source LLM models in your native language, which are `released under the Apache License (allowing free commercial use)` in `various languages`, you can try using the [hf-transllm](https://github.com/dsdanielpark/hf-transllm) package. hf-transllm also supports multilingual inference for various LLMs stored in hugging face repository.

### Example code of [hf-transllm](https://github.com/dsdanielpark/hf-transllm)
<details>
<summary>In case the Google package is no longer available due to policy restrictions, here's a simple example code for using open-source language models (LLMs) in both English and multiple languages.</summary>

<br>

### Usage
For the decoder models provided by Hugging Face, you can easily use them by either following a simple approach or overriding the inference method. You can explore various open-source language models at [this link](https://huggingface.co/models). Through the ranking information from [Open LLM Leader Board Report repository](https://github.com/dsdanielpark/Open-LLM-Leaderboard-Report), you can find information about good models.

#### For LLM that use languages `other than English`
```python
from transllm import LLMtranslator

open_llama3b_kor = LLMtranslator('openlm-research/open_llama_3b', target_lang='ko', translator='google') # Korean

trnaslated_answer = open_llama3b_kor.generate("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")
print(trnaslated_answer)
```

#### For LLM that use `English`
Refer https://github.com/openlm-research/open_llama or using like this:
```python
from transllm import LLMtranslator

open_llama3b = LLMtranslator('openlm-research/open_llama_3b) 

answer = open_llama3b.generate("Tell me about the Korean girl group Newjeans.")
print(answer)
```

</details>

<br>

## What is Google [Gemini](https://deepmind.google/technologies/gemini/#introduction)?
[Gemini](https://deepmind.google/technologies/gemini/#introduction) or formerly knowns as Bard is an advanced, multimodal AI model by [Google DeepMind](https://deepmind.google/), capable of understanding and integrating various information types like text, code, audio, images, and video.

- Paper: https://storage.googleapis.com/deepmind-media/gemini/gemini_1_report.pdf
- Web: https://blog.google/technology/ai/google-gemini-ai/#capabilities
- Code Guide: https://ai.google.dev/tutorials/python_quickstart
- Official API On [Google AI Studio](https://makersuite.google.com/app/apikey).

### Google AI Studio
Google AI Studio creates a new Google Cloud project for each new API key. You also can create an API key in an existing Google Cloud project. All projects are subject to the [Google Cloud Platform Terms of Service](https://cloud.google.com/terms).
- Web: https://makersuite.google.com/app/apikey
- Note: The Gemini API is currently in public preview. Production applications are not supported yet.

### Access to Gemini Pro in Bard API package
The Bard API, sourcing responses from [Google ~~Bard~~Gemini's official website](https://gemini.google.com/chat), allows you to receive the same responses as the website. So, if Gemini answers are available on the web, you can also accessed Gemini through the Bard API. However, it's important to note that responses might also come from other models, not exclusively Gemini Pro or Ultra. 
- There is no official Bard API or early access/waiting list for Gemini, although the [PaLM2 API](https://github.com/dsdanielpark/Bard-API#google-palm-api) is available.
  - Google's PaLM2 API differs from Bard, with some aspects of Bard being superior.
  - It's speculated that after expert review, Bard Advanced lineup will likely provide an official API in 2024.
- Gemini and previous generative AI model responses are provided randomly on Bard Web.
- The Bard API, with its imperfect extension features(e.g, `ask_about_image`), occasionally demonstrates Gemini's capabilities. This behavior may vary by region, language, or Google account.
- More information in the [FAQ](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_FAQ.md).

For more on Gemini:
- [Official API](https://makersuite.google.com/app/apikey)
- [Introducing Gemini: our largest and most capable AI model](https://blog.google/technology/ai/google-gemini-ai/)
- [How it's made: multimodal prompting](https://developers.googleblog.com/2023/12/how-its-made-gemini-multimodal-prompting.html)
- [YouTube Demo](https://www.youtube.com/watch?v=UIZAiXYceBI)

<br>



## Google PaLM
Try demo at https://makersuite.google.com/app/prompts/new_text.
```
who are you?
>> I am powered by PaLM 2, which stands for Pathways Language Model 2, a large language model from Google AI.
```

Google Generative AI
- Official Page: https://blog.google/technology/ai/google-palm-2-ai-large-language-model/
- GitHub: https://github.com/GoogleCloudPlatform/generative-ai
- Try Demo: https://makersuite.google.com/app/prompts/new_text.
- Official Library: https://makersuite.google.com/app/library
- Get API Key: https://makersuite.google.com/app/apikey
- Quick Start Tutorial: https://developers.generativeai.google/tutorials/text_quickstart

### Quick Start
```
$ pip install -q google-generativeai
```

```python
import pprint
import google.generativeai as palm

palm.configure(api_key='YOUR_API_KEY')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)

prompt = "Who are you?"

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)
print(completion.result)
```

<br>

<br>

## Sponsor

<a href="https://crawlbase.com/?utm_source=github_ad&utm_medium=social&utm_campaign=bard_api"><img src="./assets/sponsor_ad.png"></a>
 
**Use data scraping to train your AI models.** 

- Easy to use **API to crawl and scrape** millions of websites
- Use crawlbase for efficient [data extraction](https://crawlbase.com/generative-ai-data?utm_source=github_ad&utm_medium=social&utm_campaign=bard_api) for your **LLMs**
- Average **success rate: 98%**
- Uptime guarantee: **99.9%**
- [Simple docs](https://crawlbase.com/docs?utm_source=github_ad&utm_medium=social&utm_campaign=bard_api) to get started in minutes
- **Asynchronous** Crawling **API** if you need massive amounts of data
- **GDPR** and **CCPA** compliant

Used by **70k+** developers. 


## [FAQ](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_FAQ.md)
Please check the FAQ and open issues for similar questions before creating a new issue. Repeated questions will be kept as open issues. Too many requests can trigger a temporary account block (HTTP 429). Maintain proper intervals, using functions like sleep to avoid rate limits. Policies may vary by country and language, so all users could face temporary or permanent errors via the API.

## Scripts
In the scripts [folder](./scripts/), I have released a script to help you compare [OpenAI-ChatGPT](./scripts/openai_api.ipynb), [Microsoft-EdgeGPT](./scripts/microsoft_api.ipynb) and [Google-Bard](./scripts/google_api.ipynb). I hope they will help more developers.

## Contributors
I would like to express my sincere gratitude to all the contributors.

<a href="https://github.com/dsdanielpark/Bard_API/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=dsdanielpark/Bard_API" />
</a>


<br>

## License
[MIT](https://opensource.org/license/mit/) <br>
We hold no legal responsibility; for more information, please refer to the bottom of the readme file. We just want you to give me and [them](https://github.com/acheong08/Bard) a star.
```
The MIT License (MIT)

Copyright (c) 2023 Minwoo Park

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Shifting Service Policies: Bard and Google's Dynamics 
Bard's service status and Google's API interfaces are in constant flux. *The number of replies is currently limited, but certain users,* such as those utilizing VPNs or proxy servers, have reported slightly higher message caps. Adaptability is crucial in navigating these dynamic service policies. Please note that the cookie values used in this package are not official API values.
            
## Bugs and Issues
Sincerely grateful for any reports on new features or bugs. Your valuable feedback on the code is highly appreciated.

## Contacts
- Core maintainer: [Daniel Park, South Korea](https://github.com/DSDanielPark) <br>
- E-mail: parkminwoo1991@gmail.com <br>

## Reference 
[1] https://github.com/acheong08/Bard <br>
            
> **Warning** Important Notice
  The user assumes all legal responsibilities associated with using the BardAPI package. This Python package merely facilitates easy access to Google Bard for developers. Users are solely responsible for managing data and using the package appropriately. For further information, please consult the Google Bard Official Document.
    
> **Warning** Caution
This Python package is not an official Google package or API service. It is not affiliated with Google and uses Google account cookies, which means that excessive or commercial usage may result in restrictions on your Google account. The package was created to support developers in testing functionalities due to delays in the official Google package. However, it should not be misused or abused. Please be cautious and refer to the Readme for more information.
  
<br><br>
  
*Copyright (c) 2023 MinWoo Park, South Korea*<br>
