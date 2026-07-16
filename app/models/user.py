from datetime import datetime
from app.extensions import db
from flask_login import UserMixin


class User(db.Model, UserMixin):

    __tablename__ = "users"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )


    password_hash = db.Column(
        db.String(255),
        nullable=False
    )


    role = db.Column(
        db.String(20),
        nullable=False
    )


    is_active = db.Column(
        db.Boolean,
        default=True
    )


    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


    def __repr__(self):
        return f"<User {self.email}>"