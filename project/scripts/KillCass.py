from cassandra.cluster import Cluster
import uuid
import random



if __name__ == "__main__":
    # Change to 127.0.0.1 for release
    cluster = Cluster(['127.0.0.1'], port=9042)
    # Change to 192.168.99.100 for test local docker
    # cluster = Cluster(['192.168.99.100'], port=9042)
    session = cluster.connect('noticias', wait_for_all_pools=True)

    session.execute('USE noticias')
    session.execute('DROP TABLE noticia')

    session.shutdown()
    cluster.shutdown()