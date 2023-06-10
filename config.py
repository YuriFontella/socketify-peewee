from peewee import PostgresqlDatabase

class Database:
    conn = None

    def __init__(self):
        self.connect()

    def connect(self):
        if self.conn is None:
            self.conn = PostgresqlDatabase('blocks', user='postgres', password='123456', host='localhost')

        return self.conn
