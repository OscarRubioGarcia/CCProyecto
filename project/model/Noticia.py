from project.model.Comentario import Comentario


class Noticia:

    def __init__(self, id=0, titulo="Default", descripcion="Default", campus="Default"):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.campus = campus
        self.listacomentarios = []

    listacomentarios = []

    def __dict__(self):
        noticia = {
            "Id": self.id,
            "Titulo": self.titulo,
            "Descripcion": self.descripcion,
            "Campus": self.campus,
        }

        return noticia

    def setTitulo(self, titulo):
        self.titulo = titulo

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setCampus(self, campus):
        self.campus = campus

    def addComentarioLista(self, comentario: Comentario):
        if not self._checkCuerpo(comentario.cuerpo):
            raise NoBodyFoundException
        self.listacomentarios.append(comentario)

    def deleteComentarioLista(self, comentario: Comentario):
        if not self._checkCuerpo(comentario.cuerpo):
            raise NoBodyFoundException
        try:
            self.listacomentarios.remove(comentario)
        except ValueError:
            raise ValueError

    def _checkCuerpo(self, cuerpo) -> bool:

        if cuerpo.strip() == "":
            return False

        return True

    def __eq__(self, other):
        if not isinstance(other, Noticia):
            return NotImplemented

        return self.id == other.id and \
               self.titulo == other.titulo and \
               self.descripcion == other.descripcion and \
               self.campus == other.campus

    def serialize(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'campus': self.campus,
            'comentarios': [e.serialize() for e in self.listacomentarios]
        }


class NoBodyFoundException(Exception):
    pass
