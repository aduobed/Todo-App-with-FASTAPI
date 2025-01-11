import sys
sys.path.append('..')

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import engine, SessionLocal
from database import models, db_start
from model.model import AddressModel as AddressMod
from pydantic import BaseModel
from typing import Optional
from auth.user_jwt_token_generate import get_current_user
from exceptions.user_token_exception import user_exception

router = APIRouter(
    prefix="/address",
    tags=["address"],
    responses={404: {"description": "Not Found"}},
)

@router.post("/")
async def create_address(address: AddressMod, user: dict = Depends(get_current_user), db: Session = Depends(db_start.get_db)):

  if user is None:
    raise user_exception()

  db_address = models.Address(
    address1=address.address1,
    address2=address.address2,
    city=address.city,
    state=address.state,
    country=address.country,
    zip=address.zip)

  db.add(db_address)
  db.flush()

  user_model = db.query(models.Users).filter(models.Users.id == user.get("user_id")).first()
  user_model.address_id = models.Address.id

  db.add(user_model)
  db.commit()

  return {"address": "created"}