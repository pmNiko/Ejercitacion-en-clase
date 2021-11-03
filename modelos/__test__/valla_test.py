import unittest
from valla import Valla

class TestValla(unittest.TestCase):
    def setUp(self) -> None:
        self.valla = Valla()
    
    def test_LaVallaEstaAlta(self):
        """ Verifica si la valla está alta """
        self.assertTrue(self.valla.alta)


    def test_laVallaPuedeBajarse(self):
        """ Una valla alta puede bajarse """
        self.assertTrue(self.valla.alta)
        
        self.valla.cambiarSuEstado()
        
        self.assertFalse(self.valla.alta)


    def test_laVallaPuedeSubirse(self):
        """ Una valla alta puede bajarse """
        self.valla.cambiarSuEstado()
        
        self.assertFalse(self.valla.alta)
        
        self.valla.cambiarSuEstado()        
        
        self.assertTrue(self.valla.alta)
        
    

if __name__ == '__main__':
    unittest.main()   