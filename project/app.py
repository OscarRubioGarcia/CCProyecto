import os
from functools import wraps

from cassandra.cluster import NoHostAvailable
from flask import Blueprint, Response
import flask
import json

from flask_restful import abort, reqparse
from project.gestor.gestornoticias import GestorNoticias
from cassandra.cqlengine import connection
from project.Cache import cache

gestorNoticias = GestorNoticias()

api = Blueprint("api", __name__)
# Change to 0.0.0.0 for release
try:
    connection.setup(['127.0.0.1'], "cqlengine", protocol_version=3)
except NoHostAvailable:
    pass
# Change to 192.168.99.100
# connection.setup(['192.168.99.100'], "cqlengine", protocol_version=3)
parser = reqparse.RequestParser()

def abortar_ruta_inexistente(ruta):
    abort(404, message="Error 404. Ruta {} Inexistente".format(ruta))


def json_api(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        result = f(*args, **kwargs)
        json_result = to_json(result)
        return Response(response=json_result,
                        status=200,
                        mimetype="application/json")

    return decorated_function


@api.route('/', defaults={"path": ""})
@api.route('/status')
@cache.cached(timeout=50)
def index(path=None):
    return {'status': 'OK'}


@api.route("/news")
@json_api
@cache.cached(timeout=50, key_prefix='all_news')
def get_all():
    news = gestorNoticias.listar()
    return [noticia.get_data() for noticia in news]


@api.route("/news/findById", methods=["POST"])
@json_api
@cache.cached(timeout=50, key_prefix='find_news')
def get_by():
    data = json.loads(flask.request.data)
    news = gestorNoticias.getById(data)
    return news


@api.route("/news/add", methods=["POST"])
@json_api
def add_new():
    data = json.loads(flask.request.data)
    news = gestorNoticias.addWithData(data)
    return news.get_data()


@api.route("/news/deleteById", methods=["DELETE"])
@json_api
def delete_id():
    data = json.loads(flask.request.data)
    news = gestorNoticias.deleteById(data)
    return news


def to_json(data):
    def handler(obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        else:
            raise TypeError('Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj)))

    return json.dumps(data, default=handler)

#if __name__ == '__main__':
#    cache.init_app(app, config=config)
#    with app.app_context():
#        cache.clear()
# port = int(os.environ.get("PORT", 5000))
# app.run(host="0.0.0.0", debug=False)
