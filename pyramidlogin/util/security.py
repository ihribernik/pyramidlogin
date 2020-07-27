import bcrypt
import typing

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from ..models import User


class PoliticasAuth(AuthTktAuthenticationPolicy):
    """subclase de AuthTktAuthenticationPolicy, """

    def authenticated_userid(self, request):
        usuario = request.usuario
        if usuario is not None:
            return usuario.id


def get_user(request):
    usuario_id = request.unauthenticated_userid
    if usuario_id is not None:
        user = request.dbsession.query(User).get(usuario_id)
        return user


def includeme(config):
    settings = config.get_settings()
    authn_policy = PoliticasAuth(
        settings['pyramidlogin.secret'],
        hashalg='sha512',
    )
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.add_request_method(get_user, 'usuario', reify=True)
