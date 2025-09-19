from pydantic import BaseModel
from typing import List,Optional



class UserCreate(BaseModel):

    user_id : int
    username: str
    salary: Optional[float] = 0.0

class UserOUt(BaseModel):
    name: str
    password:float

    


