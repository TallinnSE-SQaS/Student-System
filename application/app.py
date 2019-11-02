from typing import Optional

from flask import Flask, render_template, session

from application.users import views as user_views
from application.users.models import User, Role
from application.courses import views as course_views


app = Flask(
    __name__.partition('.')[0],
    static_folder='../static')

# would be private in a real life application
app.secret_key = 'a3ws4e6d5rgt7hy8uj9@#ZXE$VTBYw4es5dr6tfgyih'

app.register_blueprint(user_views.users)
app.register_blueprint(course_views.courses)


@app.route("/")
def home():
    current_user: Optional[User] = session.get('current_user')

    if current_user is not None:
        return {
            Role.Student: user_views.student_home,
            Role.Professor: user_views.professor_home,
            Role.Staff: user_views.staff_home
        }[current_user['role']]()

    return render_template('home.html.j2')
