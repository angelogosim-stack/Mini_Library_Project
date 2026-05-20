def borrow_book(self, book_id: str, member_id: str, loan_id: str) -> None:

    if book_id not in self.books:
        raise BookNotFoundError("Book not found.")

    if member_id not in self.members:
        raise MemberNotFoundError("Member not found.")

    book = self.books[book_id]

    if not book.is_available:
        raise BookUnavailableError("Book is already borrowed.")

    member = self.members[member_id]

    loan = Loan(loan_id, book, member)

    book.mark_as_borrowed()

    self.loans.append(loan)