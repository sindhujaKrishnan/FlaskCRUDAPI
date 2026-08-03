import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging(app):

    log_directory = app.config.get(
        "LOG_DIRECTORY",
        "logs"
    )

    os.makedirs(
        log_directory,
        exist_ok=True
    )

    log_file = os.path.join(
        log_directory,
        app.config.get(
            "LOG_FILE",
            "app.log"
        )
    )

    log_level_name = app.config.get(
        "LOG_LEVEL",
        "INFO"
    ).upper()

    log_level = getattr(
        logging,
        log_level_name,
        logging.INFO
    )

    formatter = logging.Formatter(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    )

    # Root Logger
    root_logger = logging.getLogger()

    root_logger.setLevel(log_level)

    # Prevent duplicate handlers
    root_logger.handlers.clear()

    # Console Handler
    console_handler = logging.StreamHandler()

    console_handler.setLevel(log_level)

    console_handler.setFormatter(formatter)

    root_logger.addHandler(
        console_handler
    )

    # File Handler
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=app.config.get(
            "LOG_MAX_BYTES",
            5 * 1024 * 1024
        ),
        backupCount=app.config.get(
            "LOG_BACKUP_COUNT",
            5
        ),
        encoding="utf-8"
    )

    file_handler.setLevel(
        log_level
    )

    file_handler.setFormatter(
        formatter
    )

    root_logger.addHandler(
        file_handler
    )

    # Flask Logger
    app.logger.handlers.clear()

    app.logger.propagate = True

    app.logger.setLevel(
        log_level
    )

    app.logger.info(
        "Logging initialized. Log file: %s",
        log_file
    )