import unittest

from project.model.Noticia import Noticia


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.noticiaPrueba = Noticia()
        self.noticiaPrueba.id = 0
        self.noticiaPrueba.titulo ="Apertura de Nueva Cafeteria"
        self.noticiaPrueba.descripcion = "Nueva cafeteria siendo abierta en..."
        self.noticiaPrueba.campus = "Campus Universitario de Granada"

        self.clonPrueba = Noticia()
        self.clonPrueba.id = 0
        self.clonPrueba.titulo ="Apertura de Nueva Cafeteria"
        self.clonPrueba.descripcion = "Nueva cafeteria siendo abierta en..."
        self.clonPrueba.campus = "Campus Universitario de Granada"

    def testTipoCreacion(self):
        self.assertIsInstance(self.noticiaPrueba, Noticia, "Tipo de objeto incorrecto, no es del tipo Noticia.")

    def testUnicidad(self):
        self.assertIsNot(self.noticiaPrueba, self.clonPrueba, "No pueden existir 2 objetos identicos.")

    def testCambioTitulo(self):
        self.noticiaPrueba.setTitulo("Nueva Noticia")
        self.assertIsInstance(self.noticiaPrueba.titulo, str,
                              "El tipo del campo titulo no es correcto tras ser modificado.")
        self.assertEqual(self.noticiaPrueba.titulo, "Nueva Noticia",
                         "El atributo Titulo no fue modificado correctamente.")

    def testCambioDescripcion(self):
        self.noticiaPrueba.setDescripcion("Nueva Descripcion de Noticia")
        self.assertIsInstance(self.noticiaPrueba.descripcion, str,
                              "El tipo del campo descripcion no es correcto tras ser modificado.")
        self.assertEqual(self.noticiaPrueba.descripcion, "Nueva Descripcion de Noticia",
                         "El atributo descripcion no fue modificado correctamente.")

    def testCambioCampus(self):
        self.noticiaPrueba.setCampus("Nuevo Campus")
        self.assertIsInstance(self.noticiaPrueba.campus, str,
                              "El tipo del campo campus no es correcto tras ser modificado.")
        self.assertEqual(self.noticiaPrueba.campus, "Nuevo Campus",
                         "El atributo campus no fue modificado correctamente.")

    '''
    def testInsertarComentarioEnListaComentariosNoticia(self):
        self.assertEqual(0, len(self.noticiaPrueba.listacomentarios),
                         "La noticia ya tiene comentarios (De alguna forma).")
        self.noticiaPrueba.addComentarioLista(self.comentarioPrueba)
        self.assertEqual(1, len(self.noticiaPrueba.listacomentarios),
                         "No se ha agregado un comentario a la noticia correctamente.")

    def testEliminarComentarioEnListaComentariosNoticia(self):
        self.noticiaPrueba.addComentarioLista(self.comentarioPrueba)
        self.assertEqual(1, len(self.noticiaPrueba.listacomentarios),
                         "No se ha agregado un comentario a la noticia correctamente.")
        self.noticiaPrueba.deleteComentarioLista(self.comentarioPrueba)
        self.assertEqual(0, len(self.noticiaPrueba.listacomentarios),
                         "No se ha eliminado un comentario existente de la lista correctamente.")

    def testValueError(self):
        self.assertRaises(
            ValueError,
            self.noticiaPrueba.deleteComentarioLista, self.comentarioPruebaInexsistente)
    '''

if __name__ == '__main__':
    unittest.main()
