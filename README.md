Development Status :: 5 - Production/Stable


# Google <a href="https://bard.google.com/"><img src="https://camo.githubusercontent.com/adb54264fe2ad5067d07d0752fc32600b4e6250073b01ce8c386575b431e3f06/68747470733a2f2f7777772e677374617469632e636f6d2f6c616d64612f696d616765732f66617669636f6e5f76315f31353031363063646466663766323934636533302e737667" height="20px"></a> Bard API 


<p align="left">
<a><img alt="PyPI package" src="https://img.shields.io/badge/pypi-BardAPI-black"></a>
<!-- <a href="https://pepy.tech/project/bardapi"><img alt="Downloads" src="https://pepy.tech/badge/bardapi"></a> -->
<!-- <a><img alt="commit update" src="https://img.shields.io/github/last-commit/dsdanielpark/Bard-API?color=black"></a> -->
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/dsdanielpark/Bard-API"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdsdanielpark%2FBARD_API&count_bg=%23000000&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=BardAPI&edge_flat=false"/></a>
<a href="https://pypi.org/project/bardapi/"><img alt="PyPI" src="https://img.shields.io/pypi/v/bardapi"></a>
</p>

> The python package that returns response of [Google Bard](https://bard.google.com/) through API.

![](./assets/bard_api.gif)


Please exercise caution and use this package responsibly.

I referred to [this github repository(github.com/acheong08/Bard)](https://github.com/acheong08/Bard) where inference process of Bard was reverse engineered. Using `__Secure-1PSID`, you can ask questions and get answers from Google Bard. This package is designed for application to the Python package [ExceptNotifier](https://github.com/dsdanielpark/ExceptNotifier) and [Co-Coder](https://github.com/dsdanielpark/Co-Coder). Please note that the bardapi is not a free service, but rather a tool provided to assist developers with testing certain functionalities due to the delayed development and release of Google Bard's API. It has been designed with a lightweight structure that can easily adapt to the emergence of an official API. Therefore, I strongly discourage using it for any other purposes.

<br>


Do not expose the `__Secure-1PSID`
> Note that while I referred to `__Secure-1PSID` value as an API KEY for convenience, it is not an officially provided API KEY. 
Cookie value subject to frequent changes. Verify the value again if an error occurs. Most errors occur when an invalid cookie value is entered.
<br>

##  [Amazing Bard Prompts](https://github.com/dsdanielpark/amazing-bard-prompts) Is All You Need!
- Helpful prompts for Google Bard

<br>

## Install
If you will not provide the language parameter (use `english`, `korean`, `japanese` only as input text):
```
pip install bardapi
```

If you wish to use the Bard API, including the Google Translate feature, with the `language` argument:
```
pip install git+https://github.com/dsdanielpark/Bard-API.git
```

<br>

## Authentication
1. Visit https://bard.google.com/
2. F12 for console
3. Session: Application → Cookies → Copy the value of  `__Secure-1PSID` cookie.

<br>

## Usage 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zzzlTIh0kt2MdjLzvXRby1rWbHzmog8t?usp=sharing) 


Simple Usage

```python
from bardapi import Bard

token = 'xxxxxxxxxx'
bard = Bard(token=token)
bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
```
Or you can use this
```python
from bardapi import Bard
import os
os.environ['_BARD_API_KEY']="xxxxxxxx"

Bard().get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
```

To get reponse dictionary
```python
import bardapi
import os

# set your __Secure-1PSID value to key
token = 'xxxxxxxxxx'

# set your input text
input_text = "나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘"

# Send an API request and get a response.
response = bardapi.core.Bard(token).get_answer(input_text)
```



Addressing errors caused by delayed responses in environments like Google Colab and containers. If an error occurs despite following the proper procedure, utilize the timeout argument.
```python
from bardapi import Bard
import os
os.environ['_BARD_API_KEY']="xxxxxxxx"

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

bard = Bard(token='xxxxxxxxxx', proxies=proxies, timeout=30)
bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
```

### Reusable session object
You can continue the conversation using a reusable session.
```python
from bardapi import Bard
import os
import requests
os.environ['_BARD_API_KEY'] = 'xxxxxxxxxxx'
# token='xxxxxxxxxxx'

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

<br>

# GitHub installation required for the following features.
To remove the dependencies of the bardapi package, you need to install the GitHub developer version.
```
pip install git+https://github.com/dsdanielpark/Bard-API.git
```

### Multi-language Bard API
GitHub Dev version only.
```python
from bardapi import Bard

bard = Bard(token='xxxxxxxx', language='chinese (simplified)')
res = bard.get_answer("你好。")
print(res['content'])
```
or
```python
from bardapi import Bard
import os
os.environ["_BARD_API_LANG"] = 'chinese (simplified)'
os.environ["_BARD_API_KEY"] = 'xxxxxxxx'

res = Bard().get_answer("你好。")
print(res['content'])
```

<br>

### Get image links
GitHub Dev version only.
```python
from bardapi import Bard
bard = Bard(token='xxxxxxxxxxx')
res = bard.get_answer("Find me an image of the main entrance of Stanford University.")
res['links'] # Get image links (list)
res['images'] # Get images (set)
```
<a href="https://bard.google.com/"><img src="./assets/bard_links.png">

<br>
    
### ChatBard
```python
from bardapi import ChatBard
    
chat = ChatBard()
chat.start()
```
or
```python
from bardapi import ChatBard
import os
os.environ["_BARD_API_KEY"] = 'xxxxxx'   # Requird
os.environ["_BARD_API_LANG"] = Arabic    # Optional, Default to English
os.environ["_BARD_API_TIMEOUT"] = 30     # Optional, Session Timeout
 
chat = ChatBard()
chat.start()
```
    
<br>

## Translation to Another Programming Language
Please check the translation results in [this folder](https://github.com/dsdanielpark/Bard-API/tree/main/translate_to).
- Copy the code of [Core.py](https://github.com/dsdanielpark/Bard-API/blob/17d5e948d4afc535317de3964232ab82fe223521/bardapi/core.py).
- Ask ChatGPT to translate like "Translate to Swift."
- Ask ChatGPT to optimize the code or provide any desired instructions until you're satisfied.<br>

![](./assets/translate.png)
            
            
## Scripts
In the scripts [folder](./scripts/), I have released a script to help you compare [OpenAI-ChatGPT](./scripts/openai_api.ipynb), [Microsoft-EdgeGPT](./scripts/microsoft_api.ipynb) and [Google-Bard](./scripts/google_api.ipynb). I hope they will help more developers.

## Shifting Service Policies: Bard and Google's Dynamics 
Bard's service status and Google's API interfaces are in constant flux. *The number of replies is currently limited, but certain users,* such as those utilizing VPNs or proxy servers, have reported slightly higher message caps. Adaptability is crucial in navigating these dynamic service policies. Please note that the cookie values used in this package are not official API values.
            
            
## License
[MIT](https://opensource.org/license/mit/) <br>
I hold no legal responsibility; for more information, please refer to the bottom of the readme file. I just want you to give me and [them](https://github.com/acheong08/Bard) a star.
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

## Bugs and Issues
Sincerely grateful for any reports on new features or bugs. Your valuable feedback on the code is highly appreciated.

## Contacts
- Core maintainer: [Daniel Park, South Korea](https://github.com/DSDanielPark) <br>
- E-mail: parkminwoo1991@gmail.com <br>

## Reference 
[1] https://github.com/acheong08/Bard <br>
[2] https://github.com/discordtehe/Bard
  
<br>
            
### Important Notice
  The user assumes all legal responsibilities associated with using the BardAPI package. This Python package merely facilitates easy access to Google Bard for developers. Users are solely responsible for managing data and using the package appropriately. For further information, please consult the Google Bard Official Document.
    
### Caution!
This Python package is not an official Google package or API service. It is not affiliated with Google and uses Google account cookies, which means that excessive or commercial usage may result in restrictions on your Google account. The package was created to support developers in testing functionalities due to delays in the official Google package. However, it should not be misused or abused. Please be cautious and refer to the Readme for more information.
  

  
*Copyright (c) 2023 MinWoo Park, South Korea*<br>
