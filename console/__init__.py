import click
from flask.cli import with_appcontext
from src.models import init_db as cmd_init_db
from src.services.rabbitmq import RabbitMQ

from dotenv import load_dotenv
import os


@click.command(name="init-db")
@with_appcontext
def init_db():
    cmd_init_db()


@click.command(name="env-clear")
@with_appcontext
def cache_env_clear():
    os.environ.clear()
    load_dotenv()
    print("Cache env cleared.")


@click.command("init-queue")
@with_appcontext
def init_queue():
    rabbit = RabbitMQ()
    rabbit.init_queue()
    print("Queue initialized.")
