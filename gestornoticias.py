from typing import List

from model.Noticia import Noticia


class GestorNoticias(object):

    listanoticias = []

    def __init__(self):
        self.listanoticias.clear()
        pass

    def addNoticia(self, noticia: Noticia) -> None:
        if not self._checkEnoughData(noticia):
            raise NotEnoughDataInNews
        self.listanoticias.append(noticia)

    def removeNoticia(self, noticia: Noticia) -> None:
        if not self._checkEnoughData(noticia):
            raise NotEnoughDataInNews
        self.listanoticias.remove(noticia)

    def getNoticia(self, tituloNoticia: str) -> Noticia:
        found = None
        for x in self.listanoticias:
            if x.titulo == tituloNoticia:
                found = x
                break

        if not self._checkEnoughData(found):
            raise NotEnoughDataInNews

        return found

    def _checkEnoughData(self, noticia: Noticia) -> bool:

        if not hasattr(noticia, "titulo"):
            return False
        if not hasattr(noticia, "descripcion"):
            return False
        if not hasattr(noticia, "campus"):
            return False
        if noticia.titulo.__eq__("Default"):
            return False
        if noticia.descripcion.__eq__("Default"):
            return False
        if noticia.campus.__eq__("Default"):
            return False
        return True


class NotEnoughDataInNews(Exception):
    pass
