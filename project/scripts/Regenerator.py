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
        session.execute(
            """
            INSERT INTO Noticia(id, titulo,descripcion,campus) VALUES (uuid(), 'SampleData en UGR','Hubo SampleData','UGR');
            """
        )
        session.execute(
            """
            INSERT INTO Noticia(id, titulo,descripcion,campus) VALUES (uuid(), 'SampleData','SampleData','CampusExample');
            """
        )

    print("Successful Database Regeneration.")
    session.shutdown()
    cluster.shutdown()
