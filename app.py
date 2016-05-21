from flask import Flask

from engine.views import engine

app = Flask('engine_selection')
app.config.from_object('config')
app.register_blueprint(engine)

if __name__ == '__main__':
    app.run()
