from datetime import date
from typing import TYPE_CHECKING

from core.database import base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Integer, Float, ForeignKey, Date, UniqueConstraint

if TYPE_CHECKING:
    from models.student import Student
    from models.course import Course


class Enrollment(base):
    __tablename__ = "enrollments"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    student_id: Mapped[str] = mapped_column(
        Integer,
        ForeignKey(
            "students.national_id",
            onupdate="CASCADE",
            ondelete="RESTRICT"
        ),
        nullable=False
    )

    course_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "courses.id",
            onupdate="CASCADE",
            ondelete="RESTRICT"
        ),
        nullable=False
    )

    grade: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    enrollment_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    student: Mapped["Student"] = relationship(
        "Student",
        back_populates="enrollments"
    )

    course: Mapped["Course"] = relationship(
        "Course",
        back_populates="enrollments"
    )

    __table_args__ = (
        UniqueConstraint(
            "student_id",
            "course_id",
            name="unique_student_course"
        ),
    )