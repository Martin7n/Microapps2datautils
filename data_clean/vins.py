import re
import os
from dotenv import load_dotenv




load_dotenv()
vin_pattern = os.environ["VIN_CONVENTION"]
reg_pattern_uni = os.environ["REG_CONVENTION"]

def vin_check(record):
    record = record.strip()
    match  = re.match(vin_pattern, record)
    return match.group(0) if match else record


def reg_check(record):
    record = record.strip()
    match  = re.match(reg_pattern_uni, record)
    return match.group(0) if match else record



if __name__ == "__main__":
    pass