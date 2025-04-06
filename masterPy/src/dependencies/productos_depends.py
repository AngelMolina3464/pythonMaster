
# metodo Nuevo #
from typing import Annotated
from sqlmodel import Session as SessionSQL
from src.database.config import get_session
from fastapi import Depends

        
        
Session_depends = Annotated [SessionSQL, Depends(get_session)]