from typing import Optional

from flask import Flask, render_template, session

from application.users import views
from application.users.models import User, Role

app = Flask(
    __name__.partition('.')[0],
    static_folder='../static')

# would be private in a real life application
app.secret_key = 'a3ws4e6d5rgt7hy8uj9@#ZXE$VTBYw4es5dr6tfgyih'

app.register_blueprint(views.users)


@app.route("/")
def home():
    current_user: Optional[User] = session.get('current_user')

    if current_user is not None:
        return {
            Role.Student: views.student_home,
            Role.Professor: views.professor_home,
            Role.Staff: views.staff_home
        }[current_user['role']]()

    return render_template('home.html.j2')
