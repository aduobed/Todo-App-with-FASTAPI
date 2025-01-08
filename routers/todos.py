import sys
sys.path.append("..")

from fastapi import APIRouter, Depends, status
from database import models
from database import db_start
from sqlalchemy.orm import Session
from exceptions.exception_handler import NoTodoFoundException
from model.model import TodoModel as TodoMod
from auth.user_jwt_token_generate import get_current_user
from exceptions.user_token_exception import user_exception

router = APIRouter()

@router.get("/todo/")
async def get_todo_by_user(user: dict = Depends(get_current_user), db: Session = Depends(db_start.get_db)):
    if user is None:
        raise user_exception()

    query_response = db.query(models.Todos).filter(
        models.Todos.owner_id == user.get('user_id')).all()

    if len(query_response) == 0:
        return {"message": "No todos found for this user"}

    return query_response


@router.get("/todo/{todo_id}")
async def get_todo_by_id(todo_id: int,user: dict = Depends(get_current_user), db: Session = Depends(db_start.get_db)):
    query_response = db.query(models.Todos).filter(
        models.Todos.owner_id == user.get('user_id')
    ).filter(
        models.Todos.id == todo_id).first()

    if query_response is not None:
        return query_response
    else:
        print(f"Todo with id {todo_id} not found")
        raise NoTodoFoundException(todo_id=todo_id)


@router.post("/todo/")
async def create_todo(todo: TodoMod, user: dict = Depends(get_current_user) ,db: Session = Depends(db_start.get_db)):

    if user is None:
        raise user_exception()

    db_todo = models.Todos(title=todo.title, description=todo.description,
                           priority=todo.priority, complete=todo.complete, owner_id=user.get('user_id'))

    db.add(db_todo)
    db.commit()
    return {"message": "Todo created successfully", "status_code": status.HTTP_201_CREATED}


@router.put("/todo/{todo_id}")
async def update_todo(todo_id: int, todo: TodoMod, user: dict = Depends(get_current_user), db: Session = Depends(db_start.get_db)):
    if user is None:
        raise user_exception()

    db_todo = db.query(models.Todos).filter(
        models.Todos.owner_id == user.get("user_id")).filter(
            models.Todos.id == todo_id).first()

    if db_todo is not None:
        db_todo.title = todo.title
        db_todo.description = todo.description
        db_todo.priority = todo.priority
        db_todo.complete = todo.complete

        db.add(db_todo)
        db.commit()
        return {"message": "Todo updated successfully"}
    else:
        raise NoTodoFoundException(todo_id=todo_id)


@router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int,user: dict = Depends(get_current_user), db: Session = Depends(db_start.get_db)):
    if user is None:
        raise user_exception()

    db_todo = db.query(models.Todos).filter(
        models.Todos.owner_id == user.get("user_id")).filter(
            models.Todos.id == todo_id).first()

    if db_todo is None:
        raise NoTodoFoundException(todo_id=todo_id)

    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}
