from typing import TYPE_CHECKING

from core.database import base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, Integer

if TYPE_CHECKING:
    from models.enrollment import Enrollment


class Course(base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    enrollments: Mapped[list["Enrollment"]] = relationship(
        "Enrollment",
        back_populates="course"
    )