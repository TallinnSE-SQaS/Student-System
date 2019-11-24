from typing import Optional

from flask import Blueprint, render_template, session, redirect, url_for, flash

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
        has_completed_dependencies = False

        if current_user is not None:
            current_user = User.get_by_id(current_user['id'])
            is_enrolled = CourseEnrollment.select() \
                .where(CourseEnrollment.student == current_user,
                       CourseEnrollment.course == course) \
                .count() != 0

            if not is_enrolled:
                has_completed_dependencies = cross_check_dependencies(current_user, course)

        return render_template(
            'courses/course_view.html.j2',
            course=course, is_enrolled=is_enrolled, current_user=current_user,
            has_completed_dependencies=has_completed_dependencies)

    else:
        return '', 404


@courses.route('/<int:id>/enroll', methods=['POST'])
def course_enroll(id):
    course: Course = Course.select().where(Course.pk == id).first()
    user: Optional[User] = User.select().where(User.pk == session['current_user']['id']).first()

    if user is None:
        flash('You must be logged in to enroll into a course.', 'error')
        redirect(url_for('home'))

    if course.student_count < course.capacity:
        enrollment = CourseEnrollment(student=user, course=course)
        enrollment.save()
        course.student_count += 1
        course.save()

    else:
        flash("You cannot enroll into this course. It has reached max capacity.", 'error')

    return redirect(url_for('home'))


def cross_check_dependencies(student: User, course: Course) -> bool:
    student_courses = [ce.course for ce in student.courses]
    dependee_courses = [cd.dependee for cd in course.dependees]
    print(student_courses, dependee_courses)

    if len(dependee_courses) > 0:
        return all(dc in student_courses for dc in dependee_courses)

    else:
        return True  # no dependees -> can enroll
