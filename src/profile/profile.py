"""Profile information for the signed-in user."""


def for_user(email: str) -> dict[str, str]:
    return {"email"
