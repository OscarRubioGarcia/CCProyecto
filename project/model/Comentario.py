class Comentario:

    def __init__(self, id=0, cuerpo="Default", usuario="Default", puntuacion=101):
        self.id = id
        self.cuerpo = cuerpo
        self.usuario = usuario
        self.puntuacion = puntuacion

    def __dict__(self):
        comentario = {
            "Id" : self.id,
            "Cuerpo": self.cuerpo,
            "Usuario": self.usuario,
            "Puntuacion": self.puntuacion,
        }

        return comentario

    def setCuerpo(self, cuerpo):
        self.cuerpo = cuerpo

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setPuntuacion(self, puntuacion):
        self.puntuacion = puntuacion

    def serialize(self):
        return {
            'id': self.id,
            'cuerpo': self.cuerpo,
            'usuario': self.usuario,
            'puntuacion': self.puntuacion
        }
