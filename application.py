from flask import Flask

from engine.views import engine
from helpers import SimpleJsonEncoder

app = Flask('engine_selection')
app.config.from_object('config')
app.register_blueprint(engine)
app.json_encoder = SimpleJsonEncoder

if __name__ == '__main__':
    app.run()
