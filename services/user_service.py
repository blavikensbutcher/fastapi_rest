from sqlalchemy import create_engine, Integer, String, ForeignKey, select, Text, and_, desc, func
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship

#
# def create_user(fullname):
#     new_user = User(fullname=fullname)
#     session.add(new_user)
#     session.commit()
#     return new_user
#
#
# def create_post(title, body, user_id):
#     new_post = Post(title=title, body=body, user_id=user_id)
#     session.add(new_post)
#     session.commit()
#     return new_post
#
#
# def get_all_users():
#     answer = {}
#     stmt = select(User)
#     result = session.execute(stmt)
#     for user in result.scalars():
#         answer[user.id] = user.fullname
#     return answer
#
