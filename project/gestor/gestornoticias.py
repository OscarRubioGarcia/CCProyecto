from cassandra.cqlengine.query import LWTException

from project.model.Noticia import Noticia


class GestorNoticias(object):
    noticiastest1 = Noticia()
    noticiastest2 = Noticia()

    listanoticias = []
    listanoticiastestapi = [
        noticiastest1,
        noticiastest2,
    ]

    def __init__(self):
        self.listanoticias.clear()
        pass

    def listar(self):
        return Noticia.objects().all()

    def addWithData(self, data):
        news = Noticia.create(titulo=data["titulo"], descripcion=data["descripcion"], campus=data["campus"])
        if not self._checkEnoughData(news):
            raise NotEnoughDataInNews
        return news.save()

    def deleteById(self, data):
        success = "Deleted News with id %s" % data["id"]
        try:
            Noticia.objects(id=data["id"]).if_exists().delete()
        except LWTException as e:
            pass
            success = "No news with id = %s, exist. " % data
        return success

    def getById(self, data):
        try:
            news = Noticia.objects(id=data["id"]).if_exists()
            success = [noticia.get_data() for noticia in news]
        except LWTException as e:
            pass
            success = "No news with id = %s, exist. " % data
        return success

    def addNoticia(self, noticia: Noticia) -> None:
        if not self._checkEnoughData(noticia):
            raise NotEnoughDataInNews
        self.listanoticias.append(noticia)

    def removeNoticia(self, noticia: Noticia) -> None:
        if not self._checkEnoughData(noticia):
            raise NotEnoughDataInNews
        self.listanoticias.remove(noticia)

    def getNoticia(self, id: int) -> Noticia:
        found = None
        for x in self.listanoticias:
            if x.id == id:
                found = x
                break
        if not self._checkEnoughData(found):
            raise NotEnoughDataInNews

        return found

    def _checkEnoughData(self, noticia: Noticia) -> bool:

        if not hasattr(noticia, "id"):
            return False
        if not hasattr(noticia, "titulo"):
            return False
        if not hasattr(noticia, "descripcion"):
            return False
        if not hasattr(noticia, "campus"):
            return False
        if noticia.titulo.__eq__(''):
            return False
        if noticia.descripcion.__eq__(''):
            return False
        if noticia.campus.__eq__(''):
            return False
        return True


class NotEnoughDataInNews(Exception):
    pass
