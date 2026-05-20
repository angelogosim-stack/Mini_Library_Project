def view_loans():

   print("\n----- VIEW LOANS -----")

   loans = service.view_loans()

   if not loans:
       print("\n No loans found.")
       return

   print("\n Loans:")
   for loan in loans:
       status = "Active" if loan.is_active else "Closed"
       print(f"{loan.loan_id} - {loan.member.name} borrowed "
             f"{loan.book.title} [{status}]")

