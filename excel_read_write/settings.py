from data_mask.file_dataclass import DATAMaskrecords
from esg_vehicles.models.main_class import ESGRecord

DATA_PROCESSING_TYPE = {
    "default": ESGRecord,
    "esg_main": ESGRecord,
    "data_mask":DATAMaskrecords,

}

if __name__ == "__main__":
    pass