from flask import Flask
from console import init_db
from src.config import Config
from src.routes import route
from src.event.scheduler import Scheduler
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(os.environ.get("APP_NAME", "Example App"))

current_state = bool(int(os.environ.get("APP_PRODUCTION", 1)))

config = Config().production_config if current_state else Config().dev_config

app.env = config.ENV

app.register_blueprint(route)

app.cli.add_command(init_db)

Scheduler.start()