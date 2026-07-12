from flask import Flask

from config import Config

from app.extensions import (
    db,
    migrate,
    login_manager,
    socketio
)


def create_app(config_class=Config):
    """
    Application Factory
    Creates and configures the Flask application.
    """

    app = Flask(__name__)

    # Load Configuration
    app.config.from_object(config_class)

    # Initialize Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    socketio.init_app(app)

    # Load Flask-Login User Loader
    from app.services import user_loader

    # Import Blueprints
    from app.routes.home import home_bp
    from app.routes.auth import auth_bp
    from app.routes.student import student_bp
    from app.routes.teacher import teacher_bp
    from app.routes.exam import exam_bp
    from app.routes.monitor import monitor_bp
    from app.routes.report import report_bp

    # Register Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(teacher_bp)
    app.register_blueprint(exam_bp)
    app.register_blueprint(monitor_bp)
    app.register_blueprint(report_bp)

    return app