from application.app import app
from application.users.models import User
from application.courses.models import Course, CourseDependency


database_data = {
    User: [{"username": "student", "role": 0, "password": "some-password"},
           {"username": "professor", "role": 1, "password": "some-other-password"}],

    Course: [{"name": "Basic Course", "professor": 1, "capacity": 30, "student_count": 20},
             {"name": "Basic Course, filled out", "professor": 1, "capacity": 30, "student_count": 30},
             {"name": "Advanced Course", "professor": 1, "capacity": 30, "student_count": 20}],

    CourseDependency: [{"dependant": 3, "dependee": 1}]
}


def get_flask_test_client():
    app.testing = True
    return app.test_client()


def setup_database():
    for model in (User, Course, CourseDependency):
        model.drop_table()
        model.create_table()
        model.bulk_create([
            model(**data) for data in database_data[model]
        ])


test_client = get_flask_test_client()
setup_database()
