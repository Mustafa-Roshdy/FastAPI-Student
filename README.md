# Student & Course Management API

A full-stack **Student & Course Management System** built with **FastAPI**, **SQLAlchemy**, and a simple **HTML/CSS/JavaScript frontend**.

The application allows you to:

* Create, read, update, and delete courses.
* Create, read, update, and delete students.
* Assign students to courses.
* Retrieve a student's course.
* Retrieve a course with all of its students.
* Delete a course and automatically delete its students using cascading.
* Use a browser-based frontend to interact with the API.

---

## 📁 Project Structure

```text
project/
│
├── main.py
│
├── core/
│   ├── database.py
│   └── dependances.py
│
├── models/
│   ├── student.py
│   └── course.py
│
├── schemas/
│   ├── student.py
│   └── course.py
│
├── crud/
│   ├── student.py
│   └── course.py
│
├── routers/
│   ├── student.py
│   └── course.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
├── README.md
└── .gitignore
```

> The exact folder names can be changed depending on your implementation.

---

# 🚀 Getting Started

## 1. Clone the project

```bash
git clone <YOUR_REPOSITORY_URL>
cd <PROJECT_FOLDER>
```

---

# 🐍 2. Create a Virtual Environment

It is recommended to use a virtual environment so that the project's packages don't interfere with your global Python installation.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

If PowerShell is being used:

```powershell
.\venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

After activation, you should see something similar to:

```text
(venv) C:\project>
```

---

# 📦 3. Install Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Then install the project dependencies:

```bash
pip install -r requirements.txt
```

If you haven't created `requirements.txt` yet, the main backend packages are:

```text
fastapi
uvicorn[standard]
sqlalchemy
```

You can generate the file from your environment with:

```bash
pip freeze > requirements.txt
```

---

# 🗄️ 4. Database Configuration

The project uses **SQLAlchemy** for database communication.

The database configuration is located in:

```text
core/database.py
```

Example:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

session_db = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

base = declarative_base()
```

This example uses SQLite.

The database file will be created automatically:

```text
students.db
```

---

# 🔌 5. Database Dependency

The database session dependency is located in:

```text
core/dependances.py
```

Example:

```python
from core.database import session_db


def get_db_connection():
    db = session_db()

    try:
        yield db
    finally:
        db.close()
```

This dependency provides a database session to FastAPI endpoints and automatically closes the session after the request.

---

# 👨‍🎓 Student Model

The student model contains:

```text
id
name
email
course_id
gpa
```

Example:

```python
class Student(base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        Integer,
        autoincrement=True,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    course_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("courses.id", ondelete="CASCADE"),
        nullable=False
    )

    gpa: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    course: Mapped["Course"] = relationship(
        back_populates="students"
    )
```

---

# 📚 Course Model

The course model contains:

```text
id
name
students
```

Example:

```python
class Course(base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(
        Integer,
        autoincrement=True,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    students: Mapped[list["Student"]] = relationship(
        back_populates="course",
        cascade="all, delete-orphan"
    )
```

---

# 🔗 Relationship

The relationship between the entities is:

```text
Course 1 ──────────── * Student
```

One course can have many students.

For example:

```text
Python
│
├── Mustafa
├── Ahmed
├── Mohamed
└── Ali
```

Each student belongs to one course.

---

# 🗑️ Cascade Delete

The project uses:

```python
cascade="all, delete-orphan"
```

on the course relationship.

The student foreign key also uses:

```python
ForeignKey(
    "courses.id",
    ondelete="CASCADE"
)
```

Therefore, deleting a course also deletes its students.

For example:

```text
Course: Python

Students:
    Mustafa
    Ahmed
    Ali
```

Deleting Python results in:

```text
Python       → deleted
Mustafa      → deleted
Ahmed        → deleted
Ali          → deleted
```

This prevents orphan students from remaining in the database.

---

# 📋 API

The backend exposes CRUD endpoints for both courses and students.

## Course Endpoints

### Get all courses

```http
GET /courses
```

### Get a course

```http
GET /courses/{course_id}
```

### Create a course

```http
POST /courses
```

Example request:

```json
{
    "name": "Python"
}
```

### Update a course

```http
PUT /courses/{course_id}
```

Example:

```json
{
    "name": "Advanced Python"
}
```

### Delete a course

```http
DELETE /courses/{course_id}
```

---

# 👨‍🎓 Student Endpoints

### Get all students

```http
GET /students
```

### Get a student

```http
GET /students/{student_id}
```

### Create a student

```http
POST /students
```

Example:

```json
{
    "name": "Mustafa",
    "email": "mustafa@example.com",
    "course_id": 1,
    "gpa": 3.5
}
```

### Update a student

```http
PUT /students/{student_id}
```

Example:

```json
{
    "name": "Mustafa Roshdy",
    "email": "mustafa@example.com",
    "course_id": 1,
    "gpa": 3.8
}
```

### Delete a student

```http
DELETE /students/{student_id}
```

---

# 📤 Student Response

When requesting a student, the API can return its related course:

```json
{
    "id": 10,
    "name": "Mustafa",
    "email": "mustafa@example.com",
    "gpa": 3.5,
    "course": {
        "id": 1,
        "name": "Python"
    }
}
```

This is possible because of the SQLAlchemy relationship:

```python
course: Mapped["Course"] = relationship(
    back_populates="students"
)
```

---

# 📥 Course Response

When requesting a course, the API can return all students belonging to that course:

```json
{
    "id": 1,
    "name": "Python",
    "students": [
        {
            "id": 10,
            "name": "Mustafa",
            "email": "mustafa@example.com",
            "gpa": 3.5
        },
        {
            "id": 11,
            "name": "Ahmed",
            "email": "ahmed@example.com",
            "gpa": 3.2
        }
    ]
}
```

This is provided by:

```python
students: Mapped[list["Student"]] = relationship(
    back_populates="course",
    cascade="all, delete-orphan"
)
```

---

# 🌐 Frontend

The project also contains a simple frontend built using:

* HTML
* CSS
* JavaScript
* Fetch API

The frontend communicates with the FastAPI backend through HTTP requests.

```text
                 HTTP Requests
┌──────────────┐                 ┌──────────────┐
│              │    GET/POST     │              │
│   Frontend   │ ──────────────> │   FastAPI    │
│ HTML/CSS/JS  │ <────────────── │   Backend    │
│              │     JSON        │              │
└──────────────┘                 └──────┬───────┘
                                        │
                                        │ SQLAlchemy
                                        ▼
                                ┌──────────────┐
                                │   Database   │
                                └──────────────┘
```

---

# 🖥️ Frontend Features

The frontend provides a user interface for:

### Courses

* Display all courses
* Create a course
* Update a course
* Delete a course
* Display students belonging to a course

### Students

* Display all students
* Create a student
* Update a student
* Delete a student
* Display the student's course

The JavaScript communicates with the API using `fetch()`.

Example:

```javascript
fetch("http://127.0.0.1:8000/students")
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });
```

---

# ▶️ Running the Backend

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

Or:

```bash
python -m uvicorn main:app --reload
```

The backend will normally be available at:

```text
http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

### ReDoc

Open:

```text
http://127.0.0.1:8000/redoc
```

Swagger UI can be used to test all CRUD endpoints without using the frontend.

---

# 🌐 Running the Frontend

If the frontend is inside:

```text
frontend/
```

you can open `index.html` directly in the browser.

Alternatively, use a local development server.

For example, with VS Code, install **Live Server** and open:

```text
frontend/index.html
```

Then start Live Server.

The frontend should communicate with:

```text
http://127.0.0.1:8000
```

---

# 🔐 CORS

If the frontend and backend are running on different origins, configure CORS in `main.py`.

Example:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

For development, `allow_origins=["*"]` is convenient.

For production, it is better to specify the actual frontend origin:

```python
allow_origins=[
    "http://127.0.0.1:5500"
]
```

---

# 🏗️ Application Architecture

The project follows a layered structure:

```text
                    Client
                      │
                      ▼
                  FastAPI
                   Routers
                      │
                      ▼
                    CRUD
                      │
                      ▼
                 SQLAlchemy
                      │
                      ▼
                   Models
                      │
                      ▼
                  Database
```

### `main.py`

Responsible for creating the FastAPI application and registering routers.

### `routers/`

Contains API endpoints.

### `crud/`

Contains database operations such as:

```text
Create
Read
Update
Delete
```

### `schemas/`

Contains Pydantic schemas used for request validation and response serialization.

### `models/`

Contains SQLAlchemy database models.

### `core/`

Contains shared application configuration such as:

* Database connection
* Database session dependency

### `frontend/`

Contains:

```text
index.html
style.css
script.js
```

---

# 📦 Recommended `requirements.txt`

A basic requirements file can contain:

```text
fastapi
uvicorn[standard]
sqlalchemy
```

If you are using additional packages in your project, add them as well.

To generate the exact dependencies from your current virtual environment:

```bash
pip freeze > requirements.txt
```

Then another developer can install them with:

```bash
pip install -r requirements.txt
```

---

# 🧪 Development Workflow

Start the backend:

```bash
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

Test the endpoints through Swagger.

After confirming the API works, open the frontend:

```text
frontend/index.html
```

The frontend sends requests to the FastAPI API.

---

# 🔄 CRUD Workflow

## Create

```text
Frontend
   ↓
POST /students
   ↓
FastAPI
   ↓
Pydantic validation
   ↓
CRUD
   ↓
SQLAlchemy
   ↓
Database
```

## Read

```text
Frontend
   ↓
GET /students
   ↓
FastAPI
   ↓
CRUD
   ↓
Database
   ↓
JSON Response
   ↓
Frontend
```

## Update

```text
Frontend
   ↓
PUT /students/{id}
   ↓
FastAPI
   ↓
CRUD
   ↓
Database
```

## Delete

```text
Frontend
   ↓
DELETE /courses/{id}
   ↓
FastAPI
   ↓
SQLAlchemy
   ↓
Course deleted
   ↓
Students deleted through cascade
```

---

# ⚠️ Common Problems

## `Error loading ASGI app`

If you see:

```text
ERROR: Error loading ASGI app.
Could not import module "main".
```

Make sure you are running Uvicorn from the directory containing `main.py`.

For example:

```text
project/
└── main.py
```

Run:

```bash
uvicorn main:app --reload
```

If `main.py` is inside another package, use the correct module path.

---

## WatchFiles keeps reloading

If you see messages such as:

```text
WatchFiles detected changes
```

while using:

```bash
uvicorn main:app --reload
```

Uvicorn's reload mechanism is detecting file changes.

Make sure your virtual environment is **not located inside a directory being watched in a problematic way**, and avoid modifying files inside the environment while the server is running.

A typical structure is:

```text
project/
├── venv/
├── main.py
├── core/
├── models/
├── schemas/
├── crud/
├── routers/
└── frontend/
```

You can also test without reload:

```bash
uvicorn main:app
```

If the application works without `--reload`, the problem is related to the development file watcher rather than the API itself.

---

# 🛑 Stop the Server

Press:

```text
CTRL + C
```

---

# 📌 Future Improvements

Possible improvements for the project include:

* Authentication and authorization
* User accounts
* Pagination
* Search students
* Search courses
* Filtering by GPA
* Input validation
* Better error handling
* Alembic database migrations
* PostgreSQL support
* Environment variables using `.env`
* Production deployment
* Docker
* Automated tests with Pytest
* Better frontend UI
* Loading states
* Toast notifications
* Confirmation dialogs
* Responsive design

---

# 👨‍💻 Technologies

| Technology | Purpose                           |
| ---------- | --------------------------------- |
| Python     | Backend programming language      |
| FastAPI    | REST API framework                |
| Uvicorn    | ASGI server                       |
| SQLAlchemy | ORM/database access               |
| SQLite     | Development database              |
| Pydantic   | Data validation and serialization |
| HTML       | Frontend structure                |
| CSS        | Frontend styling                  |
| JavaScript | Frontend logic                    |
| Fetch API  | Backend communication             |

---

# 📄 License

This project is for educational and development purposes.

```

This README is designed to match the **FastAPI + SQLAlchemy + CRUD + HTML/CSS/JS** architecture you've been building, rather than documenting only the models.
```
