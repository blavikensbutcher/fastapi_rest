from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from db import Base, engine


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(50), unique=True)
    password = Column(String(20))
    avatar = Column(String)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    body = Column(String(1500))
    user_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", backref="posts")


Base.metadata.create_all(bind=engine)

