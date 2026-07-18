from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import login_user, logout_user

from werkzeug.security import generate_password_hash

from app.extensions import db

from app.models.user import User
from app.models.student import Student
from app.models.teacher import Teacher

from app.services.auth_service import authenticate_user


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


# ==================================================
# LOGIN SELECTION
# ==================================================

@auth_bp.route("/login")
def login():

    return render_template(
        "auth/login.html"
    )


# ==================================================
# STUDENT LOGIN
# ==================================================

@auth_bp.route("/student-login", methods=["GET", "POST"])
def student_login():

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password")

        user = authenticate_user(
            email,
            password
        )

        if user is None:

            flash(
                "Incorrect email or password.",
                "danger"
            )

            return render_template(
                "auth/student_login.html"
            )

        if user.role != "student":

            flash(
                "This account is not registered as a student.",
                "warning"
            )

            return render_template(
                "auth/student_login.html"
            )

        login_user(user)

        flash(
            "Welcome back!",
            "success"
        )

        return redirect(
            url_for("student.dashboard")
        )

    return render_template(
        "auth/student_login.html"
    )


# ==================================================
# TEACHER LOGIN
# ==================================================

@auth_bp.route("/teacher-login", methods=["GET", "POST"])
def teacher_login():

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password")

        user = authenticate_user(
            email,
            password
        )

        if user is None:

            flash(
                "Incorrect email or password.",
                "danger"
            )

            return render_template(
                "auth/teacher_login.html"
            )

        if user.role != "teacher":

            flash(
                "This account is not registered as a teacher.",
                "warning"
            )

            return render_template(
                "auth/teacher_login.html"
            )

        login_user(user)

        flash(
            "Welcome back!",
            "success"
        )

        return redirect(
            url_for("teacher.dashboard")
        )

    return render_template(
        "auth/teacher_login.html"
    )


# ==================================================
# STUDENT REGISTER
# ==================================================

@auth_bp.route("/student-register", methods=["GET", "POST"])
def student_register():

    if request.method == "POST":

        full_name = request.form.get("full_name").strip()
        email = request.form.get("email").strip().lower()
        password = request.form.get("password")
        register_number = request.form.get("register_number").strip()
        department = request.form.get("department").strip()

        if len(password) < 8:

            flash(
                "Password must contain at least 8 characters.",
                "danger"
            )

            return redirect(
                url_for("auth.student_register")
            )

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:

            flash(
                "An account with this email already exists.",
                "warning"
            )

            return redirect(
                url_for("auth.student_register")
            )

        existing_student = Student.query.filter_by(
            register_number=register_number
        ).first()

        if existing_student:

            flash(
                "Register number already exists.",
                "warning"
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
            "Student account created successfully. You can now sign in.",
            "success"
        )

        return redirect(
            url_for("auth.student_login")
        )

    return render_template(
        "auth/student_register.html"
    )


# ==================================================
# TEACHER REGISTER
# ==================================================

@auth_bp.route("/teacher-register", methods=["GET", "POST"])
def teacher_register():

    if request.method == "POST":

        name = request.form.get("name").strip()
        email = request.form.get("email").strip().lower()
        password = request.form.get("password")
        class_id = request.form.get("class_id").strip()

        if len(password) < 8:

            flash(
                "Password must contain at least 8 characters.",
                "danger"
            )

            return redirect(
                url_for("auth.teacher_register")
            )

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:

            flash(
                "An account with this email already exists.",
                "warning"
            )

            return redirect(
                url_for("auth.teacher_register")
            )

        teacher = Teacher.query.filter_by(
            class_id=class_id
        ).first()

        if teacher:

            flash(
                "Class ID already exists.",
                "warning"
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
            "Teacher account created successfully. You can now sign in.",
            "success"
        )

        return redirect(
            url_for("auth.teacher_login")
        )

    return render_template(
        "auth/teacher_register.html"
    )


# ==================================================
# LOGOUT
# ==================================================

@auth_bp.route("/logout")
def logout():

    logout_user()

    flash(
        "You have been logged out successfully.",
        "success"
    )

    return redirect(
        url_for("home.home")
    )