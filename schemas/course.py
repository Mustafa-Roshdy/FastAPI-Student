from pydantic import BaseModel, ConfigDict, EmailStr


class CourseBase(BaseModel):
    name:str


class CourseCreate(CourseBase):
    pass


class CourseStudentResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    gpa:float

    model_config=ConfigDict(from_attributes=True)

class CourseResponse(CourseBase):
    id:int
    students: list[CourseStudentResponse]=[]
    model_config=ConfigDict(from_attributes=True)