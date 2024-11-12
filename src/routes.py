from flask import Blueprint
from src.controllers.event_broadcast import event_broadcast

# main blueprint to be registered with application
route = Blueprint("web", __name__)

# register user with api blueprint
route.register_blueprint(event_broadcast, url_prefix="/")
