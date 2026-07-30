import os
import hmac
import hashlib
from dotenv import load_dotenv
from data_mask.file_dataclass import DATAMaskrecords



HMAC_SECRET = os.environ["HMAC_SECRET_KEY"]
SECRET_KEY = os.environ["SECRECY"]
NAME_FIELDS = ["name", "име"]
OTHER_S_FIELDS = ["egn", "eik"]
SKIP_FIELDS = ["type", "id", "appendix"]


def mask_egn(value: str, secret: str) -> str:
    if not value:
        return value

    digest = hmac.new(
        secret.encode("utf-8"),
        value.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()

    # Create exactly the same number of digits as the original
    masked = ""
    for char in digest:
        if char.isdigit():
            masked += char
        else:
            masked += str(int(char, 16) % 10)

        if len(masked) == len(value):
            break

    return masked


def data_mask(records:list[DATAMaskrecords]):
    for record in records:
        for header, value in record.original.items():
            if value is None:
                continue
            value = str(value)
            header_lower = header.strip().lower()
            if any(x in  header_lower for x in SKIP_FIELDS):
                continue
            if any(x in header_lower for x in NAME_FIELDS):
                #simplest one:
                if len(value) >= 3:
                    masked_value = value[:2] + "".join(["*" for x in value[2:]])
                    record.original[header] = masked_value
                else:
                    record.original[header] = "*" * len(value)

            elif any(x in header_lower for x in OTHER_S_FIELDS):
                record.original[header] = mask_egn(value,SECRET_KEY)

    return records

if __name__ == "__main__":
    pass