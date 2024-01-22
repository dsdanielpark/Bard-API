Development Status :: 5 - Production/Stable


# GitHub installation required for the following features.
Starting from version `0.1.18`, the GitHub version of BardAPI will be synchronized with the PyPI version and released simultaneously.
```
pip install git+https://github.com/dsdanielpark/Bard-API.git
```


# Contents
- [GitHub installation required for the following features.](#github-installation-required-for-the-following-features)
- [Contents](#contents)
    - [Structure of `core.py - Bard` class](#structure-of-corepy---bard-class)
    - [Auto Cookie Bard](#auto-cookie-bard)
    - [Text To Speech(TTS)](#text-to-speechtts)
    - [Multi-language Bard](#multi-language-bard)
    - [Bard `ask_about_image` method](#bard-ask_about_image-method)
    - [Get image links](#get-image-links)
    - [ChatBard](#chatbard)
    - [Export Conversation](#export-conversation)
    - [Export Code to Repl.it](#export-code-to-replit)
    - [Executing Python code received as a response from Bard](#executing-python-code-received-as-a-response-from-bard)
    - [Using Bard asynchronously](#using-bard-asynchronously)
    - [Multi-cookie Bard](#multi-cookie-bard)
    - [Fix Conversation ID (Fix Context)](#fix-conversation-id-fix-context)
    - [Translation to Another Programming Language](#translation-to-another-programming-language)
    - [max\_token, max\_sentence](#max_token-max_sentence)
    - [ChatBard with more features](#chatbard-with-more-features)
      - [Usage](#usage)
      - [Features](#features)
      - [Handle API Errors](#handle-api-errors)
      - [Input Validation](#input-validation)
      - [Chat History](#chat-history)
      - [Multilingual Support](#multilingual-support)
      - [Improved User Experience](#improved-user-experience)
      - [Integration with Other APIs](#integration-with-other-apis)



<br>


### Structure of `core.py - Bard` class

<details>
<summary> See class structure...</summary>
    
```python
class Bard:
    """
    Bard class for interacting with the Bard API.
    """

    def __init__(
        self,
        token: Optional[str] = None,
        timeout: int = 20,
        proxies: Optional[dict] = None,
        session: Optional[requests.Session] = None,
        conversation_id: Optional[str] = None,
        google_translator_api_key: Optional[str] = None,
        language: Optional[str] = None,
        run_code: bool = False,
        token_from_browser: bool = False,
    ):
        """
        Initialize the Bard instance.
        ...
        """

    def get_answer(self, input_text: str) -> dict:
        """
        Get an answer from the Bard API for the given input text.
        ...
        """

    def speech(self, input_text: str, lang: str = "en-US") -> dict:
        """
        Get speech audio from Bard API for the given input text.
        ...
        """

    def export_conversation(self, bard_answer, title: str = "") -> dict:
        """
        Get Share URL for specific answer from Bard.
        ...
        """

    def ask_about_image(self, input_text: str, image: bytes, lang: Optional[str] = None) -> dict:
        """
        Send Bard image along with question and get an answer.
        ...
        """

    def export_replit(
        self, code: str, langcode: Optional[str] = None, filename: Optional[str] = None, **kwargs
    ) -> dict:
        """
        Get Export URL to repl.it from code.
        ...
        """

    def _get_snim0e(self) -> str:
        """
        Get the SNlM0e value from the Bard API response.
        ...
        """

    def _get_session(self, session: Optional[requests.Session]) -> requests.Session:
        """
        Get the requests Session object.
        """

    def _get_token(self, token: str, token_from_browser: bool) -> str:
        """
        Get the Bard API token either from the provided token or from the browser cookie.
        """ 
```
</details>

<br>

### Auto Cookie Bard
Using [browser_cookie3](https://github.com/borisbabic/browser_cookie3) we extract the `__Secure-1PSID`` cookie from all browsers, and then we can use the API without passing the token. However, there are still incomplete dependency packages and various variables, so please seek assistance in the following [GitHub Issues](https://github.com/borisbabic/browser_cookie3/issues) or adjust your browser's version.

```python
from bardapi import Bard

bard = Bard(token_from_browser=True)
bard_answer = bard.get_answer("Do you like cookies?")['content']
print(bard_answer)
```

<br>

### Text To Speech(TTS)
```python
from bardapi import Bard

bard = Bard(token= xxxxxxxxx )
audio = bard.speech("Hello, I am bard! How can I assist you?", lang='en-US') # Get bytes audio object.

# Save audio object.
with open('bard_response.mp3', 'wb') as f:
    f.write(audio['audio'])
```

<br>

### Multi-language Bard
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

### Bard `ask_about_image` method 
*It may not work as it is only available for certain accounts, regions, and other restrictions.*
As an experimental feature, it is possible to ask questions with an image. However, this functionality is only available for accounts with image upload capability in Bard's web UI.

```python
from bardapi import Bard

bard = Bard(token='xxxxxxxx')
image = open('image.jpg', 'rb').read() # (jpeg, png, webp) are supported.
bard_answer = bard.ask_about_image('What is in the image?', image)
print(bard_answer['content'])
```

<br>

### Get image links
```python
from bardapi import Bard
bard = Bard(token='xxxxxxxx')
res = bard.get_answer("Find me an image of the main entrance of Stanford University.")
res['links'] # Get image links (list)
res['images'] # Get images (list)
```

<br>
    
### ChatBard
Some errors in ChatBard have been fixed. However, it is recommended not to pass the value of the token through input. See detials in [ChatBard with more features](https://github.com/dsdanielpark/Bard-API/blob/main/README_DEV.md#chatbard-with-more-features).

```python
from bardapi import ChatBard
    
chat = ChatBard(token="xxxxxxxx", language='en')
chat.start()
```
or
```python
from bardapi import ChatBard
import os
os.environ["_BARD_API_KEY"]='xxxxxxxx'   # Requird
os.environ["_BARD_API_LANG"]="Arabic"     # Optional, Default to English
os.environ["_BARD_API_TIMEOUT"]=30        # Optional, Session Timeout
 
chat = ChatBard()
chat.start()
```
or
```python
from bardapi import Bard, SESSION_HEADERS
import requests

token='xxxxxxxx'
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

### Export Conversation
*It may not work as it is only available for certain accounts, regions, and other restrictions.*
Bard UI offers a convenient way to share a specific answer from Bard by generating a URL. This feature enables users to easily create and share URLs for individual answers.

```python
from bardapi import Bard
bard = Bard(token='xxxxxxxx')
bard_answer = bard.get_answer('How are you?')
url = bard.export_conversation(bard_answer, title='Example Shared conversation')
print(url['url'])

```

<br>

### Export Code to [Repl.it](https://replit.com/)
```python
from bardapi import Bard

bard = Bard(token='xxxxxxxx')

bard_answer = bard.get_answer("code python to print hello world")
# {'code': 'print("Hello World")', 'program_lang': 'python'}
url = bard.export_replit(
    code=bard_answer['code'],
    program_lang=bard_answer['program_lang'],
)
print(url['url']) # https://replit.com/external/v1/claims/xxx/claim
```

<br>

### Executing Python code received as a response from Bard
```python
from bardapi import Bard
    
bard = Bard(token="xxxxxxxx", run_code=True)
bard.get_answer("code a pie chart in python for this data={'blue':25, 'red':30, 'green':30, 'purple':15}")
```
![](assets/bardapi_run_code.png)
    
<br>

### Using Bard asynchronously 
Using asynchronous implementation will be efficient when implementing ChatBots or something alone those lines.    
BardAsync is not using requests library instead it is using httpx library and http2 protocol.
    
```python
from httpx import AsyncClient
from bardapi import BardAsync
# Uncomment and set your API key as needed
# import os
# os.environ['_BARD_API_KEY'] = 'xxxxxxx'
token = 'xxxxxxx'  # Replace with your actual token

SESSION_HEADERS = {
    "Host": "bard.google.com",
    "X-Same-Domain": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://bard.google.com",
    "Referer": "https://bard.google.com/",
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

<br>
    

### Multi-cookie Bard
Depending on the country, region, and status of your Google account, you may need to use multiple cookies. If so, please provide the cookies in the form of a dictionary.
```python
from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": "xxxxxxxx",
    "__Secure-1PSIDTS": "xxxxxxxx",
    "__Secure-1PSIDCC", "xxxxxxxx",
    # Any cookie values you want to pass session object.
}

bard = BardCookies(cookie_dict=cookie_dict)
print(bard.get_answer("こんにちは")['content'])
```

Bard with reusable session which contain mutiple cookie value
```python
import requests
from bardapi import Bard, SESSION_HEADERS

session = requests.Session()
session.cookies.set("__Secure-1PSID", "bard __Secure-1PSID token")
session.cookies.set( "__Secure-1PSIDCC", "bard __Secure-1PSIDCC token")
session.cookies.set("__Secure-1PSIDTS", "bard __Secure-1PSIDTS token")
session.headers = SESSION_HEADERS

bard = Bard(session=session)
bard.get_answer("How is the weather today in seoul?")
```


Multi-cookie Bard with auto cookies from browser
```python
from bardapi import Bard

bard = BardCookies(token_from_browser=True)
bard.get_answer("How is the weather today in seoul?")
```

<br>

### Fix Conversation ID (Fix Context)
BART returns multiple responses as candidate answers. Each of these responses is assigned a conversation_id. While using a reusable session, you can observe that your prompt is stored. However, if you desire consistent answers, you can provide the desired conversation_id as an argument among the returned candidate answers.

- Passing only the `session`: Retains your prompt.
- Passing both `session` and `conversation_id`: Retains your prompt and allows you to receive answers with consistent parameters.

```python
from bardapi import Bard, SESSION_HEADERS
import requests

# Set token
token= 'xxxxxxxx'

# Set session
session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", token) 

# Give session and conversation id. (check manually)
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

### max_token, max_sentence
Bard does not support temperature or hyperparameter adjustments, but it is possible to achieve the appearance of limiting the number of output tokens or the number of output sentences using simple algorithms, as follows:
```python
from bardapi import Bard, max_token, max_sentence

token = 'xxxxxxx'
bard = Bard(token=token)

# max_token==30
max_token(bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content'], 30) 
# max_sentence==2
max_sentence(bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content'], 2)
```

<br>


### ChatBard with more features
ChatBard is a chatbot class powered by the Bard API. It allows users to have interactive conversations with the chatbot and retrieve responses from the Bard API.

#### Usage

```python
from bardapi import ChatBard

chat = ChatBard()
chat.start()
```

#### Features
Customize User Prompt
Users can customize the prompt displayed to the user before input by providing a custom prompt message to the start() method.
```python
chat.start(prompt="Enter your message: ")
```

#### Handle API Errors
Error handling has been implemented for API requests. If an error occurs while communicating with the Bard API, an appropriate error message will be displayed to the user.

#### Input Validation
User input is validated before sending it to the API. The input is checked for emptiness and length validation. If the input is invalid, the user is prompted to provide valid input.

#### Chat History
Chat history is stored during the conversation, including the user input and the corresponding chatbot responses. The display_chat_history() method can be called to print the chat history.
```python
chat.display_chat_history()
```

#### Multilingual Support
Users can select different languages for the chatbot interaction by specifying the language parameter when initializing the ChatBard object. The default language is English.
```python
chat = ChatBard(language="spanish")
```

#### Improved User Experience
Chatbot responses are displayed using colors and formatting to enhance the user experience. User input is displayed in green, and chatbot responses are displayed in blue.

#### Integration with Other APIs
The ChatBard class focuses on the interaction with the Bard API. If you want to integrate additional APIs, you can extend the functionality by adding appropriate methods and making the necessary API calls within the ChatBard class.
            
            
