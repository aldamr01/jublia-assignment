import click
from flask.cli import with_appcontext
from src.models import init_db as cmd_init_db

@click.command(name='init-db')
@with_appcontext
def init_db():
    cmd_init_db()