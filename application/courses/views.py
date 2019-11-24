from typing import Optional, List, Set

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
        pending_dependencies = set()

        if current_user is not None:
            current_user = User.get_by_id(current_user['id'])
            is_enrolled = CourseEnrollment.select() \
                .where(CourseEnrollment.student == current_user,
                       CourseEnrollment.course == course) \
                .count() != 0

            if not is_enrolled:
                pending_dependencies = cross_check_dependencies(current_user, course)

        return render_template(
            'courses/course_view.html.j2',
            course=course, is_enrolled=is_enrolled, current_user=current_user,
            pending_dependencies=[pd.name for pd in pending_dependencies])

    else:
        return '', 404


@courses.route('/<int:id>/enroll', methods=['POST'])
def course_enroll(id):
    course: Course = Course.select().where(Course.pk == id).first()
    user: Optional[User] = User.select().where(User.pk == session['current_user']['id']).first()

    if user is None:
        flash('You must be logged in to enroll into a course.', 'error')
        return redirect(url_for('home'))

    pending_dependencies = cross_check_dependencies(user, course)

    if course.student_count >= course.capacity:
        flash("This course has reached max capacity.", 'error')

    elif pending_dependencies:
        course_names: List[str] = [pd.name for pd in pending_dependencies]
        flash(
            "You must complete the course{} '{}' first."
                .format('s' if len(course_names) != 1 else '',
                        ', '.join(course_names)))

    else:
        enrollment = CourseEnrollment(student=user, course=course)
        enrollment.save()

    return redirect(url_for('home'))


def cross_check_dependencies(student: User, course: Course) -> Set[Course]:
    student_courses = set(ce.course for ce in student.courses)
    dependee_courses = set(cd.dependee for cd in course.dependees)

    return dependee_courses - (student_courses & dependee_courses)
