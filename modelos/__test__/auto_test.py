import unittest
from auto import Auto

class TestAuto(unittest.TestCase):
    def setUp(self) -> None:
        self.auto = Auto()
    
    def test_elAutoPuedeAcelerarUnaVelocidad(self):
        """ El auto puede acelerar una velocidad """        
        self.assertEqual(self.auto.velocidad, 0)
        
        self.auto.acelerar(100)
        
        self.assertEqual(self.auto.velocidad, 100)
     
    def test_elAutoPuedeDetenerse(self):
        """ EL auto puede detenerse """
        self.auto.acelerar(100)

        self.assertEqual(self.auto.velocidad, 100)

        self.auto.detenerse()

        self.assertEqual(self.auto.velocidad, 0)  
        
    def test_elAutoSeEncuentraEnMovimiento(self):
        """ Podemos saber si el auto se encuentra en movimiento """
        self.auto.acelerar(100)

        self.assertTrue(self.auto.enMovimiento())
    
    def test_elAutoNoSeEncuentraEnMovimiento(self):
        """ Podemos saber si el auto se encuentra en movimiento """
        self.assertFalse(self.auto.enMovimiento())
        
    
        

        
    

if __name__ == '__main__':
    unittest.main()        