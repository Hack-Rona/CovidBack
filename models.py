from peewee import *
import datetime

DATABASE = SqliteDatabase('appointments.sqlite')

class County(Model):
    name = CharField()
    url = CharField()
    site = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([County], safe=True)
    print("TABLES Created")
    DATABASE.close()