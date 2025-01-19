import sys
sys.path.append("..")

from starlette import status
from starlette.responses import RedirectResponse
from fastapi import APIRouter, Depends, status, Request, Form
from database import models
from database import db_start
from sqlalchemy.orm import Session
from exceptions.exception_handler import NoTodoFoundException
from model.model import TodoModel as TodoMod
from auth.user_jwt_token_generate import get_current_user
from exceptions.user_token_exception import user_exception

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not Found"}},
)

@router.get("/test")
async def test(request: Request):
    return templates.TemplateResponse("todo.html", {"request": request})

# @router.get("/", response_class=HTMLResponse)
# async def get_todo_by_user(user: dict = Depends(get_current_user), db: Session = Depends(db_start.get_db)):
#     if user is None:
#         raise user_exception()

#     query_response = db.query(models.Todos).filter(
#         models.Todos.owner_id == user.get('user_id')).all()

#     if len(query_response) == 0:
#         return {"message": "No todos found for this user"}

#     return query_response

@router.get("/", response_class=HTMLResponse)
async def get_todo_by_user(request: Request, db: Session = Depends(db_start.get_db)):

    todos = db.query(models.Todos).filter(
        models.Todos.owner_id == 1).all()

    return templates.TemplateResponse("todo.html", {"request": request, "todos": todos})


@router.get("/edit-todo/{todo_id}", response_class=HTMLResponse)
async def get_todo_by_id(request: Request,todo_id: int, db: Session = Depends(db_start.get_db)):
    todo = db.query(models.Todos).filter(
        models.Todos.id == todo_id).first()

    if todo is not None:
        return templates.TemplateResponse("edit-todo.html", {"request": request, "todo": todo})
    else:
        print(f"Todo with id {todo_id} not found")
        return {"message": "Todo not found"}


@router.get("/add-todo", response_class=HTMLResponse)
async def get_new_todo(request: Request):
    return templates.TemplateResponse("add-todo.html", {"request": request})


@router.post("/add-todo", response_class=HTMLResponse)
async def create_todo(request: Request,title: str = Form(...), description: str = Form(...), priority: int =
                        Form(...),db: Session = Depends(db_start.get_db)):

    db_todo = models.Todos(title=title, description=description,
                           priority=priority, complete=False, owner_id=1)

    db.add(db_todo)
    db.commit()
    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


@router.post("/edit-todo/{todo_id}", response_class=HTMLResponse)
async def edit_todo(request: Request,todo_id: int, title: str = Form(...), description: str = Form(...), priority: int =
                        Form(...),db: Session = Depends(db_start.get_db)):

    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    todo_model.title = title
    todo_model.description = description
    todo_model.priority = priority


    db.add(todo_model)
    db.commit()
    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


@router.get("/delete/{todo_id}")
async def delete_todo(request: Request,todo_id: int, db: Session = Depends(db_start.get_db)):

    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).filter(models.Todos.owner_id == 1).first()

    if todo_model is None:
        raise RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


    db.query(models.Todos).filter(models.Todos.id == todo_id).delete()
    db.commit()

    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


@router.get("/complete/{todo_id}")
async def complete_todo(request: Request,todo_id: int, db: Session = Depends(db_start.get_db)):

    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    todo_model.complete = not todo_model.complete

    db.add(todo_model)
    db.commit()

    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)