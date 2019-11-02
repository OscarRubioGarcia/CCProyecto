from model.Comentario import Comentario


class Noticia:
    def __init__(self, titulo, descripcion, campus, comentarios):
        self.titulo = titulo
        self.descripcion = descripcion
        self.campus = campus
        self.comentarios = comentarios

    listacomentarios = []

    def __dict__(self):
        noticia = {
            "Titulo": self.titulo,
            "Descripcion": self.descripcion,
            "Campus": self.campus,
            "Comentarios": self.comentarios
        }

        return noticia

    def setTitulo(self, titulo):
        self.titulo = titulo

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setCampus(self, campus):
        self.campus = campus

    def addComentario(self, comentario):
        self.comentarios.append(comentario)

    def deleteComentario(self, comentario):
        if comentario in self.comentarios:
            self.comentarios.remove(comentario)

    def addComentarioLista(self, comentario: Comentario):
        if not self._checkCuerpo(comentario.cuerpo):
            raise NoBodyFoundException
        self.listacomentarios.append(comentario)

    def _checkCuerpo(self, cuerpo) -> bool:

        if cuerpo.strip() == "":
            return False

        return True


class NoBodyFoundException(Exception):
    pass
