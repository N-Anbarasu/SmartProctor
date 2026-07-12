from app.extensions import db
from flask_login import UserMixin


class Student(db.Model, UserMixin):

    __tablename__ = "students"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    full_name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    register_number = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )


    def __repr__(self):
        return f"<Student {self.full_name}>"