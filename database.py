# SQLAlchemy usage: It allows developers to work with databases using familiar Python objects and syntax, reducing the need to
# write and manage raw SQL queries.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#The ORM component maps Python classes to database tables and instances of those classes to rows in the tables

SQLALCHEMY_DATABASE_URL = "sqlite:///./data.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread" :False})

Session_local = sessionmaker(bind = engine, autocommit = False, autoflush = False)

Base = declarative_base()

def get_db():
    db = Session_local()
    try:
        yield db
    finally:
        db.close()
