from colorama import Fore, Back, Style
import os
from bardapi import Bard
from bardapi.constants import SEPARATOR_LINE, USER_PROMPT, SESSION_HEADERS
import requests


class ChatBard:
    def __init__(self):
        self.bard = None

    def initialize_bard(self):
        print("If you don't want to execute the input, set the following environment variables: _BARD_API_KEY, _BARD_API_LANG, _BARD_API_TIMEOUT. _BARD_API_KEY is required.")
        token = os.getenv("_BARD_API_KEY", input("Enter Bard API Key: "))
        if not token:
            raise SystemExit("API Key is missing. Please set the _BARD_API_KEY environment variable.")

        language = os.getenv("_BARD_API_LANG", input("Enter the language (Just press enter to use English): ")).lower() or 'english'
        timeout = int(os.getenv("_BARD_API_TIMEOUT", input("Enter the timeout value (Just press enter to set 30 sec): "))) or 30

        session = requests.Session()
        session.headers = SESSION_HEADERS
        session.cookies.set("__Secure-1PSID", token)

        self.bard = Bard(token=token, session=session, timeout=timeout, language=language)

    def start(self):
        self.initialize_bard()

        print(f"{SEPARATOR_LINE}\n{Back.BLUE}          Welcome to Chatbot        {Back.RESET}\n{SEPARATOR_LINE}")
        print("If you enter quit, q, or stop, the chat will end.")

        while True:
            user_input = input(USER_PROMPT).lower()
            if user_input in ["quit", "q", "stop"]:
                break

            response = self.bard.get_answer(user_input)

            if response['images']:
                print(f"{Fore.BLUE}{Style.BRIGHT}Chatbot: {response['content']} \n\n Image links: {response['images']}{Fore.RESET}{Style.RESET_ALL}")
            else:
                print(f"{Fore.BLUE}{Style.BRIGHT}Chatbot: {response['content']} {Fore.RESET}{Style.RESET_ALL}")

        print(f"{SEPARATOR_LINE}\n{Fore.RED}Chat Ended.{Fore.RESET}\n\nDanielPark's Chat Template\n{SEPARATOR_LINE}")
