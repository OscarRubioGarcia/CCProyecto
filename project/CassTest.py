from cassandra.cluster import Cluster
import uuid
import random



if __name__ == "__main__":
    # Change to 127.0.0.1 for release
    cluster = Cluster(['127.0.0.1'], port=9042)
    # Change to 192.168.99.100 for test local docker
    # cluster = Cluster(['192.168.99.100'], port=9042)
    session = cluster.connect('noticias', wait_for_all_pools=True)

    random.seed(123210912)
    a = "%32x" % random.getrandbits(128)
    rd = a[:12] + '4' + a[13:16] + 'a' + a[17:]
    uuid4 = uuid.UUID(rd)

    print(uuid4)
    session.execute('USE noticias')
    rows = session.execute('SELECT * FROM noticia')
    for row in rows:
        print(row.id, row.titulo, row.descripcion, row.campus)
