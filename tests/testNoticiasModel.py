import unittest

from model.Noticia import Noticia

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.noticiaPrueba = Noticia("Apertura de Nueva Cafeteria", "Nueva cafeteria siendo abierta en...",
                                     "Campus Universitario de Granada", ["Comentario1", "Comentario2"])
        self.clonPrueba = Noticia("Apertura de Nueva Cafeteria", "Nueva cafeteria siendo abierta en...",
                                     "Campus Universitario de Granada", ["Comentario1", "Comentario2"])

    def testTipoCreacion(self):
        self.assertIsInstance(self.noticiaPrueba, Noticia, "Tipo de objeto incorrecto, no es del tipo Noticia.")

    def testUnicidad(self):
        self.assertIsNot(self.noticiaPrueba, self.clonPrueba, "No pueden existir 2 objetos identicos.")

    def testCambioTitulo(self):
        self.noticiaPrueba.setTitulo("Nueva Noticia")
        self.assertIsInstance(self.noticiaPrueba.titulo, str, "El tipo del campo titulo no es correcto tras ser modificado.")
        self.assertEqual(self.noticiaPrueba.titulo, "Nueva Noticia", "El atributo Titulo no fue modificado correctamente.")

    def testCambioDescripcion(self):
        self.noticiaPrueba.setDescripcion("Nueva Descripcion de Noticia")
        self.assertIsInstance(self.noticiaPrueba.descripcion, str, "El tipo del campo descripcion no es correcto tras ser modificado.")
        self.assertEqual(self.noticiaPrueba.descripcion, "Nueva Descripcion de Noticia", "El atributo descripcion no fue modificado correctamente.")

    def testCambioCampus(self):
        self.noticiaPrueba.setCampus("Nuevo Campus")
        self.assertIsInstance(self.noticiaPrueba.campus, str, "El tipo del campo campus no es correcto tras ser modificado.")
        self.assertEqual(self.noticiaPrueba.campus, "Nuevo Campus", "El atributo campus no fue modificado correctamente.")

    def testInsertarComentarioEnNoticia(self):
        self.noticiaPrueba.addComentario("Nuevo Comentario")
        self.assertIn("Nuevo Comentario", self.noticiaPrueba.comentarios,
                      "No se ha agregado un comentario a la noticia correctamente.")

    def testEliminarComentarioDeNoticia(self):
        self.assertEqual(len(self.noticiaPrueba.comentarios), 2,
                         "No se han creado los comentarios correctamente.")
        self.noticiaPrueba.deleteComentario("Comentario Inexistente")
        self.assertEqual(len(self.noticiaPrueba.comentarios), 2, "Un error ocurrio al eliminar un comentario inexistente")
        self.noticiaPrueba.deleteComentario("Comentario1")
        self.assertNotIn("Comentario1", self.noticiaPrueba.comentarios,
                         "El comentario especificado no ha sido eliminado correctamente.")

if __name__ == '__main__':
    unittest.main()
