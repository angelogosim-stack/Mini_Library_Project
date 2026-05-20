# ============================================
               # loan.py
# ============================================

from book import Book
from member import Member


class Loan:

    def __init__(
        self,
        loan_id: str,
        book: Book,
        member: Member
    ) -> None:

        self.__loan_id: str = loan_id
        self.__book: Book = book
        self.__member: Member = member
        self.__active: bool = True

    @property
    def loan_id(self) -> str:
        return self.__loan_id

    @property
    def book(self) -> Book:
        return self.__book

    @property
    def member(self) -> Member:
        return self.__member

    @property
    def is_active(self) -> bool:
        return self.__active

    def close_loan(self) -> None:
        self.__active = False

    def __str__(self) -> str:

        status: str = (
            "Active"
            if self.__active
            else "Returned"
        )

        return (
            f"Loan {self.__loan_id}: "
            f"{self.__member.name} borrowed "
            f"{self.__book.title} "
            f"({status})"
        )