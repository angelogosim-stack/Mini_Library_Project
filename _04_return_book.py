def return_book():

    print("\n----- RETURN BOOK -----")

    loan_id = input("  Loan ID: ").strip()

    try:
        loan = service.return_book(loan_id)
        print(f"\n  Book returned: {loan.book.title}")
    except ValueError as e:
        print(f"\n  Error: {e}")

