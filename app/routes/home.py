from flask import Blueprint, render_template

home_bp = Blueprint(
    "home",
    __name__
)


@home_bp.route("/")
def home():
    return render_template("public/index.html")


@home_bp.route("/features")
def features():
    return render_template("public/features.html")


@home_bp.route("/about")
def about():
    return render_template("public/about.html")


@home_bp.route("/contact")
def contact():
    return render_template("public/contact.html")