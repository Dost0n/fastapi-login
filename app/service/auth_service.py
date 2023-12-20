import base64
from uuid import uuid4
from schema import RegisterSchema
from passlib.context import CryptContext
from datetime import datetime
from model import Person, Users, UsersRole
from repository.role import RoleRepository
from repository.base_repo import BaseRepo
from repository.users import UsersRepository
from fastapi import HTTPException
from repository.person import PersonRepository

pwd_context = CryptContext(schemas=["bcrypt"], deprecated = "auto")


class AuthService:
    
    @staticmethod
    async def register_service(register:RegisterSchema):
        
        _person_id = str(uuid4())
        _users_id = str(uuid4())
        
        
        birth_date = datetime.strftime(register.birth, "%d-%m-%Y")
        
        
        with open("./media/avatar.png", "rb") as f:
            image_str = base64.b64decode(f.read())
        image_str = "data:image;base64," + image_str.decode('utf-8')
        
        _person = Person(id=_person_id,
                        name = register.name,
                        birth = register.birth,
                        sex = register.sex,
                        profile="",
                        phone_number = register.phone_number)
        _users = Users(id = _users_id,
                       name = register.name,
                       username=register.username,
                       email = register.email,
                       password = pwd_context(register.password),
                       person_id = _person_id
                       )
        
        _role = await RoleRepository.find_by_role_name("user")
        _users_role = UsersRole(users_id = _users_id, role_id = _role)
         
        _username = await UsersRepository.find_by_email(register.username)
        
        if __username:
            raise HTTPException(status_code=400, detail = "Userbane altead axi")
        
        
        
##24.22