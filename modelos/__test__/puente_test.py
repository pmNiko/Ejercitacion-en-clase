import unittest
from puente import Puente

class TestPuente(unittest.TestCase):
    def setUp(self) -> None:
        self.puente = Puente(12)
    
    def test_elPuenteTieneLaVallaAlta(self):
        """ Verifica si la valla está alta """
        self.assertTrue(self.puente.vallaAlta())
        
    def test_elPuenteBajaLaValla(self):
        """ El puente puede bajar la valla """
        self.assertTrue(self.puente.vallaAlta())
        
        self.puente.bajarValla()

        self.assertFalse(self.puente.vallaAlta())
        
    def test_elPuenteBajaSuVallaBaja(self):
        """ Si el puente intenta bajar su valla estando baja 
        no modifica el estado """
        self.puente.bajarValla()
        
        self.assertFalse(self.puente.vallaAlta())
        
        self.puente.bajarValla()
        
        self.assertFalse(self.puente.vallaAlta())
        
    def test_elPuenteSubeSuVallaBaja(self):
        """ Si la valla está baja, esta se abre """
        self.puente.bajarValla()

        self.assertFalse(self.puente.vallaAlta())

        self.puente.levantarValla()

        self.assertTrue(self.puente.vallaAlta())

    def test_elPuenteSubeSuVallaAlta(self):
        """ Si la valla está alta, al enviarle levantarValla() no modifica el estado """
        self.assertTrue(self.puente.vallaAlta())

        self.puente.levantarValla()

        self.assertTrue(self.puente.vallaAlta())




        

if __name__ == '__main__':
    unittest.main()
