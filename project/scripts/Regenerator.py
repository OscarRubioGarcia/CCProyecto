import uuid
import random

from cassandra.cluster import Cluster

KEYSPACE = "noticias"

if __name__ == "__main__":
    cluster = Cluster(['127.0.0.1'], port=9042)
    # Change to 192.168.99.100 for test local docker
    # cluster = Cluster(['192.168.99.100'], port=9042)
    session = cluster.connect()

    session.execute(
        """
        CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
        """ % KEYSPACE)

    session = cluster.connect(keyspace=KEYSPACE)
    tableFlag = True
    data = session.execute(""" SELECT * FROM system_schema.tables  WHERE keyspace_name='noticias'; """)
    for row in data:
        # print(row.keyspace_name)
        if row.keyspace_name == "noticias":
            tableFlag = False

    if tableFlag:
        session.execute(
            """
            CREATE TABLE Noticia (
             id UUID,
             titulo text,
             descripcion text,
             campus text,
             PRIMARY KEY(id)
            );
            """
        )

        random.seed(123210912)
        a = "%32x" % random.getrandbits(128)
        rd = a[:12] + '4' + a[13:16] + 'a' + a[17:]
        uuid4 = uuid.UUID(rd)

        session.execute(
            """
            INSERT INTO Noticia(id, titulo,descripcion,campus) VALUES (%s, 'SampleData en UGR','Hubo SampleData','UGR');
            """ % uuid4
        )
        session.execute(
            """
            INSERT INTO Noticia(id, titulo,descripcion,campus) VALUES (uuid(), 'SampleData','SampleData','CampusExample');
            """
        )

    print("Successful Database Regeneration.")
    session.shutdown()
    cluster.shutdown()
