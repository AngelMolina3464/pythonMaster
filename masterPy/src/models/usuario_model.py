from sqlmodel import SQLModel ,Field
from typing import Optional

class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    email: str