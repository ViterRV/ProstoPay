from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine('sqlite:///users.db', echo=True)

class Base(DeclarativeBase):
    pass

class User_DB(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key= True, autoincrement=True)
    user_name = Column(String(100))
    email = Column(String(100))

Base.metadata.create_all(bind=engine)
Session = sessionmaker(autoflush=False, bind=engine)
session = Session()