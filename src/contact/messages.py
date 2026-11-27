# game, game, game , game
"""Messages sent from the Contact page (POST /api/contact)."""

MESSAGES: list[dict] = []


def send(data: dict) -> tuple[int, dict]:
    """Checks and keeps one message. Returns (status code, answer)."""
    name, email, message = (str(data.get(key) or "").strip() for key in ("name", "email", "message"))
    if not name or not message or "@" not in email:
        return 400, {"error": "Name, a valid email and a message are needed"}
    MESSAGES.append({"name": name[:100], "email": email[:254], "message": message[:5000]})
    return 201, {"ok": True}
