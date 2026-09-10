from datetime import date

from pydantic import BaseModel, Field, ConfigDict


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int
    grade: float = Field(ge=0, le=100)
    enrollment_date: date


class EnrollmentUpdate(BaseModel):
    grade: float = Field(ge=0, le=100)
    enrollment_date: date


class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int
    grade: float
    enrollment_date: date

    model_config = ConfigDict(from_attributes=True)