from fastapi import FastAPI
from database import models
from database.database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def create_db():
    return {"database": "created"}
