# ============================================
               # book.py
# ============================================

class Book:

    def __init__(
        self,
        book_id: str,
        title: str,
        author: str
    ) -> None:

        self.__book_id: str = book_id
        self.__title: str = title
        self.__author: str = author
        self.__available: bool = True

    @property
    def book_id(self) -> str:
        return self.__book_id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def author(self) -> str:
        return self.__author

    @property
    def is_available(self) -> bool:
        return self.__available

    def borrow(self) -> None:
        self.__available = False

    def return_book(self) -> None:
        self.__available = True

    def __str__(self) -> str:

        status: str = (
            "Available"
            if self.__available
            else "Borrowed"
        )

        return (
            f"[{self.__book_id}] "
            f"{self.__title} by "
            f"{self.__author} - {status}"
        )