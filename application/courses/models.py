import peewee

from application.db import BaseModel
from application.users.models import User


class Course(BaseModel):
    name = peewee.CharField()
    professor = peewee.ForeignKeyField(User, backref='courses')
    capacity = peewee.IntegerField()
    student_count = peewee.IntegerField()


Course.create_table()


class CourseEnrollment(BaseModel):
    student = peewee.ForeignKeyField(User, backref='courses')
    course = peewee.ForeignKeyField(Course, backref='enrollments')


CourseEnrollment.create_table()
