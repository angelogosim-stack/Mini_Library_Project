def view_books(self) -> list:
    return list(self.books.values())

# usage in main python 

books = service.view_books()

if not books:
    print("No books found.")

else:
    for book in books:

        status = "Available" if book.is_available else "Borrowed"

        print(
            f"[{book.book_id}] "
            f"{book.title} by {book.author} - {status}"
        )