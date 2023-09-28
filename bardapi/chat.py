import os
import requests
from typing import Optional
from bardapi import Bard
from colorama import Fore, Back, Style
from bardapi.constants import SEPARATOR_LINE, SESSION_HEADERS


class ChatBard(Bard):
    """
    A class representing a chatbot powered by the Bard API.

    Usage:
        chat = ChatBard()
        chat.start()

    Example:
        from bardapi import ChatBard

        chat = ChatBard()
        chat.start()
    """

    USER_PROMPT = ">>> "

    def __init__(
        self,
        token: Optional[str] = None,
        timeout: int = 20,
        proxies: Optional[dict] = None,
        session: Optional[requests.Session] = None,
        google_translator_api_key: Optional[str] = None,
        language: Optional[str] = None,
        token_from_browser: bool = False,
    ):
        """
        Initialize the Chat Bard.

        Args:
            token (str, optional): Bard API token.
            timeout (int, optional, default = 20): Request timeout in seconds.
            proxies (dict, optional): Proxy configuration for requests.
            session (requests.Session, optional): Requests session object.
            google_translator_api_key (str, optional): Google cloud translation API key.
            language (str, optional): Chat Bard language.
            token_from_browser (bool, optional, default = False): Gets a token from the browser
        """

        self.session = session or self._init_session(token)
        self.language = language or os.getenv("_BARD_API_LANG") or "english"
        self.timeout = int(timeout or os.getenv("_BARD_API_TIMEOUT") or 30)
        self.token = token or os.getenv("_BARD_API_KEY") or self._get_api_key()
        self.token_from_browser = token_from_browser
        self.proxies = proxies
        self.google_translator_api_key = google_translator_api_key

        self.bard = self._init_bard()

        # Chat history
        self.chat_history = []

    @staticmethod
    def _init_session(token):
        session = requests.Session()
        session.headers = SESSION_HEADERS
        session.cookies.set("__Secure-1PSID", token)
        return session

    @staticmethod
    def _get_api_key():
        key = input("Enter the Bard API Key(__Secure-1PSID): ")
        if not key:
            print("Bard API(__Secure-1PSID) Key must be entered.")
            exit(1)
        return key

    def _init_bard(self):
        return Bard(
            token=self.token,
            session=self.session,
            google_translator_api_key=self.google_translator_api_key,
            timeout=self.timeout,
            language=self.language,
            proxies=self.proxies,
            token_from_browser=self.token_from_browser,
        )

    def start(self, prompt: Optional[str] = None) -> None:
        """
        Starts the chatbot interaction.

        Takes user input and retrieves responses from the Bard API until the user enters "quit", "q", or "stop".
        Prints the chatbot's response, including image links if available.

        Parameters:
            prompt (str, optional): Custom prompt message for user input. If not provided, defaults to the class constant USER_PROMPT.

        Returns:
            None
        """

        prompt = prompt or self.USER_PROMPT
        print(
            f"{SEPARATOR_LINE}\n{Back.BLUE}          Welcome to Chatbot        {Back.RESET}\n{SEPARATOR_LINE}"
        )
        print("If you enter quit, q, or stop, the chat will end.")

        # Start chat
        while True:
            user_input = input(prompt).lower()
            if user_input in ["quit", "q", "stop"]:
                break

            # Validate user input
            if not self._is_valid_input(user_input):
                print(f"{Fore.RED}Invalid input! Please try again.{Fore.RESET}")
                continue

            # Get response from Bard API
            try:
                response = self.bard.get_answer(user_input)
                if response.get("error"):
                    print(f"{Fore.RED}Error: {response['error']}{Fore.RESET}")
                else:
                    self._display_response(response)
                    # Add user input and chatbot response to chat history
                    self._add_to_chat_history(user_input, response["content"])
            except requests.exceptions.RequestException as e:
                print(f"{Fore.RED}Error occurred: {str(e)}{Fore.RESET}")

        print(
            f"{SEPARATOR_LINE}\n{Fore.RED}Chat Ended.{Fore.RESET}\n\nDanielPark's Chat Template\n{SEPARATOR_LINE}"
        )

    def display_chat_history(self) -> None:
        """
        Displays the chat history.

        Prints the user input and chatbot responses from the chat history.

        Returns:
            None
        """
        print(
            f"{SEPARATOR_LINE}\n{Back.YELLOW}          Chat History        {Back.RESET}\n{SEPARATOR_LINE}"
        )

        for entry in self.chat_history:
            print(f"{Fore.GREEN}User: {entry['User']}{Fore.RESET}")
            print(f"{Fore.BLUE}Chatbot: {entry['Chatbot']}{Fore.RESET}")

        print(SEPARATOR_LINE)

    @staticmethod
    def _is_valid_input(user_input: str) -> bool:
        """
        Checks if the user input is valid.

        Validates the user input by checking if it is empty or exceeds a certain length.

        Parameters:
            user_input (str): The user input.

        Returns:
            bool: True if the user input is valid, False otherwise.
        """
        if not user_input:
            return False
        if len(user_input) > 1000:
            return False
        return True

    @staticmethod
    def _display_response(response: dict) -> None:
        """
        Displays the chatbot's response.

        Prints the chatbot's response, including image links if available.

        Parameters:
            response (dict): The response from the Bard API.

        Returns:
            None
        """
        if response.get("images"):
            print(
                f"{Fore.BLUE}{Style.BRIGHT}Chatbot: {response['content']} \n\n Image links: {response['images']}{Fore.RESET}{Style.RESET_ALL}"
            )
        else:
            print(
                f"{Fore.BLUE}{Style.BRIGHT}Chatbot: {response['content']} {Fore.RESET}{Style.RESET_ALL}"
            )

    def _add_to_chat_history(self, user_input: str, chatbot_response: str) -> None:
        """
        Adds the user input and chatbot response to the chat history.

        Parameters:
            user_input (str): The user input.
            chatbot_response (str): The chatbot's response.

        Returns:
            None
        """
        self.chat_history.append({"User": user_input, "Chatbot": chatbot_response})
