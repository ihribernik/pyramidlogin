import bcrypt
import typing

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from ..models import User


class PoliticasAuth(AuthTktAuthenticationPolicy):
    """subclase de AuthTktAuthenticationPolicy, """
    def authenticated_userid(self, request):
        user = request.body
        if user is not None:
            return None

def encript_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def decode_password(password: str) -> str:
    db_password = 'password'
    return bcrypt.checkpw(password, db_password)

def get_user(request):
    usuario = request.body
    print(f'bodi en get_ user {usuario}')
    if usuario is not None:
        return usuario.id


def includeme(config):
    settings = config.get_settings()
    authn_policy = PoliticasAuth(
        settings['pyramidlogin.secret'],
        hashalg='sha512',
    )
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.add_request_method(get_user, 'usuario', reify=True)