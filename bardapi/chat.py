import os
import requests
from bardapi import Bard
from colorama import Fore, Back, Style
from bardapi.constants import SEPARATOR_LINE, SESSION_HEADERS


class ChatBard:
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
        token: str = None,
        timeout: int = 20,
        proxies: dict = None,
        session: requests.Session = None,
        language: str = None,
    ):
        """
        Initialize the ChatBard object.

        Parameters:
            token (str): The Bard API token.
            timeout (int): The timeout value for API requests.
            proxies (dict): Dictionary of proxies to use for API requests.
            session (requests.Session): Optional pre-initialized requests session.
            language (str): The language for Bard API interactions.

        Returns:
            None
        """
        if session is None:
            self.session = requests.Session()
            self.session.headers = SESSION_HEADERS
            self.session.cookies.set("__Secure-1PSID", token)
        else:
            self.session = session
        self.language = (
            language
            or os.getenv(
                "_BARD_API_LANG",
                input("Enter the language (Just press enter to use English): "),
            )
            or "english"
        )
        self.timeout = int(
            timeout
            or os.getenv("_BARD_API_TIMEOUT")
            or input("Enter the timeout value (Just press enter to set 30 sec): ")
            or 30
        )
        self.token = (
            token
            or os.getenv("_BARD_API_KEY")
            or input("Enter the Bard API Key(__Secure-1PSID): ")
            or print("Bard API(__Secure-1PSID) Key must be entered.")
        )
        self.proxies = proxies

        # Set Bard object
        self.bard = Bard(
            token=self.token,
            session=self.session,
            timeout=self.timeout,
            language=self.language,
            proxies=self.proxies,
        )

        # Chat history
        self.chat_history = []

    def start(self, prompt: str = None) -> None:
        """
        Starts the chatbot interaction.

        Takes user input and retrieves responses from the Bard API until the user enters "quit", "q", or "stop".
        Prints the chatbot's response, including image links if available.

        Parameters:
            prompt (str): Custom prompt message for user input. If not provided, defaults to the class constant USER_PROMPT.

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

    def _is_valid_input(self, user_input: str) -> bool:
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

    def _display_response(self, response: dict) -> None:
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
