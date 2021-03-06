from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from typing import List

class RouterBase(BaseModel):
    ip : str
    name : str
    username: str
    password : str
    
    class Config():
        orm_mode= True

class RouterDisplay(BaseModel):
    id: int
    ip : str
    name : str
    username: str
    password : str
    
    class Config():
        orm_mode= True


##Services schemas

class ServiceBase(BaseModel):
    name : str
    price : int
    rate : str

    class Config():
        orm_mode= True

class ServiceDisplay(BaseModel):
    id: int
    name : str
    price : int
    rate : str

    class Config():
        orm_mode= True

##Client schema

class ClientBase(BaseModel):
    name : str
    lastname : str
    address : str
    phone : str
    payment_date: int
    service_id : int
    router_id : int

    class Config():
        orm_mode= True

class ClientDisplay(BaseModel):
    id:int
    name : str
    lastname : str
    address : str
    phone : str
    admission_date: datetime
    payment_date: int
    service_id : int
    router_id : int
    class Config():
        orm_mode= True



