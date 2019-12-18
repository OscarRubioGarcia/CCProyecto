from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from flask import Flask
from cassandra.cluster import Cluster
from project.Cache import cache

from project.model.Noticia import Noticia
from project.app import api

KEYSPACE = "noticias"


def create_app():
    app = Flask(__name__)
    cache.init_app(app)
    app.register_blueprint(api)

    # Change to 0.0.0.0 for release
    cluster = Cluster(['127.0.0.1'], port=9042)
    # Change to 192.168.99.100 for test local docker
    # cluster = Cluster(['192.168.99.100'], port=9042)
    session = cluster.connect()

    session.execute(
        """
        CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
        """ % KEYSPACE)

    session = cluster.connect(keyspace=KEYSPACE)

    return app


app = create_app()

if __name__ == '__main__':
    # Change to 0.0.0.0 for release
    connection.setup(['127.0.0.1'], "cqlengine", protocol_version=3)
    # Change to 192.168.99.100 for test local docker
    # connection.setup(['192.168.99.100'], "cqlengine", protocol_version=3)
    sync_table(Noticia)
    app.run(host="0.0.0.0", port=8081, debug=False)
