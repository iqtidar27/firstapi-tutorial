import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi import APIRouter, Depends, HTTPException, Response, status 
from typing import List
import schema, models, database
from sqlalchemy.orm import Session
from passlib.context import CryptContext
#from database import get_db
from repository import user

router = APIRouter(
    prefix="/user",
    tags=['User']
    )

#pwt_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


#New user creation
@router.post('/', response_model=schema.ShowUser)
def create_user(request: schema.User, db: Session=Depends(database.get_db)):
    return user.create(request, db)

#Query user with their ID
@router.get('/{id}', response_model=schema.ShowUser)
def get_user(id:int, db: Session=Depends(database.get_db)):
    return user.show(id, db)