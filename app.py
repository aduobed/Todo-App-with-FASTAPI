from fastapi import FastAPI, Depends
from exceptions.exception_handler import NoTodoFoundException, no_todo_found_exception_handler
from routers import user, todos
from utils import check_header_token

app = FastAPI()

app.include_router(user.router)
app.include_router(todos.router)

app.add_exception_handler(NoTodoFoundException,
                          no_todo_found_exception_handler)

# Example of using dependencies, tags and headers check in FastAPI
@app.get("/test", tags=["header present test"], dependencies=[Depends(check_header_token.check_token)])
async def test():
    return {"test": "secret header is present"}