Development Status :: 5 - Production/Stable


# Google <a href="https://bard.google.com/"><img src="https://camo.githubusercontent.com/adb54264fe2ad5067d07d0752fc32600b4e6250073b01ce8c386575b431e3f06/68747470733a2f2f7777772e677374617469632e636f6d2f6c616d64612f696d616765732f66617669636f6e5f76315f31353031363063646466663766323934636533302e737667" height="20px"></a> Bard API

<p align="left">
<a href="https://github.com/dsdanielpark/Bard-API"><img alt="PyPI package" src="https://img.shields.io/badge/pypi-BardAPI-black"></a>
<!-- <a href="https://pepy.tech/project/bardapi"><img alt="Downloads" src="https://pepy.tech/badge/bardapi"></a> -->
<!-- <a><img alt="commit update" src="https://img.shields.io/github/last-commit/dsdanielpark/Bard-API?color=black"></a> -->
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/dsdanielpark/Bard-API"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdsdanielpark%2FBARD_API&count_bg=%23000000&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=BardAPI&edge_flat=false"/></a>
<a href="https://github.com/dsdanielpark/Bard-API/stargazers"><img src="https://img.shields.io/github/stars/dsdanielpark/Bard-API?style=social"></a>
<a href="https://pypi.org/project/bardapi/"><img alt="PyPI" src="https://img.shields.io/pypi/v/bardapi"></a>
<a href="https://www.buymeacoffee.com/parkminwoo"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-orange.png" height="20px"></a>
  
</p>


> The python package that returns response of [Google Bard](https://bard.google.com/) through value of cookie.

![](./assets/bard_api.gif)


**Please exercise caution and use this package responsibly.**

I referred to this github repository([github.com/acheong08/Bard](https://github.com/acheong08/Bard)) where inference process of Bard was reverse engineered. Using `__Secure-1PSID`, you can ask questions and get answers from Google Bard. This package is designed for application to the Python package [ExceptNotifier](https://github.com/dsdanielpark/ExceptNotifier) and [Co-Coder](https://github.com/dsdanielpark/Co-Coder). Please note that the bardapi is not a free service, but rather a tool provided to assist developers with testing certain functionalities due to the delayed development and release of Google Bard's API. It has been designed with a lightweight structure that can easily adapt to the emergence of an official API. Therefore, I strongly discourage using it for any other purposes. If you have access to official [PaLM-2 API](https://blog.google/technology/ai/google-palm-2-ai-large-language-model/), replace the provided response with the corresponding official code.

<br>

- [Google  Bard API](#google--bard-api)
  - [What is Google Bard?](#what-is-google-bard)
  - [Install](#install)
  - [Authentication](#authentication)
  - [Usage](#usage)
  - [Further](#further)
    - [Behind a proxy](#behind-a-proxy)
    - [Reusable session object](#reusable-session-object)
    - [Auto Cookie Bard](#auto-cookie-bard)
    - [Bard `ask_about_image` method](#bard-ask_about_image-method)
    - [Text To Speech(TTS) from Bard](#text-to-speechtts-from-bard)
  - [More features](#more-features)
  - [Before using the Bard API](#before-using-the-bard-api)



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

## What is Google Bard?
Bard is a conversational generative artificial intelligence chatbot developed by Google, based initially on the LaMDA family of LLMs(Large Language Models) and later the PaLM LLM. Please check official documents for [updates](https://bard.google.com/updates) on Bard, including [available regions and languages](https://support.google.com/bard/answer/13575153?hl=en).

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
> **Warning** Do not expose the `__Secure-1PSID` 
1. Visit https://bard.google.com/
2. F12 for console
3. Session: Application → Cookies → Copy the value of  `__Secure-1PSID` cookie.

Note that while I referred to `__Secure-1PSID` value as an API key for convenience, it is not an officially provided API key. 
Cookie value subject to frequent changes. Verify the value again if an error occurs. Most errors occur when an invalid cookie value is entered.

<br>

If you need to set multiple Cookie values

- [Bard Cookies](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#multi-cookie-bard) - After confirming that multiple cookie values are required to receive responses reliably in certain countries, I will deploy it for testing purposes. Please debug and create a pull request


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
os.environ['_BARD_API_KEY']="xxxxxxx"

Bard().get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
```

To get reponse dictionary
```python
import bardapi
import os

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
import os

# Change 'http://proxy.example.com:8080' to your http proxy
# timeout in seconds
proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
}

bard = Bard(token='xxxxxxx', proxies=proxies, timeout=30)
bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
```

## Use rotating proxies

If you want to **avoid blocked requests** and bans, then use [Smart Proxy by Crawlbase](https://crawlbase.com/docs/smart-proxy/?utm_source=github_ad&utm_medium=social&utm_campaign=bard_api). It forwards your connection requests to a **randomly rotating IP address** in a pool of proxies before reaching the target website. The combination of AI and ML make it more effective to **avoid CAPTCHAs and blocks**.

### Reusable session object
You can continue the conversation using a reusable session.
```python
from bardapi import Bard
import os
import requests
os.environ['_BARD_API_KEY'] = 'xxxxxxx'
# token='xxxxxxx'

session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 
# session.cookies.set("__Secure-1PSID", token) 

bard = Bard(token=token, session=session, timeout=30)
bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']

# Continued conversation without set new session
bard.get_answer("What is my last prompt??")['content']
```

### Auto Cookie Bard
Using [browser_cookie3](https://github.com/borisbabic/browser_cookie3) we extract the `__Secure-1PSID` cookie from all browsers, and then we can use the API without passing the token. However, there are still incomplete dependency packages and various variables, so please seek assistance in the following [GitHub Issues](https://github.com/borisbabic/browser_cookie3/issues) or adjust your browser's version.
- Visit https://bard.google.com/ in your browser and execute the following command while in the chat-enabled state. Refer to browser_cookie3 for details on how it works. If any issues arise, please restart the browser or log in to your Google account again. 
*Recommended to keep the browser open.*
```python
from bardapi import Bard

bard = Bard(token_from_browser=True)
res = bard.get_answer("Do you like cookies?")
print(res['content'])
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
- [max_token-max_sentence](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#max_token-max_sentence)
- [Translation to another programming language](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#translation-to-another-programming-language)


<br>

## Before using the Bard API
- Google Bard can return different responses based on various factors such as account, country, region, IP, etc., following Google's policies. This means that even well-functioning methods, especially the `ask_about_image` method, can encounter Response Errors, which are caused by various reasons related to Google's policies, not package errors. It cannot be resolved at the package level. (e.g., CAPTCHA or HTTP 429 error)
- The API token(__Secure-1PSID cookie value) for this service is unofficial. Additionally, exposing it can allow others to easily use the Bard service with your Google ID, so never expose it.
- This service has very limited and variable call limits per unit of time, and exceeding rate limiting temporarily prevents obtaining normal response results.
- Sending the same question multiple times in requests can also temporarily prevent obtaining normal response results.
- Some regions may require additional cookie values besides __Secure-1PSID; refer to the issue page.
- The __Secure-1PSID cookie value may change frequently. Logout, restart your web browser, and enter the new __Secure-1PSID cookie value.
- Using this package for real-world applications is highly inappropriate. Due to rate limiting and variable API policies, it will only function temporarily.
- If the time interval between requests is very short, the Google API process may interpret it as performing a large number of requests and may not return normal responses.
- All these policies are subject to change, and the interface is also variable.


<br>


##  [Amazing Bard Prompts](https://github.com/dsdanielpark/amazing-bard-prompts) Is All You Need!
- Helpful prompts for Google Bard


## [hf-transllm](https://github.com/dsdanielpark/hf-transllm)
If you want to test the open-llama model, which is `released under the Apache License (allowing free commercial use)` in `various languages`, you can try using the [hf-transllm](https://github.com/dsdanielpark/hf-transllm) package. hf-transllm also supports multilingual inference for various LLMs stored in hugging face repository.

## Example code of [hf-transllm](https://github.com/dsdanielpark/hf-transllm)
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

# Google PaLM API
You can explore information about various generative AI models by Google. Although the palm2 API seems to be under preparation, you can check out demos related to palm2 on the demo page.

## PaLM API
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

<br><br>


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
