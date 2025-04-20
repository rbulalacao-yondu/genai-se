import jwt
from datetime import datetime, timedelta

class AuthService:
    def __init__(self, user_repo, secret_key: str):
        self.user_repo = user_repo
        self.secret_key = secret_key

    def login(self, username: str, password: str) -> str | None:
        user = self.user_repo.find_by_username(username)
        if not user or not user.check_password(password):
            return None
        # issue JWT
        payload = {
            "sub": user.id,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }
        return jwt.encode(payload, self.secret_key, algorithm="HS256")

    def logout(self, token: str):
        # blacklist the token
        BlacklistService.add(token)

    def refresh(self, token: str) -> str:
        data = jwt.decode(token, self.secret_key, algorithms=["HS256"])
        data["exp"] = datetime.utcnow() + timedelta(hours=1)
        return jwt.encode(data, self.secret_key, algorithm="HS256")