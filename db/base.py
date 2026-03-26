from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from config import settings

engine = create_engine(settings.DATABASE_URL.replace("+asyncpg", ""), echo=True)

Base = declarative_base()
