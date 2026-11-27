"""Profile information for the signed-in user."""


def for_user(email: str) -> dict[str, str]:
    return {"email": email}
# added new module, mark this module as low, and dont only run login test case.
