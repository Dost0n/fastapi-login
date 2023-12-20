from sqlalchemy import Enum
from sqlmodel import SQLModel, Field, Relationship
from model.mixins import TimeMixin
from typing import Optional
from datetime import date


class Sex(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class Person(SQLModel, TimeMixin, table = True):
    __tablename__ = "person"
    
    id: Optional[str] = Field(None, primary_key = True, nullable = False)
    name: str
    birthday: date
    sex: Sex
    profile: str
    phone_number: str
    
    users: Optional['Users'] = Relationship(
        sa_relationship_kwargs={'uselist':False}, back_populates = 'person ')
    