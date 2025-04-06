from dotenv import load_dotenv
import os
# Configuracion con el modelo de SQL nuevo #

from sqlmodel import create_engine, Session

load_dotenv()
url_conn = f"mysql+pymysql://{os.getenv('USER_SQL')}:{os.getenv('PASSWORD_SQL')}@localhost/{os.getenv('DB_NAME')}"


engine = create_engine(url_conn, echo=True)

def get_session(): 
    with Session(engine) as session : 
        yield session
        
        
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
"""
# Configuracion con el modelo de SQL Antiguo#
DATABASE_URL = "mysql+asyncmy://root:bored34sql@localhost/pyBD"
engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

"""
