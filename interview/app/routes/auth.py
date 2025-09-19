from fastapi import APIRouter
from app.schema import UserOUt


router =APIRouter(tags=["auth"],prefix="/auth")




@router.get("/register",response_model=UserOUt)
def register(name: str,password: str):
    
    return {"name":name, "password":password}