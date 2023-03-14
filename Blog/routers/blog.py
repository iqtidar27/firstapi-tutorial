#import sys
#sys.path.append("..") #Kuttar Baccha
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi import APIRouter, Depends, HTTPException, Response, status 
from typing import List
import schema, models, database, oauth2
from sqlalchemy.orm import Session
from repository import blog
#from database import get_db


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
    )

#Create post
@router.post('/')
def create(request: schema.Blog, db: Session=Depends(database.get_db), current_user: schema.User=Depends(oauth2.get_current_user)):
    return blog.create(request, db)

#Show the all the blogs already created
@router.get('/', response_model=List[schema.ShowBlog])
def all(db: Session = Depends(database.get_db), current_user: schema.User=Depends(oauth2.get_current_user)):
    #blogs = db.query(models.Blog).all()
    return blog.get_all(db)

#Update Blogs
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schema.UpdateBlog, db:Session = Depends(database.get_db), current_user: schema.User=Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)

#Query the Blog with their ID
@router.get('/{id}', response_model=schema.ShowBlog)
def show(id,  response: Response, db: Session = Depends(database.get_db), current_user: schema.User=Depends(oauth2.get_current_user)):
    return blog.show(id, db)

@router.delete('/{id}')
def delete(id, db:Session=Depends(database.get_db), current_user: schema.User=Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)