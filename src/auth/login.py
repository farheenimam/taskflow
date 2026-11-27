"""Signing in (POST /api/auth/login) and finding who sent a request."""
import secrets

# Demo accounts. A real product would keep hashed passwords in a database.
USERS = {"demo@taskflow.test": "Taskflow123!", "api@taskflow.test": "Taskflow123!"}

def login(data: dict) -> tuple[int, dict]:
    email = str(data.get("email") or "").strip().lower()
    if USERS.get(email) != data.get("password"):
        return 401, {"error": "Email or password is incorrect"}
    token = secrets.token_hex(16)
    TOKENS[token] = email
    return 200, {"token": token, "email": email}


def user_for(authorization: str | None) -> str | None:
    """The email behind an "Authorization: Bearer <token>" header, or None."""
    return TOKENS.get((authorization or "").removeprefix("Bearer ").strip())
