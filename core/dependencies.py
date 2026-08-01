
from core.database import session_db

def get_db_connection():
    db=session_db()
    try :
        yield db
        
    finally:
        db.close()