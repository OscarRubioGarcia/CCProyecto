import uuid
from cassandra.cqlengine import columns
from project2.model.Base import Base


class Comentario(Base):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    cuerpo = columns.Text()
    usuario = columns.Text()
    puntuacion = columns.BigInt()
    idnoticia = columns.UUID(default=uuid.uuid4)

    def __dict__(self):
        comentario = {
            "Id" : str(self.id),
            "Cuerpo": self.cuerpo,
            "Usuario": self.usuario,
            "Puntuacion": str(self.puntuacion),
            "Idnoticia": str(self.idnoticia),
        }

        return comentario

    def setCuerpo(self, cuerpo):
        self.cuerpo = cuerpo

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setPuntuacion(self, puntuacion):
        self.puntuacion = puntuacion

    def get_data(self):
        return {
            'id': str(self.id),
            'cuerpo': self.cuerpo,
            'usuario': self.usuario,
            'puntuacion': str(self.puntuacion),
            'idnoticia': str(self.idnoticia)
        }

    def __eq__(self, other):
        if not isinstance(other, Comentario):
            return NotImplemented

        return self.id == other.id and \
               self.cuerpo == other.cuerpo and \
               self.usuario == other.usuario and \
               self.puntuacion == other.puntuacion and \
               self.idnoticia == other.idnoticia
