Development Status :: 4 - Beta


# Google <a href="https://bard.google.com/"><img src="https://camo.githubusercontent.com/adb54264fe2ad5067d07d0752fc32600b4e6250073b01ce8c386575b431e3f06/68747470733a2f2f7777772e677374617469632e636f6d2f6c616d64612f696d616765732f66617669636f6e5f76315f31353031363063646466663766323934636533302e737667" height="20px"></a> BARD API 


<p align="left">
<a><img alt="PyPI package" src="https://img.shields.io/badge/pypi-BardAPI-blue"></a>
<a href="https://pypi.org/project/bardapi/"><img alt="PyPI" src="https://img.shields.io/pypi/v/bardapi"></a>
<!-- <a href="https://pepy.tech/project/bardapi"><img alt="Downloads" src="https://pepy.tech/badge/bardapi"></a> -->
<a><img alt="commit update" src="https://img.shields.io/github/last-commit/dsdanielpark/Bard_API?color=blue"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://www.buymeacoffee.com/parkminwoo"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" height="20px"></a>
</p>


> A package that returns Response of Google BARD through API

![](./assets/bardapi.gif)


I referred to the [GitHub repository](https://github.com/acheong08/Bard) where inference process of BARD was reverse engineered. Using `__Secure-1PSID`, you can ask questions and get answers from Google BARD. This package is designed for application to the Python package [ExceptNotifier](https://github.com/dsdanielpark/ExceptNotifier).

<br>

> **Be careful** <br>
> ```Please note that while I referred to __Secure-1PSID value as an API KEY for convenience, it is not an officially provided API KEY. Since this is not an official service, be extra cautious not to leak it externally, and be aware that there are no methods to revoke and reissue the __Secure-1PSID value.```

<br>


## Install
The latest stable release (and required dependencies) can be installed from PyPI:
```
pip install bardapi
```
You may instead want to use the development version from Github:
```
pip install git+https://github.com/dsdanielpark/BARD_API.git
```

<br>

## Authentication
1. Visit https://bard.google.com/
2. F12 for console
3. Session: Application → Cookies → Copy the value of  __Secure-1PSID cookie.

<br>

## Usage 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1hxhoA9ZsO7sgc59WtfojNwZZLGxlX4Sl?usp=share_link)

Simple Usage
```python
from bardapi import Bard
import os

os.environ['_BARD_API_KEY']="xxxxxxxx."
Bard().get_answer("What is Google BARD????")['content']
```


Or you can use this
```python
import bardapi
import os

# set your __Secure-1PSID value to key
os.environ['_BARD_API_KEY']="xxxxxxxx."

# set your input text
input_text = "What is Google Bard???"

# Send an API request and get a response.
response = bardapi.core.Bard().get_answer(input_text)
```

<br>

## License 
Just Give me and [them](https://github.com/acheong08/Bard) a star.

# Reference [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdsdanielpark%2FBARD_API&count_bg=%2379C83D&title_bg=%23555555&icon=python.svg&icon_color=%23E7E7E7&title=BardAPI&edge_flat=false)](https://hits.seeyoufarm.com)
[1] https://github.com/acheong08/Bard
