def borrow_book():

   print("\n--- BORROW BOOK ---")

   book_id = input("  Book ID  : ").strip()
   member_id = input("  Member ID: ").strip()

   book = service.books.get(book_id)
   if book is None:
       print("\n Book not found.")
       return

   member = service.members.get(member_id)
   if member is None:
       print("\n Member not found.")
       return

   if not book.available:
       print("\n Book is already borrowed.")
       return

   book.borrow()
   loan = Loan(book, member)
   service.loans.append(loan)

   print(f"\n  {member.name} borrowed {book.title}")

