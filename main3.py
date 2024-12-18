from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title: str, author: str, publication_year: int):
        """
        Initializes the book.

        :param title: the title of the book
        :param author: the name of the book's author
        :param publication_year: the year of publication (must not be later than the current year)

        :raises ValueError: if publication year is later than the current year
        """
        current_year = 2024  # Assuming a fixed current year for example
        if publication_year > current_year:
            raise ValueError("Publication year cannot be later than the current year.")

        self.title = title
        self.author = author
        self.publication_year = publication_year

    @abstractmethod
    def read(self) -> None:
        """
        Starts reading the book.

        :return: None

        :Example:
        >>> book = Book("1984", "George Orwell", 1949)  # Create an implementation and test it
        >>> book.read()
        ...
        """
        ...

    @abstractmethod
    def annotate(self, note: str) -> None:
        """
        Adds an annotation to the book.

        :param note: the text of the note
        :return: None

        :Example:
        >>> book.annotate("Interesting idea about control")
        ...
        """
        ...