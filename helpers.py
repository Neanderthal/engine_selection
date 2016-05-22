import decimal
import flask
import simplejson as json
from werkzeug.wrappers import Response


class SimpleJsonEncoder(flask.json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Response):
            return str(obj)
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return json.dumps(obj, use_decimal=True)
        return super(SimpleJsonEncoder, self).default(obj)
