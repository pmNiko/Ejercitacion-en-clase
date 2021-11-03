"""
    Modelar: un Puente

        atributos: 
            - numero
            - valla

        puede:
            - ver su numero
            - ver si la valla esta alta
            - bajar la valla
            - levantar la valla
"""
"""
    Extender el modelo del puente para que pueda recibir un auto como 
    parametro. 
        - en caso de que la valla del puente este levantada los autos 
          pueden circular a 40km/h
        - si la valla esta baja le envia el mensaje detenerse al vehiculo
          que lo transita.
"""
from valla import Valla
from auto import Auto

class Puente(object):
    """ 
        Clase Puente
        
        Metodos:
            ✅ numero: se puede recuperar el numero del puente
            ✅ vallaAlta: responde si la valla esta alta
            ✅ bajarValla: baja la valla
            ✅ levantarValla: sube la valla                   
    """
    
    def __init__(self, numero: int) -> None:
        self.__numero = numero
        self.__valla = Valla()
        
    @property
    def numero(self): return self.__numero

    def vallaAlta(self) -> bool:
        """ Responde True si la valla está alta """
        return self.__valla.alta

    def bajarValla(self) -> None:
        """ Baja la valla """
        if self.vallaAlta(): self.__valla.cambiarSuEstado()

    def levantarValla(self) -> None:
        """ Sube la valla  """
        if not self.vallaAlta(): self.__valla.cambiarSuEstado()

    def recibirAuto(self, un_auto: Auto) -> None:
        """ Modifica la velocidad del vehiculo que recibe como parametro """
        if self.vallaAlta(): 
            un_auto.detenerse()
            un_auto.acelerar(40)
        else: un_auto.detenerse()
    
    
    
if __name__ == '__main__':
    pass