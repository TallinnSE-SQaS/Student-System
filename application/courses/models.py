import peewee

from application.db import BaseModel
from application.users.models import User


class Course(BaseModel):
    name = peewee.CharField()
    professor = peewee.ForeignKeyField(User, backref='courses')
    capacity = peewee.IntegerField()

    @property
    def student_count(self):
        return self.enrollments.count()


Course.create_table()


class CourseEnrollment(BaseModel):
    student = peewee.ForeignKeyField(User, backref='courses')
    course = peewee.ForeignKeyField(Course, backref='enrollments')


CourseEnrollment.create_table()


class CourseDependency(BaseModel):
    dependant = peewee.ForeignKeyField(Course, backref='dependees')
    dependee = peewee.ForeignKeyField(Course, backref='dependants')


CourseDependency.create_table()
