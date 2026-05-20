def view_members(self) -> list:
    return list(self.members.values())



# usage in main.py 


members = service.view_members()

if not members:
    print("No members found.")

else:
    for member in members:

        print(
            f"[{member.member_id}] "
            f"{member.name} ({member.email})"
        )
