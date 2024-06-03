from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Models import User, Post
from Schemas import UserSchema, UserSchemaResponse
from db import get_db
from main import app


@app.get("/api/users", response_model=list[UserSchemaResponse], tags=['Users'])
async def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@app.post("/api/users", response_model=UserSchemaResponse, tags=['Users'])
async def create_user(body: UserSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(email=body.email).first()

    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    new_user = User(name=body.name, email=body.email, password=body.password, avatar=body.avatar)
    db.add(new_user)
    db.commit()
    print(body)
    return new_user


@app.get("/api/users/{user_id}", tags=['Users'])
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return user


@app.get("/api/posts", tags=['Posts'])
async def get_all_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts


@app.get("/api/users/{post_id}", tags=['Posts'])
async def get_post_by_id(post_id: str, db: Session = Depends(get_db)):
    post = db.query(User).get(post_id)
    if post is None:
        raise HTTPException(status_code=400, detail="Post doesn't exists")
    return post
