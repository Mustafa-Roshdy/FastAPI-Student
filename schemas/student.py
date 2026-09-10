from pydantic import BaseModel, ConfigDict, EmailStr


class StudentBase(BaseModel):
    name: str
    email: EmailStr


class StudentCreate(StudentBase):
    national_id: int


class StudentCourseResponse(BaseModel):
    id: int
    name: str
    grade: float
    enrollment_date: str

    model_config = ConfigDict(from_attributes=True)


class StudentPhoneResponse(BaseModel):
    id: int
    phone_number: str

    model_config = ConfigDict(from_attributes=True)


class StudentResponse(StudentBase):
    national_id: int
    phones: list[StudentPhoneResponse] = []
    courses: list[StudentCourseResponse] = []

    model_config = ConfigDict(from_attributes=True)