from src.config.dev import DevConfig
from src.config.production import ProductionConfig
import os

from dotenv import load_dotenv

class Config:
    def __init__(self) -> None:
        self.DEV_CONFIG = DevConfig()
        self.PRODUCTION_CONFIG = ProductionConfig()
            
        
    MAIL_SERVER = os.getenv("MAIL_SERVER", "sandbox.smtp.mailtrap.io")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "true").lower() in ["true", "1"]
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL", "false").lower() in ["true", "1"]
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "0b6b3b80de9def")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "f2d25cc27b329e")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", "noreply@test-jblia.com")
