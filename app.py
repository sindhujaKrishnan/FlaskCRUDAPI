import logging
import time
import uuid
from config import DevelopmentConfig
from flask import Flask, g, request

from config import Config
from models.item import db
from routes.item_routes import item_bp
from utils.logger import setup_logging
from utils.response import error
from utils.validators import ValidationException


logger = logging.getLogger(__name__)


# ===========================================
# Application Factory
# ===========================================

def create_app(config_class=Config):

    # Create Flask Application
    app = Flask(__name__)

    # Load Configuration
    app.config.from_object(config_class)

    # Initialize Logging
    setup_logging(app)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(item_bp)

    # =======================================
    # Before Request
    # =======================================

    @app.before_request
    def before_request():

        g.request_id = str(uuid.uuid4())

        g.request_start_time = time.perf_counter()

        logger.info(
            "REQUEST | id=%s | method=%s | path=%s",
            g.request_id,
            request.method,
            request.path
        )

    # =======================================
    # After Request
    # =======================================

    @app.after_request
    def after_request(response):

        request_id = getattr(
            g,
            "request_id",
            "unknown"
        )

        start_time = getattr(
            g,
            "request_start_time",
            None
        )

        duration_ms = 0

        if start_time is not None:

            duration_ms = (
                time.perf_counter()
                - start_time
            ) * 1000

        response.headers[
            "X-Request-ID"
        ] = request_id

        logger.info(
            "RESPONSE | id=%s | method=%s | "
            "path=%s | status=%s | duration_ms=%.2f",
            request_id,
            request.method,
            request.path,
            response.status_code,
            duration_ms
        )

        return response

    # =======================================
    # Validation Exception
    # =======================================

    @app.errorhandler(ValidationException)
    def handle_validation_exception(ex):

        logger.warning(
            "VALIDATION_ERROR | id=%s | %s",
            getattr(
                g,
                "request_id",
                "unknown"
            ),
            str(ex)
        )

        return error(
            message=str(ex),
            status_code=400
        )

    # =======================================
    # 404
    # =======================================

    @app.errorhandler(404)
    def handle_not_found(ex):

        logger.warning(
            "NOT_FOUND | id=%s | method=%s | path=%s",
            getattr(
                g,
                "request_id",
                "unknown"
            ),
            request.method,
            request.path
        )

        return error(
            message="API Endpoint Not Found.",
            status_code=404
        )

    # =======================================
    # 405
    # =======================================

    @app.errorhandler(405)
    def handle_method_not_allowed(ex):

        logger.warning(
            "METHOD_NOT_ALLOWED | id=%s | "
            "method=%s | path=%s",
            getattr(
                g,
                "request_id",
                "unknown"
            ),
            request.method,
            request.path
        )

        return error(
            message="HTTP Method Not Allowed.",
            status_code=405
        )

    # =======================================
    # Global Exception Handler
    # =======================================

    @app.errorhandler(Exception)
    def handle_exception(ex):

        logger.exception(
            "UNHANDLED_EXCEPTION | id=%s",
            getattr(
                g,
                "request_id",
                "unknown"
            )
        )

        return error(
            message="Internal Server Error.",
            status_code=500
        )

    return app


# ===========================================
# Production Application
# ===========================================

app = create_app()


# ===========================================
# Create Database Tables
# ===========================================

with app.app_context():

    db.create_all()

    logger.info(
        "Database initialization completed"
    )


# ===========================================
# Application Startup
# ===========================================

if __name__ == "__main__":

    logger.info(
        "Starting Flask CRUD API"
    )

    app.run(
        debug=app.config["DEBUG"]
    )