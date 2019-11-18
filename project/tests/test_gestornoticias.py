import unittest

from project.model.Noticia import Noticia
from project.gestor.gestornoticias import GestorNoticias, NotEnoughDataInNews


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.noticiaPrueba = Noticia("Apertura de Nueva Cafeteria", "Nueva cafeteria siendo abierta en...",
                                     "Campus Universitario de Granada")
        self.noticiaVacia = Noticia()
        self.gestorNoticias = GestorNoticias()

    def testTipoCreacion(self):
        self.assertIsInstance(self.gestorNoticias, GestorNoticias, "Tipo de objeto incorrecto, no es del tipo GestorNoticias.")

    def testInsertarNoticia(self):
        self.assertEqual(len(self.gestorNoticias.listanoticias), 0,
                         "Se a generado un gestor de noticias con noticias")
        self.gestorNoticias.addNoticia(self.noticiaPrueba)
        self.assertEqual(len(self.gestorNoticias.listanoticias), 1,
                         "A ocurrido un error al añadir una noticia valida")

    def testInsertarNoticiaNoValida(self):
        self.assertEqual(len(self.gestorNoticias.listanoticias), 0, "Se a generado un gestor de noticias con noticias")
        self.assertRaises(
            NotEnoughDataInNews,
            self.gestorNoticias.addNoticia, self.noticiaVacia)
        self.assertEqual(len(self.gestorNoticias.listanoticias), 0,
                         "A ocurrido un error al añadir una noticia no valida")

    def testEliminarNoticiaValida(self):
        self.assertEqual(len(self.gestorNoticias.listanoticias), 0,
                         "Se a generado un gestor de noticias con noticias")
        self.gestorNoticias.addNoticia(self.noticiaPrueba)
        self.assertEqual(len(self.gestorNoticias.listanoticias), 1,
                         "A ocurrido un error al añadir una noticia valida")

        self.gestorNoticias.removeNoticia(self.noticiaPrueba)
        self.assertEqual(len(self.gestorNoticias.listanoticias), 0,
                         "A ocurrido un error al añadir una noticia no valida")

    def testEliminarNoticiaNoValida(self):
        self.assertEqual(len(self.gestorNoticias.listanoticias), 0,
                         "Se a generado un gestor de noticias con noticias")
        self.gestorNoticias.addNoticia(self.noticiaPrueba)
        self.assertEqual(len(self.gestorNoticias.listanoticias), 1,
                         "A ocurrido un error al añadir una noticia valida")

        self.assertRaises(
            NotEnoughDataInNews,
            self.gestorNoticias.removeNoticia, self.noticiaVacia)
        self.assertEqual(len(self.gestorNoticias.listanoticias), 1,
                         "A ocurrido un error al añadir una noticia no valida")

    def testExcepcionNoticiaNoValida(self):
        self.assertRaises(
            NotEnoughDataInNews,
            self.gestorNoticias.getNoticia, self.noticiaVacia)

    def testGetNoticiaValida(self):
        self.assertEqual(len(self.gestorNoticias.listanoticias), 0,
                         "Se a generado un gestor de noticias con noticias")
        self.gestorNoticias.addNoticia(self.noticiaPrueba)
        self.assertEqual(len(self.gestorNoticias.listanoticias), 1,
                         "A ocurrido un error al añadir una noticia valida")
        found = self.gestorNoticias.getNoticia("Apertura de Nueva Cafeteria")
        self.assertIsInstance(found, Noticia,
                              "Tipo de objeto incorrecto, no es del tipo Noticia.")
        self.assertEqual(found, self.noticiaPrueba)


if __name__ == '__main__':
    unittest.main()
