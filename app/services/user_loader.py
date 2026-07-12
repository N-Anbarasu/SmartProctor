from app.extensions import login_manager
from app.models.student import Student
from app.models.teacher import Teacher


@login_manager.user_loader
def load_user(user_id):
    """
    Load user from session.
    Checks both Student and Teacher tables.
    """

    # Try Student first
    student = Student.query.get(int(user_id))

    if student:
        return student

    # Try Teacher
    teacher = Teacher.query.get(int(user_id))

    return teacher