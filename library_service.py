# ============================================
            # library_service.py
# ============================================

class LibraryError(Exception):
    pass


class BookNotFoundError(LibraryError):
    pass


class MemberNotFoundError(LibraryError):
    pass


class BookUnavailableError(LibraryError):
    pass

from typing import Dict, List

from book import Book
from member import Member
from loan import Loan

from exception import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError
)


class LibraryService:

    def __init__(self) -> None:

        self.__books: Dict[str, Book] = {}
        self.__members: Dict[str, Member] = {}
        self.__loans: List[Loan] = []

    # ADD BOOK

    def add_book(
        self,
        book_id: str,
        title: str,
        author: str
    ) -> None:

        self.__books[book_id] = Book(
            book_id,
            title,
            author
        )

    # REGISTER MEMBER

    def register_member(
        self,
        member_id: str,
        name: str,
        email: str
    ) -> None:

        self.__members[member_id] = Member(
            member_id,
            name,
            email
        )

    # BORROW BOOK

    def borrow_book(
        self,
        book_id: str,
        member_id: str,
        loan_id: str
    ) -> None:

        if book_id not in self.__books:
            raise BookNotFoundError(
                f"Book ID {book_id} not found."
            )

        if member_id not in self.__members:
            raise MemberNotFoundError(
                f"Member ID {member_id} not found."
            )

        book: Book = self.__books[book_id]

        if not book.is_available:
            raise BookUnavailableError(
                f"{book.title} is already borrowed."
            )

        member: Member = self.__members[member_id]

        loan: Loan = Loan(
            loan_id,
            book,
            member
        )

        book.borrow()

        self.__loans.append(loan)

    # RETURN BOOK

    def return_book(
        self,
        book_id: str
    ) -> bool:

        if book_id not in self.__books:
            raise BookNotFoundError(
                f"Book ID {book_id} not found."
            )

        book: Book = self.__books[book_id]

        for loan in self.__loans:

            if (
                loan.book.book_id == book_id
                and loan.is_active
            ):

                loan.close_loan()
                book.return_book()

                return True

        return False

    # VIEW BOOKS

    def view_books(self):

        return self.__books.values()

    # VIEW MEMBERS

    def view_members(self):

        return self.__members.values()

    # VIEW LOANS

    def view_loans(self):

        return self.__loans