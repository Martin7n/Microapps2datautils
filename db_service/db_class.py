from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON

from db_service.base import Base


class ESGRecordDB(Base):
    __tablename__ = "esg_records"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    leasing_type: Mapped[str | None]
    appendix_id: Mapped[str | None]

    brand: Mapped[str | None]
    model: Mapped[str | None]

    vin: Mapped[str | None] = mapped_column(
        index=True
    )
    registration: Mapped[str | None]

    weight: Mapped[float | None]
    seats: Mapped[int | None]

    fuel_type: Mapped[str | None]

    # # keep original Excel row
    # original: Mapped[dict] = mapped_column(JSON)
    original: Mapped[dict] = mapped_column(
        JSON,
        nullable=False
    )

    def __repr__(self):
        return f"<ESGRecordDB id={self.id} vin={self.vin}>"