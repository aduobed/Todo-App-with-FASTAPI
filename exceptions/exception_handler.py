from fastapi import FastAPI, HTTPException, Request
from starlette.responses import JSONResponse


class NoTodoFoundException(Exception):
    def __init__(self, todo_id: int):
        self.todo_id = todo_id


app = FastAPI()


@app.exception_handler(NoTodoFoundException)
async def no_todo_found_exception_handler(request: Request, exc: NoTodoFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"Todo with id {exc.todo_id} not found"}
    )