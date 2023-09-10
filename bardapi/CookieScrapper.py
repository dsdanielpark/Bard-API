import json
import subprocess
import pyautogui
from time import sleep
import os
import platform
def CookieScraper(browser:str="brave",**kwargs):
  """
    browser:str pass the browser named where the cookies editor is installed
    Install the Cookie Editor from the chrome browser "https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm"
  """
    url = "https://bard.google.com"
    # Use xdg-open to open the URL in the default web browser
    subprocess.run(["brave", url])
    screen_width, screen_height = pyautogui.size()
    x1=kwargs.get("x1")
    y1=kwargs.get("y1")
    x2=kwargs.get("x2")
    y2=kwargs.get("y2")
    x3=kwargs.get("x3")
    y3=kwargs.get("y3")
    x4=kwargs.get("x4")
    y4=kwargs.get("y4")
    sleep(2)
    pyautogui.click(x=x1,y=y1)
    sleep(1)
    pyautogui.click(x=x2,y=y2)
    sleep(1)
    pyautogui.click(x=y3,y=y3)
    sleep(1)
    pyautogui.click(x=x4,y=y4)
    # Close the current tab in Brave
    pyautogui.hotkey("ctrl", "w")
    if platform=="Windows":
      data=pyautogui.hotkey("ctrl","v")
    else:
    #sudo apt install xclip in Linux
        data=subprocess.check_output(["xclip", "-o", "-selection", "clipboard"], text=True)
    try:
        json_data = json.loads(data)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")

    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    SIDValue = next((item for item in json_data if item["name"] == SID), None)
    TSValue = next((item for item in json_data if item["name"] == TS), None)
    CCValue = next((item for item in json_data if item["name"] == CC), None)

    if SIDValue is not None:
        SIDValue = SIDValue["value"]
    else:
        print(f"{SIDValue} not found in the JSON data.")

    if TSValue is not None:
        TSValue = TSValue["value"]
    else:
        print(f"{TSValue} not found in the JSON data.")

    if CCValue is not None:
        CCValue = CCValue["value"]
    else:
        print(f"{CCValue} not found in the JSON data.")

    cookie_dict = {
        "__Secure-1PSID": SIDValue,
        "__Secure-1PSIDTS": TSValue,
        "__Secure-1PSIDCC": CCValue,
    }
    return cookie_dict
