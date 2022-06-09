from ast import In
from .database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    

class Router(Base):
    __tablename__ = 'router'
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String)
    name = Column(String)
    username = Column(String)
    password = Column(String)
    clients = relationship('Client', back_populates='router')


class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    rate= Column(String)
    clients = relationship('Client', back_populates='service')


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lastname = Column(String)
    address = Column(String)
    phone = Column(String)
    code = Column(String)
    admission_date = Column(DateTime)
    payment_date= Column(Integer)
    service_id = Column(Integer, ForeignKey("service.id"))
    router_id = Column(Integer, ForeignKey("router.id"))
    router = relationship('Router', back_populates='clients')
    service = relationship("Service", back_populates='clients')

class InvoicesClient(Base):
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lastname = Column(String)
    address = Column(String)
    phone = Column(String)
    service = Column(String)
    amount = Column(Integer)
    creation_date = Column(DateTime)
    expiration_date = Column(DateTime)
    paid = Column(Boolean, default=False)