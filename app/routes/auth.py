from flask import Blueprint, render_template

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


@auth_bp.route("/login")
def login():
    return render_template("auth/login.html")


@auth_bp.route("/student")
def student_login():
    return render_template("auth/student_login.html")


@auth_bp.route("/teacher")
def teacher_login():
    return render_template("auth/teacher_login.html")