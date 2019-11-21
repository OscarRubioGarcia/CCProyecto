class Comentario:

    def __init__(self, cuerpo, usuario, puntuacion):
        self.cuerpo = cuerpo
        self.usuario = usuario
        self.puntuacion = puntuacion

    def __dict__(self):
        comentario = {
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
            'cuerpo': self.cuerpo,
            'usuario': self.usuario,
            'puntuacion': self.puntuacion
        }
