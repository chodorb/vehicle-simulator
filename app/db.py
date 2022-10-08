from pydantic import env_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv('.env')
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
name = os.environ.get("DB_NAME")


DATABASE_URI = "postgresql://{}:{}@postgresdb/{}".format(user,password,name)
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
Base = declarative_base()
