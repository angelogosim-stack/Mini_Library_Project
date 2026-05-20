def view_books():

    print("\n----- VIEW BOOKS -----")

    books = service.view_books()

    if not books:
        print("\n  No books found.")
        return

    print('\n  Books:')
    for book in books:
        status = "Available" if book.available else "Borrowed"
        print(f"{book.book_id} - {book.title} by {book.author} [{status}]")

