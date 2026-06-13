# Personal Task Manager

Internship project using FastAPI, SQLite, and Streamlit.

## Features

- User registration and login
- SQLite database storage
- Create, view, update, delete tasks
- Mark tasks as completed
- Dashboard summary cards
- Search tasks
- Filter by status and priority
- Categories
- Overdue task indicator
- CSV export

## Run Backend

```bash
cd backend
pip install fastapi uvicorn pydantic
uvicorn main:app --reload
```

Open API docs:

```text
http://127.0.0.1:8000/docs
```

## Run Frontend

Open a new terminal:

```bash
cd frontend
pip install streamlit requests pandas
streamlit run app.py
```

## Note

Password hashing is not added because this version is for internship/demo learning only.
