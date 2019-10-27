from flask import Blueprint, render_template, request, session, flash, redirect

from .models import User
from application.courses.models import CourseEnrollment, Course


users = Blueprint('users', __name__, url_prefix='/users')


@users.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    select = User.select().where(User.username == username)
    flash_msg = ('Invalid credentials.', 'error')

    if select.count() != 0:
        u: User = select.first()

        if u.password == password:
            session['current_user'] = {'id': u.pk, 'role': u.role}
            flash_msg = ('Welcome back!',)

    flash(*flash_msg)

    return redirect('/')


@users.route('/logout')
def logout():
    session.pop('current_user', None)
    flash('Logged out successfully.')
    return redirect('/')


def student_home():
    courses_enrolled_in = CourseEnrollment.select().where(
        CourseEnrollment.student == session['current_user']['id'])
    return render_template('users/student_home.html.j2', courses=enumerate(courses_enrolled_in))


def professor_home():
    return render_template('users/professor_home.html.j2')


def staff_home():
    return render_template('users/staff_home.html.j2')
