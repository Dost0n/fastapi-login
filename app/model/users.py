from typing import List, Optional
from sqlalchemy import Column, String, table
from sqlmodel import SQLModel, Field, Relationship
from model.user_role import UsersRole
from model.mixins import TimeMixin


class Users(SQLModel, TimeMixin, table=True):
    __tablename__ = "users"
    
    id : Optional[str] = Field(None, primary_key = True, nullable = False)
    username : str = Field(sa_column=Column("username", String, unique = True))
    email : str = Field(sa_column = Column("email", String, unique = True))
    pasword: str
    
    person_id: Optional[str] = Field(default = None, foreign_key="person.id")
    person: Optional["person"] = Relationship(back_populates="users")
    
    roles: List["Role"] = Relationship(back_populates="users", link_model = UsersRole)