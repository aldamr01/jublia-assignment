import click
from flask.cli import with_appcontext
from src.models import init_db as cmd_init_db
from dotenv import load_dotenv
import os

@click.command(name='init_db')
@with_appcontext
def init_db():
    cmd_init_db()
    
@click.command(name='cache_env_clear')
@with_appcontext
def cache_env_clear():
    os.environ.clear()
    load_dotenv()
    print("Cache env cleared.")