# ============================================
                # main.py
# ============================================

from library_service import LibraryService
from exception import LibraryError


class LibraryApp:

    def __init__(self) -> None:

        self.service: LibraryService = (
            LibraryService()
        )

    # ========================================
    # DISPLAY MENU
    # ========================================

    def display_menu(self) -> None:

        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")

        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Members")
        print("7. View Loans")
        print("8. Exit")

    # ========================================
    # RUN APPLICATION
    # ========================================

    def run(self) -> None:

        while True:

            self.display_menu()

            choice: str = input(
                "\nSelect option: "
            )

            try:

                # ====================================
                # ADD BOOK
                # ====================================

                if choice == "1":

                    book_id: str = input(
                        "Book ID: "
                    )

                    title: str = input(
                        "Title: "
                    )

                    author: str = input(
                        "Author: "
                    )

                    self.service.add_book(
                        book_id,
                        title,
                        author
                    )

                    print(
                        "\n✅ Book Added"
                    )

                # ====================================
                # REGISTER MEMBER
                # ====================================

                elif choice == "2":

                    member_id: str = input(
                        "Member ID: "
                    )

                    name: str = input(
                        "Name: "
                    )

                    email: str = input(
                        "Email: "
                    )

                    self.service.register_member(
                        member_id,
                        name,
                        email
                    )

                    print(
                        "\n✅ Member Registered"
                    )

                # ====================================
                # BORROW BOOK
                # ====================================

                elif choice == "3":

                    book_id: str = input(
                        "Book ID: "
                    )

                    member_id: str = input(
                        "Member ID: "
                    )

                    loan_id: str = input(
                        "Loan ID: "
                    )

                    self.service.borrow_book(
                        book_id,
                        member_id,
                        loan_id
                    )

                    print(
                        "\n✅ Book Borrowed"
                    )

                # ====================================
                # RETURN BOOK
                # ====================================

                elif choice == "4":

                    book_id: str = input(
                        "Book ID: "
                    )

                    returned: bool = (
                        self.service.return_book(
                            book_id
                        )
                    )

                    if returned:

                        print(
                            "\n✅ Book Returned"
                        )

                    else:

                        print(
                            "\n⚠️ No active loan found."
                        )

                # ====================================
                # VIEW BOOKS
                # ====================================

                elif choice == "5":

                    books = (
                        self.service.view_books()
                    )

                    print("\n===== BOOKS =====")

                    found: bool = False

                    for book in books:

                        found = True
                        print(book)

                    if not found:

                        print(
                            "📭 No books found."
                        )

                # ====================================
                # VIEW MEMBERS
                # ====================================

                elif choice == "6":

                    members = (
                        self.service.view_members()
                    )

                    print("\n===== MEMBERS =====")

                    found: bool = False

                    for member in members:

                        found = True
                        print(member)

                    if not found:

                        print(
                            "📭 No members found."
                        )

                # ====================================
                # VIEW LOANS
                # ====================================

                elif choice == "7":

                    loans = (
                        self.service.view_loans()
                    )

                    print("\n===== LOANS =====")

                    found: bool = False

                    for loan in loans:

                        found = True
                        print(loan)

                    if not found:

                        print(
                            "📭 No loans found."
                        )

                # ====================================
                # EXIT
                # ====================================

                elif choice == "8":

                    print(
                        "\nProgram Closed."
                    )

                    break

                else:

                    print(
                        "\n⚠️ Invalid Choice."
                    )

            except LibraryError as error:

                print(
                    f"\n❌ Error: {error}"
                )

            except Exception as error:

                print(
                    f"\n💥 System Error: {error}"
                )


if __name__ == "__main__":

    app: LibraryApp = LibraryApp()
    app.run()()