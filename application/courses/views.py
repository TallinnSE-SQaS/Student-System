from typing import Optional

from flask import Blueprint, render_template, session, redirect, url_for

from .models import Course, CourseEnrollment
from application.users.models import User


courses = Blueprint('courses', __name__, url_prefix='/courses')


@courses.route('/')
def home():
    all_courses = Course.select()
    return render_template('courses/home.html.j2', courses=all_courses)


@courses.route('/<int:id>')
def course_view(id):
    course: Optional[Course] = Course.select().where(Course.pk == id).first()

    if course is not None:
        current_user = session.get('current_user')
        is_enrolled = False

        if current_user is not None:
            is_enrolled = CourseEnrollment.select() \
                .where(CourseEnrollment.student == current_user['id'],
                       CourseEnrollment.course == course) \
                .count() != 0

        return render_template(
            'courses/course_view.html.j2',
            course=course, is_enrolled=is_enrolled, current_user=current_user)

    else:
        return '', 404


@courses.route('/<int:id>/enroll', methods=['POST'])
def course_enroll(id):
    course: Course = Course.select().where(Course.pk == id).first()
    user: User = User.select().where(User.pk == session['current_user']['id']).first()

    enrollment = CourseEnrollment(student=user, course=course)
    enrollment.save()
    course.student_count += 1
    course.save()

    return redirect(url_for('home'))
