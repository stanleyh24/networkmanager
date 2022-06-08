from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.database import get_db
from db import db_client
from typing import List
from .schemas import ClientBase,ClientDisplay


client = APIRouter(
    prefix='/client',
    tags=['client']
)

@client.get('/', response_model=List[ClientDisplay])
def get_all_clients(db: Session= Depends(get_db)):
    return db_client.get_all(db)

@client.post('/new', response_model=ClientDisplay)
def create_service(request: ClientBase, db: Session= Depends(get_db)):
    return db_client.create(db,request)

@client.put('/update/{client_id}', response_model=ClientDisplay)
def delete_client(request: ClientBase,client_id:int , db: Session= Depends(get_db)):
    return db_client.update(db,client_id, request)

@client.delete('/delete/{client_id}')
def delete_client(client_id:int , db: Session= Depends(get_db)):
    return db_client.delete(db,client_id)