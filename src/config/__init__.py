from src.config.dev import DevConfig
from src.config.production import ProductionConfig

class Config:
    def __init__(self) -> None:
        self.dev_config = DevConfig()
        self.production_config = ProductionConfig()