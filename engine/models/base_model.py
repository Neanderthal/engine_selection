import simplejson as json

from peewee import SqliteDatabase, Model

database = SqliteDatabase('my_app.db')


class PeeweeModel(Model):
    class Meta:
        database = database


class BaseModel:
    def __init__(self):
        pass

    def save(self, session):
        session[type(self).__name__] = json.dumps(dict(self.list_of_public()), use_decimal=True)

    def list_of_public(self):
        return {key: value for key, value in self.__dict__.items() if
                not key.startswith('_')}.items()

    def update(self, data):
        self.__dict__.update(
            {key: value for key, value in data if key in self.__dict__})

    def load(self, session):
        if(session.get(type(self).__name__)):
            vars = json.loads(session.get(type(self).__name__), use_decimal=True)
            self.update(vars)
            pass

    def __iter__(self):
        return self.list_of_public()
