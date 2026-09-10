from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import date

class StudentBase(BaseModel):
    name: str
    email: EmailStr


class StudentCreate(StudentBase):
    national_id: str = Field(
        min_length=14,
        max_length=14,
        pattern=r"^\d{14}$"
    )


class StudentCourseResponse(BaseModel):
    id: int
    name: str
    grade: float
    enrollment_date: date

    model_config = ConfigDict(from_attributes=True)


class StudentPhoneResponse(BaseModel):
    id: int
    phone_number: str

    model_config = ConfigDict(from_attributes=True)


class StudentResponse(StudentBase):
    national_id: str
    phones: list[StudentPhoneResponse] = Field(default_factory=list)
    courses: list[StudentCourseResponse] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)