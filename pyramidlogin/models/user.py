import bcrypt
from typing import Union

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(Text, unique=True)
    password = Column(Text)

    def encode_password(self, password: str) -> None:
        """genera un codigo hash a partir de la pasword ingresada y la guarda en el atributo password"""
        self.password = bcrypt.hashpw(password.encode(
            'utf8'), bcrypt.gensalt()).decode('utf8')

    def decode_pasword(self, password_ingresada: str) -> Union[str, str]:
        """verifica si el password en forma hash es igual al password ingresado """
        if self.password is not None:
            password_actual = self.password.encode('utf8')
            return bcrypt.checkpw(password_ingresada.encode('utf8'), password_actual)

        return False

Index('user_login', User.login, unique=True, mysql_length=255)