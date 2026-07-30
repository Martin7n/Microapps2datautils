from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class RAWDATArecords:
    # raw / orig_data
    original: dict
    values: dict
    equipallocid: str | None = None
    equipment: str | None = None
    tdregno: str | None = None
    serialnum: str | None = None
    tdweight: str | None = None
    tdweightid: str | None = None
    tdmeasure: str | None = None
    tdmeasureid: str | None = None
    tdfuel:str | None = None
    tdfuelid: str | None = None
    emissions: str | None = None
    tdtype: str | None = None
    tdtypeid: str | None = None

    #upd data...obviously :)
    updated_serialnum : str | None = None
    updated_tdregno: str | None = None
    updated_tdweight: str | None = None
    updated_tdweightid: str | None = None
    updated_tdmeasure: str | None = None
    updated_tdmeasureid: str | None = None
    updated_tdfuel: str | None = None
    updated_tdfuelid: str | None = None
    updated_emissions: str | None = None
    updated_tdtype: str | None = None
    updated_tdtypeid: str | None = None

    # Processing fields
    normalized: list[str] = field(default_factory=list)

    errors: list[str] = field(default_factory=list)

    def get(self, header, default=None):
        return self.original.get(header, default)