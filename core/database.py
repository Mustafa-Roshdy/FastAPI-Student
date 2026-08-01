from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

from core.config import settings

engine = create_engine(settings.DATABASE)

base =declarative_base()

session_db=sessionmaker(bind=engine)