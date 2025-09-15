from sqlalchemy.ext.asyncio import create_async_engine, async_session
from sqlalchemy.orm import declarative_base, sessionmaker



DATABASE_URL = "postgresql+asyncpg//postgres:aswinnt0017@localhost:5174/demo"


AsyncSessionLocal =create_async_engine(DATABASE_URL, echo= True, future=True)

Base =declarative_base()





