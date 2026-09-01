from fastapi import FastAPI
from routers.student import router as student_router
from routers.course import router as course_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Student Management System")

app.add_middleware(
    CORSMiddleware,
    # Configure CORS middleware
    origins = [
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://localhost:3000",
    ],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(student_router)
app.include_router(course_router)

@app.get("/")
def root():
    return {"message":"server is running"}