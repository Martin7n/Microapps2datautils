from dataclasses import dataclass, field
from datetime import datetime



@dataclass
class DATAMaskrecords:
    # raw / orig_data
    original: dict
    values: dict


    # Processing fields
    normalized: list[str] = field(default_factory=list)

    errors: list[str] = field(default_factory=list)

    def get(self, header, default=None):
        return self.original.get(header, default)