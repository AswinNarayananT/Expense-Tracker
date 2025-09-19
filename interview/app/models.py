from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum as SAEnum
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime, timezone
import enum

class CategoryEnum(str, enum.Enum):
    Food ="Food"
    Entertainment = "Entertainment"
    Transport ="Transport"
    Utilities ="Utilities"
    Other ="Other"

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    username = Column(String(150), unique=True, nullable=False, index=True)
    salary = Column(Float, default=0.0, nullable=False)
    hashed_password = Column(String(256), nullable=False)

    expenses = relationship("Expense", back_populates="user", cascade="all, delete-orphan")

class Expense(Base):
    __tablename__ = "expenses"

    expense_id  = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(200), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(SAEnum(CategoryEnum), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)

    user = relationship("User", back_populates="expenses")