from fastapi import FastAPI, Depends, HTTPException
from database import models
from database.database import engine, SessionLocal
from sqlalchemy.orm import Session
from exceptions.exception_handler import NoTodoFoundException, no_todo_found_exception_handler
from model.model import TodoModel as TodoMod

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.add_exception_handler(NoTodoFoundException,
                          no_todo_found_exception_handler)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/todo")
async def get_todos(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@app.get("/todo/{todo_id}")
async def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    query_response = db.query(models.Todos).filter(
        models.Todos.id == todo_id).first()

    if query_response is not None:
        return query_response
    else:
        print(f"Todo with id {todo_id} not found")
        raise NoTodoFoundException(todo_id=todo_id)


@app.post("/todo")
async def create_todo(todo: TodoMod, db: Session = Depends(get_db)):
    db_todo = models.Todos(title=todo.title, description=todo.description,
                           priority=todo.priority, complete=todo.complete)

    db.add(db_todo)
    db.commit()
    return {"message": "Todo created successfully"}
