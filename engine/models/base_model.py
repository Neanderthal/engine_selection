import json

from flask import session, jsonify
from peewee import SqliteDatabase, Model

database = SqliteDatabase('my_app.db')

class PeeweeModel(Model):
    class Meta:
        database = database

class BaseModel:
    def __init__(self):
        pass
    def save(self):
        session[__name__] = jsonify(**self.list_of_public())

    def list_of_public(self):
        return {key: str(value) for key, value in self.__dict__.items() if
                   not key.startswith('_')}

    def update(self, data):
        self.__dict__.update(data)

    def load(self):
        self.update(json.loads(session[__name__]))

    def __iter__ (self):
        return self.list_of_public()