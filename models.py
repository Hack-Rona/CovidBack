from peewee import *
import datetime

DATABASE = PostgresqlDatabase('users')

class Volunteer(Model):
    name = CharField()
    city = CharField()
    state = CharField()
    zipCode = CharField()
    phoneNumber = CharField(unique = True)
    email = CharField(unique = True)
    cap = IntegerField()
    vacc = BooleanField()
    date = DateField()
    inperson = BooleanField()
    created_at = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = DATABASE
        
class Gethelp(Model):
    name = CharField()
    city = CharField()
    state = CharField()
    zipCode = CharField()
    phoneNumber = CharField(unique = True)
    email = CharField(unique = True)
    reason = Charfield()
    method = Charfield()
    created_at = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Volunteer, Gethelp], safe=True)
    print("TABLES Created")
    DATABASE.close()
