from core.database import base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, Integer


class Course(base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(
        Integer,
        autoincrement=True,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    students: Mapped[list["Student"]] = relationship(
        back_populates="course",
        cascade="all, delete-orphan"
    )