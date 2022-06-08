from routers.schemas import ServiceBase
from sqlalchemy.orm.session import Session
from db.models import Service
from fastapi import HTTPException, status


def create(db:Session, request:ServiceBase):
    new_service = Service(
        name=request.name,
        price=request.price,
        rate=request.rate
    )
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service

def get_all(db:Session):
    return db.query(Service).all()

def update(db:Session, service_id:int, request:ServiceBase):
    service= db.query(Service).filter(Service.id ==service_id).first()

    if not service:
        raise HTTPException(status=status.HTTP_404_NOT_FOUND, detail=f'Service with id {service_id} not found')

    service.name= request.name
    service.price= request.price
    service.rate= request.rate
    db.commit()
    db.request(service)
    return service

def delete(db:Session, service_id:int):
    service= db.query(Service).filter(Service.id ==service_id).first()
    
    if not service:
        raise HTTPException(status=status.HTTP_404_NOT_FOUND, detail=f'Service with id {service_id} not found')
    
    db.delete(service)
    db.commit()
    return 'ok'