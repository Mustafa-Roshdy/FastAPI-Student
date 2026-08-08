from pydantic import BaseModel, ConfigDict, EmailStr


class StudentBase(BaseModel):
    name:str
    email:EmailStr
    gpa:float


class StudentCreate(StudentBase):
    course_id:int


class StudentResponse(StudentBase):
    id:int
    course_id:int

    model_config=ConfigDict(from_attributes=True)
