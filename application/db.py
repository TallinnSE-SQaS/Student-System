from application import settings

from peewee import SqliteDatabase, Model, AutoField


db = SqliteDatabase(settings.get_environment()['db_name'])


class BaseModel(Model):
    pk = AutoField()  # primary key

    class Meta:
        database = db
