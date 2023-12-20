from sqlalchemy import table
from sqlmodel import Relationship, SQLModel, Field
from model.mixins import TimeMixin
from model.user_role import UsersRole
from typing import List, Optional


class Role(SQLModel, TimeMixin, table = True):
    __tablename__ = "role"
    
    id: Optional[ str] = Field(None, primary_key = True, nullable=True)
    role_name: str
    
    users:List["Users"] = Relationship(back_populates="roles", link_model = UsersRole)