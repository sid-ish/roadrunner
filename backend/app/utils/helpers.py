import time
import hmac
import hashlib
from app.core.config import AUTH_SECRET, TOKEN_TTL_SECONDS

def generate_token():
    expiry = int(time.time()) + TOKEN_TTL_SECONDS
    payload = f"{expiry}"
    signature = hmac.new(
        AUTH_SECRET.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    return f"{payload}.{signature}"

def verify_token(token: str):
    try:
        expiry, signature = token.split(".")
        if int(expiry) < int(time.time()):
            return False

        expected = hmac.new(
            AUTH_SECRET.encode(),
            expiry.encode(),
            hashlib.sha256
        ).hexdigest()

        return hmac.compare_digest(signature, expected)
    except Exception:
        return False

def generate_id():
    import uuid
    return str(uuid.uuid4())
