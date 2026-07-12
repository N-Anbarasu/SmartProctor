from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO

# Database
db = SQLAlchemy()

# Database Migration
migrate = Migrate()

# User Authentication
login_manager = LoginManager()

# Real-time Communication
socketio = SocketIO()

login_manager.login_view = "auth.login"
login_manager.login_message = "Please log in to continue."
login_manager.login_message_category = "warning"