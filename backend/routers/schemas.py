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

