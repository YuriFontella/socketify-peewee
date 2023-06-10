import peewee
from config import Database

db = Database()

class Users(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = db.connect()
