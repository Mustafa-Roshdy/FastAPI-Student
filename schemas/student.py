from pydantic import BaseModel, ConfigDict, EmailStr


class StudentBase(BaseModel):
    name:str
    email:EmailStr
    gpa:float


class StudentCreate(StudentBase):
    course_id:int


class StudentCourseResponse(BaseModel):
    id:int
    name:str

    model_config=ConfigDict(from_attributes=True)

class StudentResponse(StudentBase):
    id:int
    course_id:int
    course:StudentCourseResponse

    model_config=ConfigDict(from_attributes=True)
