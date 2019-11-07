import os

from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
from model import Noticia

app = Flask("DashBoard")
api = Api(app)
parser = reqparse.RequestParser()

def abortar_ruta_inexistente(ruta):
    abort(404, message="Error 404. Ruta {} Inexistente".format(ruta))

class Main(Resource):
    def get(self):
        return {'status':'OK'}


api.add_resource(Main,'/','/status')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port, debug=False)
