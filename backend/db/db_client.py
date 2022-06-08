from routers.schemas import ClientBase
from sqlalchemy.orm.session import Session
from db.models import Client
import datetime
from fastapi import HTTPException, status

def create(db:Session, request: ClientBase):
    new_client = Client(
        name = request.name,
        lastname = request.lastname,
        address = request.address,
        phone = request.phone,
        code = request.code,
        admission_date = request.admission_date,
        payment_date= request.payment_date,
        service_id = request.service_id
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

def get_all(db:Session):
    return db.query(Client).all()

def update(db:Session, client_id: int, request: ClientBase):
    client = db.query(Client).filter(Client.id == client_id).first()
    
    if not client:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f'Client with id {client_id} not found')
    
    client.name = request.name
    client.lastname = request.lastname
    client.address = request.address
    client.phone = request.phone
    client.code = request.code
    client.payment_date= request.payment_date
    client.service_id = request.service_id
    
    db.commit()
    db.refresh(client)
    return client

def delete(db:Session, client_id: int):
    client = db.query(Client).filter(Client.id == client_id).first()

    if not client:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f'Client with id {client_id} not found')
    
    db.delete(client)
    db.commit()
    return 'ok'