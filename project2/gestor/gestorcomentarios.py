from cassandra.cqlengine.query import LWTException, DoesNotExist
import uuid

from project2.model.Comentario import Comentario


class GestorComentarios(object):

    def listar(self):
        return Comentario.objects().all()

    def addWithData(self, data):
        uuidid = uuid.UUID(data["idnoticia"])
        comments = Comentario.create(cuerpo=data["cuerpo"], usuario=data["usuario"], puntuacion=data["puntuacion"],
                                     idnoticia=uuidid)
		
        return comments.save()

    def deleteById(self, data):
        success = "Deleted Comment with id %s" % data["id"]
        try:
            Comentario.objects(id=data["id"]).if_exists().delete()
        except LWTException as e:
            pass
            success = "No comments with id = %s, exist. " % data
        return success

    def getById(self, data):
        try:
            comments = Comentario.objects(id=data["id"]).if_exists()
            success = [comment.get_data() for comment in comments]
        except LWTException as e:
            pass
            success = "No comments with id = %s, exist. " % data
        return success

    def getByIdnoticia(self, data):
        try:
            comments = Comentario.objects.all()
            success = {}
            index = 1
            # very costly
            for comment in comments:
                print(comment.idnoticia)
                if str(comment.idnoticia) == data["idnoticia"]:
                    success[index] = comment.get_data()
                    index = index + 1
        except DoesNotExist as e:
            pass
            success = "No news with idnoticia = %s, exist. " % data
        return success

    def deleteFirst(self):
        success = "Deleted Comment with id "

        for c in Comentario.objects().all():
            success = success + str(c.id)
            c.delete()
            break

        return success

    def _checkEnoughData(self, comentario: Comentario) -> bool:

        if not hasattr(comentario, "cuerpo"):
            return False
        if not hasattr(comentario, "usuario"):
            return False
        if not hasattr(comentario, "puntuacion"):
            return False
        if not hasattr(comentario, "idnoticia"):
            return False
        if comentario.cuerpo.__eq__(''):
            return False
        if comentario.usuario.__eq__(''):
            return False
        if comentario.puntuacion.__eq__(''):
            return False
        return True


class NotEnoughDataInComments(Exception):
    pass
