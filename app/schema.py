from typing import TypeVar, Optional
import logging
from pydantic import BaseModel, validator
import re
from fastapi import HTTPException
from model.person import Sex

T = TypeVar('T')


logger = logging.getLogger(__name__)


class RegisterSchema(BaseModel):
    username : str
    email : str
    name : str
    password:str
    phone_number: str
    birth: str
    sex: Sex
    profile: str = "base64"
    
    
    @validator("phone_number")
    def phone_validation(cls, v):
        logger.debug(f"phone in 2 validation : {v}")
        
        
        regex = r"^[\+]?[(]?[0-9]{4}[)]?[-\s.]?[0-9]{4}[-\s\.]?[0-9]{4,6}$"
        if v and not re.search(regex, v, re.I):
            raise HTTPException(status_code=400, detail = {"status":"Bad Request", "message":"Invalid input phone"})
        
        return v
    
    @validator
    def sex_validation(cls, v):
        if hasattr(Sex, v) is False:
            raise HTTPException(status_code=400, detail={"status":"Bad Request", "message":"Invalid input sex"})
        return v
    
    

class LoginSchema(BaseModel):
    username: str
    password: str
    
    
class ForgotPasswordSchema(BaseModel):
    email: str
    new_password: str
    

class DetailSchema(BaseModel):
    status: str
    message: str
    result: Optional[T] = None
    
    
class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T]= None
    