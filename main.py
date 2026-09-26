import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class TaskCreate(BaseModel):
    title: str

@app.get("/")
def home():
    return {"message": "Hello, backend!"}


@app.get("/tasks")
def get_tasks():
    conn = sqlite3.connect("paperpilot.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, title FROM tasks")
    rows = cursor.fetchall()

    conn.close()

    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "title": row[1]
        })

    return result

@app.get("/hello")
def hello():
    return {"message": "你好，这是我的第二个接口"}
@app.post("/tasks")
def create_task(task: TaskCreate):
    conn = sqlite3.connect("paperpilot.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (task.title,)
    )

    conn.commit()

    task_id = cursor.lastrowid

    conn.close()

    return {
        "message": "任务创建成功",
        "task": {
            "id": task_id,
            "title": task.title
        }
    }