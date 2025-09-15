from sqlalchemy import column,integer, String,Enum as SAEnum, Float,Integer,ForeignKey,DateTime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship
import enum
from datetime import datetime, timezone


from database import Base

class Category(enum.Enum):
    Food ="food"
    Entertainment = "Entertainmaent"
    Transport ="Transport"
    Utilities ="Utilities"
    Other ="Other"





class User(Base):
    __tablename__ = "users"
    user_id = column(Integer, primary_key=True, index=True,auto_increment=True)
    username = column(String,index=True, nullable=True)
    salary = column(Float,nullable=True)

    expense =relationship("users", foreign_keys="Expenses.id",back_populates="user")




class Expenses(Base):
    __tablename__ = "expense"

    expense_id  =column(Integer,primary_key=True, auto_increment=True)
    user_id =column(Integer,ForeignKey("Users.user_id"))
    name =column(str,nullable=True)
    amount = column(Float,nullable=True)
    category = column(String,SAEnum(Category))
    created_at =column(DateTime,default=datetime.now(timezone.utc))

    user =relationship("expense",foreign_keys=["expense_id"],back_populates="expenses")