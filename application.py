from flask import Flask
from peewee import SqliteDatabase

from engine.views import engine

app = Flask('engine_selection')
app.config.from_object('config')
app.register_blueprint(engine)

db = SqliteDatabase('engine.db')
db.connect()

if __name__ == '__main__':
    app.run()
