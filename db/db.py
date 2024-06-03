import os
from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import dotenv
dotenv.load_dotenv()


url_object = URL.create(
    "postgresql+psycopg2",
    username=os.environ.get('DB_USERNAME'),
    password=os.environ.get('DB_PASSWORD'),
    host="localhost",
    database=os.environ.get('DB_NAME'),
)


engine = create_engine(url_object, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
