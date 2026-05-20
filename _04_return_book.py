def return_book(self, book_id: str) -> bool:

    if book_id not in self.books:
        raise BookNotFoundError("Book not found.")

    book = self.books[book_id]

    for loan in self.loans:

        if loan.book.book_id == book_id and loan.is_active:
            loan.complete_return()
            book.mark_as_returned()
            return True

    return False