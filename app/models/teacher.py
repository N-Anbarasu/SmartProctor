from app.extensions import db
from flask_login import UserMixin


class Teacher(db.Model, UserMixin):

    __tablename__ = "teachers"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    class_id = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )


    def __repr__(self):
        return f"<Teacher {self.name}>"