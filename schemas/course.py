from pydantic import BaseModel, ConfigDict
from datetime import date

class CourseBase(BaseModel):
    name: str


class CourseCreate(CourseBase):
    pass


class CourseStudentResponse(BaseModel):
    national_id: int
    name: str
    email: str
    grade: float
    enrollment_date: date

    model_config = ConfigDict(from_attributes=True)


class CourseResponse(CourseBase):
    id: int
    students: list[CourseStudentResponse] = []

    model_config = ConfigDict(from_attributes=True)