import bcrypt
import typing

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from ..models import User


class PoliticasAuth(AuthTktAuthenticationPolicy):
    """subclase de AuthTktAuthenticationPolicy, """
    def authenticated_userid(self, request):
        user = request.user
        if user is not None:
            return user.id

def encript_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def decode_password(password: str) -> str:
    db_password = 'password'
    return bcrypt.checkpw(password, db_password)

def get_user(request):
    pass
