from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import login_user, logout_user

from app.extensions import db

from app.models.user import User
from app.models.student import Student
from app.models.teacher import Teacher

from app.services.auth_service import authenticate_user
from werkzeug.security import generate_password_hash



auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)



# ---------------- LOGIN SELECTION ----------------

@auth_bp.route("/login")
def login():

    return render_template(
        "auth/login.html"
    )



# ---------------- STUDENT LOGIN ----------------

@auth_bp.route("/student-login", methods=["GET","POST"])
def student_login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")


        user = authenticate_user(
            email,
            password
        )


        if user and user.role == "student":

            login_user(user)

            return redirect(
                url_for("student.dashboard")
            )


        flash(
            "Invalid student login details",
            "danger"
        )


    return render_template(
        "auth/student_login.html"
    )



# ---------------- TEACHER LOGIN ----------------

@auth_bp.route("/teacher-login", methods=["GET","POST"])
def teacher_login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")


        user = authenticate_user(
            email,
            password
        )


        if user and user.role == "teacher":

            login_user(user)

            return redirect(
                url_for("teacher.dashboard")
            )


        flash(
            "Invalid teacher login details",
            "danger"
        )


    return render_template(
        "auth/teacher_login.html"
    )



# ---------------- STUDENT REGISTER ----------------

@auth_bp.route("/student-register", methods=["GET","POST"])
def student_register():

    if request.method == "POST":

        full_name = request.form.get("full_name")
        email = request.form.get("email")
        password = request.form.get("password")
        register_number = request.form.get("register_number")
        department = request.form.get("department")


        existing = User.query.filter_by(
            email=email
        ).first()


        if existing:

            flash(
                "Email already registered",
                "danger"
            )

            return redirect(
                url_for("auth.student_register")
            )



        user = User(

            email=email,

            password_hash=generate_password_hash(password),

            role="student"

        )


        db.session.add(user)

        db.session.commit()



        student = Student(

            full_name=full_name,

            email=email,

            register_number=register_number

        )


        db.session.add(student)

        db.session.commit()



        flash(
            "Student account created successfully",
            "success"
        )


        return redirect(
            url_for("auth.student_login")
        )



    return render_template(
        "auth/student_register.html"
    )



# ---------------- TEACHER REGISTER ----------------

@auth_bp.route("/teacher-register", methods=["GET","POST"])
def teacher_register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        class_id = request.form.get("class_id")


        existing = User.query.filter_by(
            email=email
        ).first()


        if existing:

            flash(
                "Email already registered",
                "danger"
            )

            return redirect(
                url_for("auth.teacher_register")
            )



        user = User(

            email=email,

            password_hash=generate_password_hash(password),

            role="teacher"

        )


        db.session.add(user)

        db.session.commit()



        teacher = Teacher(

            name=name,

            email=email,

            class_id=class_id

        )


        db.session.add(teacher)

        db.session.commit()



        flash(
            "Teacher account created successfully",
            "success"
        )


        return redirect(
            url_for("auth.teacher_login")
        )



    return render_template(
        "auth/teacher_register.html"
    )



# ---------------- LOGOUT ----------------

@auth_bp.route("/logout")
def logout():

    logout_user()

    return redirect(
        url_for("home.home")
    )