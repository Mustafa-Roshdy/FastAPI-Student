from core.database import base
from sqlalchemy.orm import relationship,Mapped,mapped_column
from sqlalchemy import Float,String,Integer,Enum,ForeignKey
class Student(base):
    __tablename__="students"

    id:Mapped[int]=mapped_column(Integer,autoincrement=True,primary_key=True)
    name:Mapped[str]=mapped_column(String(50),nullable=False)
    email:Mapped[str]=mapped_column(String,nullable=False)
    course_id:Mapped[int]=mapped_column(Integer,ForeignKey("courses.id"))
    gpa: Mapped[float] = mapped_column(Float)

    course:Mapped["Course"]=relationship(back_populates="students")

