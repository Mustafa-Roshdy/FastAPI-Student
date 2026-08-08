from fastapi import FastAPI
from routers.student import router as student_router
from routers.course import router as course_router

app = FastAPI()

app.include_router(student_router)
app.include_router(course_router)

@app.get("/")
def root():
    return {"message":"server is running"}