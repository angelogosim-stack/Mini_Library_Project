def view_members():

   print("\n----- VIEW MEMBERS -----")

   members = service.view_members()

   if not members:
       print("\n No members found.")
       return

   print("\n Members:")
   for member in members:
       print(f"{member.member_id} - {member.name} ({member.email})") 

