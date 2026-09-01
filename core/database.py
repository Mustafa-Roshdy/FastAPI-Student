from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

from core.config import settings

engine = create_engine(
    settings.sync_database_url, 
    pool_pre_ping=True,  # Checks if Neon connection is alive before executing queries
    pool_recycle=300     # Recycles idle pooler connections every 5 minutes
)

base =declarative_base()

session_db=sessionmaker(autocommit=False, autoflush=False, bind=engine)