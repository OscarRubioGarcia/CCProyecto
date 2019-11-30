import os

from flask import Flask
from flask_restful import Api, abort, reqparse, Resource
from flask import jsonify
from project.gestor.gestornoticias import GestorNoticias, NotEnoughDataInNews

gestorNoticias = GestorNoticias()

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

def abortar_ruta_inexistente(ruta):
    abort(404, message="Error 404. Ruta {} Inexistente".format(ruta))


class Main(Resource):
    def get(self):
        return {'status': 'OK'}


def create_app():
    return app


class News(Resource):
    def get(self, id):
        response = []
        if id is not None:
            try:
                noticia = gestorNoticias.getNoticia(int(id))
            except NotEnoughDataInNews:
                noticia = None
            if noticia is not None:
                response.append(noticia.serialize())
            else:
                response.append({'no news found with id': id})
            return jsonify({'news': response})
        else:
            return jsonify({'news': {'no news found with id': id}})

class NewsList(Resource):
    def get(self):
        response = []
        for n in gestorNoticias.listanoticiastestapi:
            response.append(n.serialize())
        return jsonify({'news': response})


api.add_resource(Main, '/', '/status')
api.add_resource(News, '/news/<id>')
api.add_resource(NewsList, '/news')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
