from flask import Blueprint, render_template
from flask_login import login_required, current_user


teacher_bp = Blueprint(
    "teacher",
    __name__,
    url_prefix="/teacher"
)


@teacher_bp.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "teacher/dashboard.html",
        user=current_user
    )