import os
from functools import wraps

from cassandra.cluster import NoHostAvailable
from flask import Blueprint, Response
import flask
import json

from flask_restful import abort, reqparse
from project2.gestor.gestorcomentarios import GestorComentarios
from cassandra.cqlengine import connection
from project2.Cache import cache

gestorComentarios = GestorComentarios()

api = Blueprint("api-comments", __name__)
try:
    connection.setup(['127.0.0.1'], "cqlengine", protocol_version=3)
except NoHostAvailable:
    pass
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
@cache.cached(timeout=60)
def index_comments(path=None):
    return {'status': 'OK'}


@api.route("/comments")
@json_api
@cache.cached(timeout=60, key_prefix='all_comments')
def get_all_comments():
    comments = gestorComentarios.listar()
    return [comentario.get_data() for comentario in comments]


@api.route("/comments/findById", methods=["POST"])
@json_api
@cache.cached(timeout=60, key_prefix='find_comments')
def get_by_comments():
    data = json.loads(flask.request.data)
    comments = gestorComentarios.getById(data)
    return comments


@api.route("/comments/findByIdnoticia", methods=["POST"])
@json_api
@cache.cached(timeout=60, key_prefix='find_noticia_comments')
def get_by_news_comments():
    data = json.loads(flask.request.data)
    comments = gestorComentarios.getByIdnoticia(data)
    return comments


@api.route("/comments/add", methods=["POST"])
@json_api
def add_new_comments():
    data = json.loads(flask.request.data)
    comments = gestorComentarios.addWithData(data)
    return comments.get_data()


@api.route("/comments/deleteById", methods=["DELETE"])
@json_api
def delete_id_comments():
    data = json.loads(flask.request.data)
    news = gestorComentarios.deleteById(data)
    return news


# Test service only
@api.route("/comments/deleteRandom", methods=["DELETE"])
@json_api
def delete_id_comments_random():
    news = gestorComentarios.deleteFirst()
    return news


def to_json(data):
    def handler(obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        else:
            raise TypeError('El objeto con typo %s y valor %s no se puede serializar a JSON' % (type(obj), repr(obj)))

    return json.dumps(data, default=handler)

