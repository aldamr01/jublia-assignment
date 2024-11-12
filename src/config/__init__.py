from src.config.dev import DevConfig
from src.config.production import ProductionConfig
import os

from dotenv import load_dotenv


class Config:
    def __init__(self) -> None:
        self.DEV_CONFIG = DevConfig()
        self.PRODUCTION_CONFIG = ProductionConfig()

    MAIL_SERVER = os.getenv("MAIL_SERVER", "127.0.0.1")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "true").lower() in ["true", "1"]
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL", "false").lower() in ["true", "1"]
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "username")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "secret")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", "noreply@testmail.com")

    RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "127.0.0.1")
    RABBITMQ_USER = os.getenv("RABBITMQ_USER", "rabbitmq")
    RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "rabbitmq")
    RABBITMQ_PORT = os.getenv("RABBITMQ_PORT", "5672")
    RABBITMQ_VHOST = os.getenv("RABBITMQ_VHOST", "/")
