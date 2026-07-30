import os
import hmac
import hashlib
from dotenv import load_dotenv

from data_clean.raw_dataclass import RAWDATArecords
from data_clean.vins import vin_check, reg_check
from esg_backup_v1.weight_check import weight_normalization
from esg_vehicles.processors.category_check import category_handler


def process_records(records:list[RAWDATArecords]):
    count = 0
    data_ex = {}

    for record in records:
        record.updated_serialnum = vin_check(record.serialnum)
        record.updated_tdregno = reg_check(record.tdregno)

        record.updated_tdweight = weight_normalization(record.tdweight, record.tdmeasure)
        record.updated_tdmeasure = "kg"
        record.updated_tdmeasureid = "1"

        record.updated_tdfuel = ""
        record.updated_tdfuelid = ""

        record.updated_tdtype = ""
        record.updated_tdtypeid = ""

        record.updated_emissions= ""

if __name__ == "__main__":
    pass