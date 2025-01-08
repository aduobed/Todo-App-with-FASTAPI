from fastapi import FastAPI
from exceptions.exception_handler import NoTodoFoundException, no_todo_found_exception_handler
from routers import user, todos

app = FastAPI()

app.include_router(user.router)
app.include_router(todos.router)

app.add_exception_handler(NoTodoFoundException,
                          no_todo_found_exception_handler)
