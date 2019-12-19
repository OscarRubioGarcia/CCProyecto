from cassandra.cluster import Cluster
import uuid
import random

if __name__ == "__main__":
    cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect('comentarios', wait_for_all_pools=True)
    # session.execute('DROP TABLE comentarios.comentario ;')

    random.seed(123210912)
    a = "%32x" % random.getrandbits(128)
    rd = a[:12] + '4' + a[13:16] + 'a' + a[17:]
    uuid4 = uuid.UUID(rd)

    session.execute('USE comentarios')
    rows = session.execute('SELECT * FROM comentario')
    for row in rows:
        print(row.id, row.cuerpo, row.usuario, row.puntuacion, row.idnoticia)

    session.shutdown()
    cluster.shutdown()