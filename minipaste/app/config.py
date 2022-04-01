class Config:
    """Base Config."""


class ProdConfig(Config):
    FLASK_ENV = "production"
    DATABASE_URI = "sqlite:///prod.db"


class DevConfig(Config):
    FLASK_ENV = "development"
    DATABASE_URI = "sqlite:///dev.db"
