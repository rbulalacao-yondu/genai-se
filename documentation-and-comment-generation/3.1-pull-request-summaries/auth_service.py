class AuthService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def login(self, username: str, password: str) -> bool:
        user = self.user_repo.find_by_username(username)
        if not user:
            return False
        return user.check_password(password)

    def logout(self, user_id: int):
        # no-op for now
        pass