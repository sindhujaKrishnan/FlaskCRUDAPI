import os


class Config:

    BASE_DIR = os.path.abspath(
        os.path.dirname(__file__)
    )

    # =========================================
    # Flask
    # =========================================

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "development-secret-key"
    )

    DEBUG = False
    TESTING = False

    # =========================================
    # SQLAlchemy
    # =========================================

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # =========================================
    # JSON
    # =========================================

    JSON_SORT_KEYS = False

    # =========================================
    # Logging
    # =========================================

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    LOG_DIRECTORY = os.path.join(
        BASE_DIR,
        "logs"
    )

    LOG_FILE = "app.log"

    LOG_MAX_BYTES = 5 * 1024 * 1024
    LOG_BACKUP_COUNT = 5


# =============================================
# Development
# =============================================

class DevelopmentConfig(Config):

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///"
        + os.path.join(
            Config.BASE_DIR,
            "inventory.db"
        )
    )


# =============================================
# Testing
# =============================================

class TestConfig(Config):

    TESTING = True
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///:memory:"
    )

    LOG_LEVEL = "WARNING"


# =============================================
# Production
# =============================================

class ProductionConfig(Config):

    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL"
    )

    @classmethod
    def validate(cls):

        if not cls.SECRET_KEY:
            raise RuntimeError(
                "SECRET_KEY environment variable is required."
            )

        if not cls.SQLALCHEMY_DATABASE_URI:
            raise RuntimeError(
                "DATABASE_URL environment variable is required."
            )
        