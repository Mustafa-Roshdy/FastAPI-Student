from typing import TYPE_CHECKING

from core.database import base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, Integer

if TYPE_CHECKING:
    from models.enrollment import Enrollment
    from models.phone import Phone


class Student(base):
    __tablename__ = "students"

    national_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        unique=True
    )

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )

    phones: Mapped[list["Phone"]] = relationship(
        "Phone",
        back_populates="student",
        cascade="all, delete-orphan"
    )

    enrollments: Mapped[list["Enrollment"]] = relationship(
        "Enrollment",
        back_populates="student"
    )