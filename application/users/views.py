from flask import Blueprint, render_template


users = Blueprint('users', __name__, url_prefix='users/')


@users.route('/', methods=['GET'])
def index():
    pass


def student_home():
    return render_template('student_home.html.j2')


def professor_home():
    return render_template('professor_home.html.j2')


def staff_home():
    return render_template('staff_home.html.j2')
