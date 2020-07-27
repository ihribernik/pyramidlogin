import argparse
import sys
import datetime

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from .. import models


def setup_models(dbsession):
    """
    Add or update models / fixtures in the database.

    """
    user1 = models.user.User()
    user1.login = 'ihribernik'
    user1.encode_password('MiPasswordUltraSegura')
    user1.email = 'cihribernik@gmail.com'
    user1.fecha_registro = datetime.date.today()

    user2 = models.user.User()
    user2.login = 'admin'
    user2.encode_password('admin')
    user2.email = 'admin@admin.com'
    user2.fecha_registro = datetime.date.today()

    dbsession.add(user1)
    dbsession.add(user2)


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_uri',
        help='Configuration file, e.g., development.ini',
    )
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env['request'].tm:
            dbsession = env['request'].dbsession
            setup_models(dbsession)
    except OperationalError:
        print('''
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
            ''')
