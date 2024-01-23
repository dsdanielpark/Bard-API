import os
import requests
from typing import Optional
from colorama import Fore, Back, Style
from bardapi.core import Bard
from bardapi.constants import SEPARATOR_LINE, SESSION_HEADERS
from bardapi.utils import extract_bard_cookie


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
        multi_cookies_bool: bool = False,
        cookie_dict: dict = None,
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
        self.cookie_dict = cookie_dict
        self.multi_cookies_bool = multi_cookies_bool
        self.session = session or self._get_session(token, proxies)
        self.language = language or os.getenv("_BARD_API_LANG", "english")
        self.timeout = int(timeout or os.getenv("_BARD_API_TIMEOUT", 30))
        self.token = self._get_token(token, token_from_browser)
        self.token_from_browser = token_from_browser
        self.proxies = proxies
        self.google_translator_api_key = google_translator_api_key

        super().__init__(
            token=self.token,
            session=self.session,
            google_translator_api_key=self.google_translator_api_key,
            timeout=self.timeout,
            language=self.language,
            proxies=self.proxies,
            token_from_browser=self.token_from_browser,
            cookie_dict=self.cookie_dict,
            multi_cookies_bool=self.multi_cookies_bool,
        )

        # Chat history list
        self.chat_history = []

    def _get_session(
        self, token: Optional[str], proxies: Optional[dict]
    ) -> requests.Session:
        """
        Get the requests Session object.

        Args:
            token (str, optional): Bard API token.
            proxies (dict, optional): Proxy configuration for requests.

        Returns:
            requests.Session: The Session object.
        """
        new_session = requests.Session()
        new_session.headers = SESSION_HEADERS
        new_session.cookies.set("__Secure-1PSID", self.token)
        new_session.proxies = proxies

        if self.cookie_dict is not None:
            for k, v in self.cookie_dict.items():
                new_session.cookies.set(k, v)

        return new_session

    def _get_token(self, token: str, token_from_browser: bool) -> str:
        """
        Get the Bard API token either from the provided token or from the browser cookie.

        Args:
            token (str, optional): Bard API token.
            token_from_browser (bool): Whether to extract the token from the browser cookie.

        Returns:
            str: The Bard API token.
        Raises:
            Exception: If the token is not provided and can't be extracted from the browser.
        """
        if token:
            return token

        env_token = os.getenv("_BARD_API_KEY")
        if env_token:
            return env_token

        if token_from_browser:
            extracted_cookie_dict = extract_bard_cookie(cookies=self.multi_cookies_bool)
            if self.multi_cookies_bool:
                self.cookie_dict = extracted_cookie_dict
                required_cookies = [
                    "__Secure-1PSID",
                    "__Secure-1PSIDTS",
                    "__Secure-1PSIDCC",
                ]
                if len(extracted_cookie_dict) < len(required_cookies) or not all(
                    key in extracted_cookie_dict for key in required_cookies
                ):
                    print(
                        "Essential cookies (__Secure-1PSID, __Secure-1PSIDTS, __Secure-1PSIDCC) are missing."
                    )
                    return extracted_cookie_dict.get("__Secure-1PSID", "")
            if extracted_cookie_dict:
                return extracted_cookie_dict.get("__Secure-1PSID", "")

        raise Exception(
            "Bard API Key must be provided as the 'token' argument or extracted from the browser."
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

    def get_chat_history(self) -> list:
        """
        Retrieve the chat history.

        Usage:
            chat = ChatBard()
            chat.start()
            history_list = chat.get_chat_history()

        Returns:
            list: A list of dictionaries containing chat history entries.
                Each entry has two keys: 'User' and 'Chatbot'.
                'User' contains the user input, and 'Chatbot' contains the chatbot's response.

        Example:
            chat = ChatBard()
            chat.start()
            history_list = chat.get_chat_history()

            # Access individual chat history entries
            for entry in history_list:
                user_input = entry['User']
                chatbot_response = entry['Chatbot']
                print(f"User: {user_input}")
                print(f"Chatbot: {chatbot_response}")

        :return: List of chat history entries.
        :rtype: list
        """
        return self.chat_history

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
