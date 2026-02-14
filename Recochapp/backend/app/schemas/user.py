from typing import Optional
from pydantic import BaseModel, EmailStr

# Propiedades compartidas
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    full_name: Optional[str] = None

# Propiedades para recibir vía API en creación
class UserCreate(UserBase):
    email: EmailStr
    password: str
    full_name: str

# Propiedades para devolver vía API
class User(UserBase):
    id: int
    is_superuser: bool

    class Config:
        from_attributes = True