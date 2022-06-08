from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.database import get_db
from db import db_service
from typing import List
from .schemas import ServiceBase, ServiceDisplay


service = APIRouter(
    prefix='/service',
    tags=['service']
)

@service.get('/')
def get_all_services(db: Session= Depends(get_db)):
    return db_service.get_all(db)

@service.post('/new', response_model=ServiceDisplay)
def create_service(request: ServiceBase, db: Session= Depends(get_db)):
    return db_service.create(db,request)

@service.put('/update/{service_id}', response_model=ServiceDisplay)
def delete_router(request: ServiceBase,service_id:int , db: Session= Depends(get_db)):
    return db_service.update(db,service_id, request)

@service.delete('/delete/{service_id}')
def delete_router(request: ServiceBase,service_id:int , db: Session= Depends(get_db)):
    return db_service.delete(db,service_id)