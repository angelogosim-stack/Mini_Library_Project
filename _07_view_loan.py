def view_loans(self) -> list:
    return self.loans


# usage in main.py 
loans = service.view_loans()

if not loans:
    print("No loans found.")

else:
    for loan in loans:

        status = "Active" if loan.is_active else "Returned"

        print(
            f"Loan {loan.loan_id}: "
            f"{loan.member.name} borrowed "
            f"{loan.book.title} ({status})"
        )