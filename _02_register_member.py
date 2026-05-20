def register_member():

    print("\n----- REGISTER MEMBER -----")

    member_id = input(" Member ID  : ").strip()
    name = input(" Member Name : ").strip()
    email = input(" Member Email: ").strip()

    member = service.register_member(member_id, name, email)
    print(f"\n  Member registered: {member.name}")

