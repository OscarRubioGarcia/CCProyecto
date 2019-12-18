from project.model.Comentario import Comentario
import uuid
from cassandra.cqlengine import columns
from project.model.Base import Base


class Noticia(Base):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    titulo = columns.Text()
    descripcion = columns.Text()
    campus = columns.Text()

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
        raise NoBodyFoundException

    def deleteComentarioLista(self, comentario: Comentario):
        raise NoBodyFoundException

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

    def get_data(self):
        return {
            'id': str(self.id),
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'campus': self.campus
        }


class NoBodyFoundException(Exception):
    pass
