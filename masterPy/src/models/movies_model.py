from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel): 
    id : int 
    title : str
    overview : str
    year: int
    active : bool
    category : Optional[str] = None
    
