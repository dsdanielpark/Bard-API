from abc import ABC, abstractmethod, abstractproperty


class UserContent(ABC):
    @property
    @abstractmethod
    def key(self) -> str:
        pass

    # markdown representation as a long string
    @property
    @abstractmethod
    def markdown_text(self) -> str:
        pass
