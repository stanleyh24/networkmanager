from unicodedata import name
from routers.schemas import RouterBase
from sqlalchemy.orm.session import Session
from db.models import Router
import datetime
from fastapi import HTTPException, status

def create(db:Session, request: RouterBase):
    new_router = Router(
        ip = request.ip,
        name = request.name,
        username = request.username,
        password = request.password
    )
    db.add(new_router)
    db.commit()
    db.refresh(new_router)
    return new_router

def get_all(db:Session):
    return db.query(Router).all()

def update(db:Session, router_id: int, request: RouterBase):
    router = db.query(Router).filter(Router.id == router_id).first()
    
    if not router:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f'Router with id {router_id} not found')
    
    router.ip = request.ip
    router.name = request.name
    router.username = request.username
    router.password = request.password
    db.commit()
    db.refresh(router)
    return router

def delete(db:Session, router_id: int):
    router = db.query(Router).filter(Router.id == router_id).first()

    if not router:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f'Router with id {router_id} not found')
    
    db.delete(router)
    db.commit()
    return 'ok'