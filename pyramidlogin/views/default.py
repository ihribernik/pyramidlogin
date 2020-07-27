from pyramid.httpexceptions import HTTPForbidden, HTTPFound
from pyramid.response import Response
from pyramid.security import remember
from pyramid.view import view_config, view_defaults
from sqlalchemy.exc import DBAPIError

from pyramidlogin.models.user import User

from .. import models  # flake8: noqa

db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""


@view_defaults(renderer='../templates/login.jinja2')
class PyramidLoginViews:
    """Class-based view: para manejar todas las vistas de la aplicacion en una sola clase """

    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='../templates/home.jinja2')
    def home(self):
        usuario = self.request.usuario
        if usuario is None:
            raise HTTPForbidden

        return {}

    @view_config(route_name='login', renderer='../templates/login.jinja2')
    def login(self):
        """ funcion login, realiza validaciones para ver si puede logearse o no en el sistema"""

        proxima_url = self.request.route_url('home')

        mensage = ''
        usuario = ''
        password = ''

        if 'form.submitted' in self.request.params:
            usuario = self.request.POST.get('usuario')
            password = self.request.POST.get('password')
            try:
                usuario_db = self.request.dbsession.query(
                    User).filter_by(login=usuario).first()
            except DBAPIError:
                return Response(db_err_msg, content_type='text/plain', status=500)

            if usuario_db and usuario_db.decode_pasword(password_ingresada=password):

                headers = remember(self.request, usuario_db.id)
                print(f'esto es lo que se manda despues del login {headers}')

                return HTTPFound(location=proxima_url, headers=headers)

            mensage = 'fallo al iniciar session'
            proxima_url = self.request.route_url('login')

        return dict(
            mensage=mensage,
            url=self.request.route_url('login'),
            proxima_url=proxima_url,
            login=usuario,
        )
