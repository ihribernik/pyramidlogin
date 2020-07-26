# from pyramid.url import route_path
from pyramidlogin.models.user import User
from pyramid.view import view_config, view_defaults
# from pyramid.security import forget, remember
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPForbidden,
    HTTPNotFound,
)

# from sqlalchemy.exc import DBAPIError
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

        return {}

    @view_config(route_name='login', renderer='../templates/login.jinja2')
    def login(self):
        """ funcion """

        proxima_url = self.request.params.get('next', self.request.referrer)
        if not proxima_url:
            proxima_url = self.request.route_url('login')
        usuario = ''
        password = ''
        if 'form.submitted' in self.request.params:
            usuario = self.request.POST.get('usuario')
            password = self.request.POST.get('password')
            usuario_db = self.request.dbsession.query(
                User).filter_by(login=usuario).first()
            print(usuario_db)
            if usuario_db and User.decode_pasword(password_ingresada=password):
                print('el usuario y la password coinciden')

        return {}
