import requests
from bardapi import Bard
from colorama import Fore, Back, Style
from bardapi.constants import SEPARATOR_LINE, USER_PROMPT, SESSION_HEADERS


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
            language.lower()
            or os.getenv(
                "_BARD_API_LANG",
                input("Enter the language (Just press enter to use English): "),
            ).lower()
            or "english"
        )
        self.timeout = int(
            timeout
            or os.getenv("_BARD_API_TIMEOUT")
            or input("Enter the timeout value (Just press enter to set 30 sec): ")
            or 30
        )
        self.proxies = proxies

        # Set Bard object
        self.bard = Bard(
            token=token,
            session=self.session,
            timeout=self.timeout,
            language=self.language,
            proxies=self.proxies,
        )

    def start(self) -> None:
        """
        Starts the chatbot interaction.

        Takes user input and retrieves responses from the Bard API until the user enters "quit", "q", or "stop".
        Prints the chatbot's response, including image links if available.
        """

        print(
            f"{SEPARATOR_LINE}\n{Back.BLUE}          Welcome to Chatbot        {Back.RESET}\n{SEPARATOR_LINE}"
        )
        print("If you enter quit, q, or stop, the chat will end.")

        # Start chat
        while True:
            user_input = input(USER_PROMPT).lower()
            if user_input in ["quit", "q", "stop"]:
                break

            # Get response from bard
            response = self.bard.get_answer(user_input)

            if response["images"]:
                print(
                    f"{Fore.BLUE}{Style.BRIGHT}Chatbot: {response['content']} \n\n Image links: {response['images']}{Fore.RESET}{Style.RESET_ALL}"
                )
            else:
                print(
                    f"{Fore.BLUE}{Style.BRIGHT}Chatbot: {response['content']} {Fore.RESET}{Style.RESET_ALL}"
                )

        print(
            f"{SEPARATOR_LINE}\n{Fore.RED}Chat Ended.{Fore.RESET}\n\nDanielPark's Chat Template\n{SEPARATOR_LINE}"
        )
