from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Timer(BaseModel): 
    id : Optional[int] = None
    module : Optional[str] = None
    date: datetime = datetime.now()
    moduleNumber : int = Field( gt=0)

    
