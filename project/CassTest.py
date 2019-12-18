from cassandra.cluster import Cluster

if __name__ == "__main__":
    # Change to 127.0.0.1 for release
    cluster = Cluster(['127.0.0.1'], port=9042)
    # Change to 192.168.99.100 for test local docker
    # cluster = Cluster(['192.168.99.100'], port=9042)
    session = cluster.connect('noticias', wait_for_all_pools=True)
    session.execute('USE noticias')
    rows = session.execute('SELECT * FROM noticia')
    for row in rows:
        print(row.id, row.titulo, row.descripcion, row.campus)

