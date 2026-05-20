# ============================================
              # member.py
# ============================================

class Member:

    def __init__(
        self,
        member_id: str,
        name: str,
        email: str
    ) -> None:

        self.__member_id: str = member_id
        self.__name: str = name
        self.__email: str = email

    @property
    def member_id(self) -> str:
        return self.__member_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    def __str__(self) -> str:

        return (
            f"[{self.__member_id}] "
            f"{self.__name} "
            f"({self.__email})"
        )