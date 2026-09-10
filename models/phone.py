from typing import TYPE_CHECKING

from core.database import base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey

if TYPE_CHECKING:
    from models.student import Student


class Phone(base):
    __tablename__ = "phones"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    student_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "students.national_id",
            onupdate="CASCADE",
            ondelete="RESTRICT"
        ),
        nullable=False
    )

    phone_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True
    )

    student: Mapped["Student"] = relationship(
        "Student",
        back_populates="phones"
    )