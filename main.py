from fastapi import FastAPI,Request
from routers.student import router as student_router
from routers.course import router as course_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(title="Student Management System")

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Use explicit list when allow_credentials=True
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Catch unhandled exceptions to prevent losing CORS headers on server crashes
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error", "error": str(exc)},
        headers={"Access-Control-Allow-Origin": request.headers.get("origin", "*")},
    )

app.include_router(student_router)
app.include_router(course_router)

@app.get("/")
def root():
    return {"message":"server is running"}