from enum import IntEnum, unique

import peewee

from application.db import BaseModel


@unique
class Role(IntEnum):
    Student = 0
    Professor = 1
    Staff = 2


class User(BaseModel):
    username = peewee.CharField()
    password = peewee.CharField()
    role = peewee.IntegerField()


User.create_table()
