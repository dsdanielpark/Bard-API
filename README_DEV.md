Development Status :: 5 - Production/Stable


# GitHub installation required for the following features.
Starting from version `0.1.18`, the GitHub version of BardAPI will be synchronized with the PyPI version and released simultaneously.
```
pip install git+https://github.com/dsdanielpark/Bard-API.git
```


# Contents
- [GitHub installation required for the following features.](#github-installation-required-for-the-following-features)
- [Contents](#contents)
    - [Multi-language Bard API](#multi-language-bard-api)
    - [Get image links](#get-image-links)
    - [ChatBard](#chatbard)
    - [Executing Python code received as a response from Bard](#executing-python-code-received-as-a-response-from-bard)
    - [Using Bard asynchronously](#using-bard-asynchronously)
    - [Bard which can get Cookies](#bard-which-can-get-cookies)
    - [Fix Conversation ID (Fix Context)](#fix-conversation-id-fix-context)
    - [Translation to Another Programming Language](#translation-to-another-programming-language)



<br>

### Multi-language Bard API
For commercial use cases, please refrain from using the unofficial Google Translate package included in bardapi for non-commercial purposes. Instead, kindly visit the official Google Cloud Translation website. Please use it responsibly, taking full responsibility for your actions, as bardapi package does not assume any implicit or explicit liability.
> Official Google Translation API
- Support Languages: https://cloud.google.com/translate/docs/languages?hl=ko
> Unofficial Google Trnaslator for non-profit purposes (such as feature testing)
- Support Languages: https://github.com/nidhaloff/deep-translator/blob/master/deep_translator/constants.py
```python
from bardapi import Bard

bard = Bard(token=token, language='chinese (simplified)')
res = bard.get_answer("今天首尔的天气怎么样？")
print(res['content'])
```
or
```python
from bardapi import Bard
import os
os.environ["_BARD_API_LANG"] = 'chinese (simplified)'
os.environ["_BARD_API_KEY"] = 'xxxxxxxxx'

res = Bard().get_answer("今天首尔的天气怎么样？")
print(res['content'])
```

<br>

### Get image links
```python
from bardapi import Bard
bard = Bard(token='xxxxxxxxx')
res = bard.get_answer("Find me an image of the main entrance of Stanford University.")
res['links'] # Get image links (list)
res['images'] # Get images (set)
```


<br>
    
### ChatBard
Some errors in ChatBard have been fixed. However, it is recommended not to pass the value of the token through input. See detials in [ChatBard with more features](https://github.com/dsdanielpark/Bard-API/blob/main/README_DEV.md#chatbard-with-more-features).

```python
from bardapi import ChatBard
    
chat = ChatBard(token=token, language='en')
chat.start()
```
or
```python
from bardapi import ChatBard
import os
os.environ["_BARD_API_KEY"] = 'xxxxxxxxx'   # Requird
os.environ["_BARD_API_LANG"] = Arabic    # Optional, Default to English
os.environ["_BARD_API_TIMEOUT"] = 30     # Optional, Session Timeout
 
chat = ChatBard()
chat.start()
```
or
```python
from bardapi import Bard, SESSION_HEADERS
import os
import requests

token='xxxxxxxxx'
session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", token) 
proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
}
    
ChatBard(token=token, session=session, proxies=proxies, timeout=40, language="chinese (simplified)").start()
```

<br>    

### Executing Python code received as a response from Bard
```python
from bardapi import Bard
    
bard = Bard(token="xxxxxxxxx", run_code=True)
bard.get_answer("code a pie chart in python for this data={'blue':25, 'red':30, 'green':30, 'purple':15}")
```
![](assets/bardapi_run_code.png)
    
<br>

### Using Bard asynchronously 
Using asynchronous implementation will be efficient when implementing ChatBots or something alone those lines.    
BardAsync is not using requests library instead it is using httpx library and http2 protocol.
    
BardAsync is present in translate_to.core_async.BardAsync
```python
from bardapi import BardAsync 
    
bard = BardAsync(token="xxxxxxxxx")
await bard.get_answer("What is Metaverse?")
```
or
```python
import asyncio
from bardapi import BardAsync
    
bard = BardAsync(token="xxxxxxxxx")
asyncio.run(bard.get_answer("What is Metaverse?"))
```

<br>
    

### Bard which can get Cookies
```python
from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": "xxxxxxxxx",
    "__Secure-1PSIDTS": "xxxxxxxxx",
    "__Secure-1PSIDCC", "xxxxxxx")
    # Any cookie values you want to pass session object.
}

bard = BardCookies(cookie_dict=cookie_dict)
print(bard.get_answer("こんにちは"))
```

<br>

### Fix Conversation ID (Fix Context)
BART returns multiple responses as candidate answers. Each of these responses is assigned a conversation_id. While using a reusable session, you can observe that your prompt is stored. However, if you desire consistent answers, you can provide the desired conversation_id as an argument among the returned candidate answers.

- Passing only the `session`: Retains your prompt.
- Passing both `session` and `conversation_id`: Retains your prompt and allows you to receive answers with consistent parameters.

```python
from bardapi import Bard, SESSION_HEADERS
import os
import requests

# Set token
token= 'xxxxxxxxx'

# Set session
session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", token) 

# Give session and conversation id
bard = Bard(token=token, session=session, conversation_id="c_1f04f704a788e6e4", timeout=30)
bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
```

<br>

### Translation to Another Programming Language
Please check the translation results in [this folder](https://github.com/dsdanielpark/Bard-API/tree/main/translate_to).
- Copy the code of [Core.py](https://github.com/dsdanielpark/Bard-API/blob/17d5e948d4afc535317de3964232ab82fe223521/bardapi/core.py).
- Ask ChatGPT to translate like "Translate to Swift."
- Ask ChatGPT to optimize the code or provide any desired instructions until you're satisfied.<br>

![](./assets/translate.png)


<br>


## ChatBard with more features
ChatBard is a chatbot class powered by the Bard API. It allows users to have interactive conversations with the chatbot and retrieve responses from the Bard API.

### Usage

```python
from bardapi import ChatBard

chat = ChatBard()
chat.start()
```

### Features
Customize User Prompt
Users can customize the prompt displayed to the user before input by providing a custom prompt message to the start() method.
```pythno
chat.start(prompt="Enter your message: ")
```

### Handle API Errors
Error handling has been implemented for API requests. If an error occurs while communicating with the Bard API, an appropriate error message will be displayed to the user.

### Input Validation
User input is validated before sending it to the API. The input is checked for emptiness and length validation. If the input is invalid, the user is prompted to provide valid input.

### Chat History
Chat history is stored during the conversation, including the user input and the corresponding chatbot responses. The display_chat_history() method can be called to print the chat history.
```python
chat.display_chat_history()
```

### Multilingual Support
Users can select different languages for the chatbot interaction by specifying the language parameter when initializing the ChatBard object. The default language is English.
```python
chat = ChatBard(language="spanish")
```

### Improved User Experience
Chatbot responses are displayed using colors and formatting to enhance the user experience. User input is displayed in green, and chatbot responses are displayed in blue.

### Integration with Other APIs
The ChatBard class focuses on the interaction with the Bard API. If you want to integrate additional APIs, you can extend the functionality by adding appropriate methods and making the necessary API calls within the ChatBard class.
            
            
