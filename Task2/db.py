from sqlalchemy import Column, Integer, String, create_engine, MetaData, Table, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncAttrs

engine = create_async_engine(f"sqlite+aiosqlite:///users.db", echo=True)

metadata = MetaData()

class Base(DeclarativeBase,AsyncAttrs):
    pass

class User_DB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(100))
    email = Column(String(100))

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_name', String(100)),
    Column('email', String(100))
)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

def get_async_session():
    return async_session()
