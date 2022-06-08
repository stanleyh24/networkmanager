from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.database import get_db
from db import db_router
from typing import List
from .schemas import RouterBase, RouterDisplay


router = APIRouter(
    prefix='/router',
    tags=['router']
)


@router.get('')
def get_all_routers(db:Session= Depends(get_db)):
    return db_router.get_all(db)

@router.post('/new', response_model=RouterDisplay)
def create_router(request: RouterBase, db: Session= Depends(get_db)):
    return db_router.create(db, request)


@router.put('/update/{router_id}', response_model=RouterDisplay)
def delete_router(request: RouterBase,router_id:int , db: Session= Depends(get_db)):
    return db_router.update(db,router_id, request)

@router.delete('/delete/{router_id}')
def delete_router(request: RouterBase,router_id:int , db: Session= Depends(get_db)):
    return db_router.delete(db,router_id)