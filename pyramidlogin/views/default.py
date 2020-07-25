# from pyramid.url import route_path
from pyramid.view import view_config, view_defaults
# from pyramid.security import forget, remember
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPForbidden,
    HTTPNotFound,
)

# from sqlalchemy.exc import DBAPIError

from .. import models

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
        # self.logged_in = request.userid_connected

    @view_config(route_name='home', renderer='../templates/home.jinja2')
    def home(self):
        print('estoy en el home')
        return {}

    @view_config(route_name='login', renderer='../templates/login.jinja2')
    def login(self):
        """ funcion """
        request = self.request
        
        
        usuario = ''
        password = ''
        print(request.POST)
        if 'form.submitted' in request.params:
            usuario = request.POST.get('usuario')
            password = request.POST.get('password')
            
        return {}
