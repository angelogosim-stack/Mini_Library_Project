def register_member(self, member_id: str, name: str, email: str) -> None:
    self.members[member_id] = Member(member_id, name, email)