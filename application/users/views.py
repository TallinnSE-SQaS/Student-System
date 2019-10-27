from flask import Blueprint, render_template, request, session, flash, redirect

from .models import User


users = Blueprint('users', __name__, url_prefix='/users')


@users.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    cursor = User.select().where(User.username == username).execute()

    try:
        u: User = cursor.iterate()

        if u.password == password:
            session['current_user'] = {'id': u.pk, 'role': u.role}
            flash('Welcome back!')

        else:
            flash('Invalid credentials.', 'error')

    except StopIteration:
        flash('No such user.', 'error')

    return redirect('/')


@users.route('/logout')
def logout():
    session.pop('current_user', None)
    flash('Logged out successfully.')
    return redirect('/')


def student_home():
    return render_template('users/student_home.html.j2')


def professor_home():
    return render_template('users/professor_home.html.j2')


def staff_home():
    return render_template('users/staff_home.html.j2')
