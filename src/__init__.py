import os

from flask import Flask
from dotenv import load_dotenv

from console import init_db, cache_env_clear, init_queue
from src.config import Config
from src.routes import route
from src.event.scheduler import Scheduler
from src.event.listener import Listener
from src.services.rabbitmq import RabbitMQ


load_dotenv(override=True)

app = Flask(os.environ.get("APP_NAME", "Example App"))

rabbit = RabbitMQ()

current_state = bool(int(os.environ.get("APP_PRODUCTION", 1)))

current_env = Config().PRODUCTION_CONFIG if current_state else Config().DEV_CONFIG

app.env = current_env.ENV

app.register_blueprint(route)

# app.config.from_object(Config)

app.cli.add_command(init_db)
app.cli.add_command(cache_env_clear)
app.cli.add_command(init_queue)

rabbit.init_queue()

Scheduler.start()
Listener.start()