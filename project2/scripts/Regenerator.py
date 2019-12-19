import uuid
import random

from cassandra.cluster import Cluster

KEYSPACE = "comentarios"

if __name__ == "__main__":
    cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect()

    session.execute(
        """
        CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
        """ % KEYSPACE)

    session = cluster.connect(keyspace=KEYSPACE)
    tableFlag = True
    data = session.execute(""" SELECT * FROM system_schema.tables  WHERE keyspace_name='comentarios'; """)
    for row in data:
        # print(row.keyspace_name)
        if row.keyspace_name == "comentarios":
            tableFlag = False

    if tableFlag:
        session.execute(
            """
            CREATE TABLE Comentario (
             id UUID,
             cuerpo text,
             usuario text,
             puntuacion bigint,
             idnoticia UUID,
             PRIMARY KEY(id)
            );
            """
        )

        # 62b48eec-9dfa-44db-ae95-0211abf54d95
        random.seed(123210912)
        a = "%32x" % random.getrandbits(128)
        rd = a[:12] + '4' + a[13:16] + 'a' + a[17:]
        uuid4 = uuid.UUID(rd)

        session.execute(
            """
            INSERT INTO Comentario(id, cuerpo, usuario, puntuacion, idnoticia) VALUES (uuid(), 'Ejemplo comentario', 'testuser', 100, %s);
            """ % uuid4
        )

        session.execute(
            """
            INSERT INTO Comentario(id, cuerpo, usuario, puntuacion, idnoticia) VALUES (uuid(), 'SampleData','testuser', 100, %s);
            """ % uuid4
        )

    print("Successful Database Regeneration.")
    session.shutdown()
    cluster.shutdown()
