import os
import hmac
import hashlib
from dotenv import load_dotenv

load_dotenv()

HMAC_SECRET = os.environ["HMAC_SECRET_KEY"]

def anonymize(value: str) -> str:
    return hmac.new(
        HMAC_SECRET.encode("utf-8"),
        value.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()


if __name__ == "__main__":
    customer_id = "customer_12345"

    print(anonymize(customer_id))