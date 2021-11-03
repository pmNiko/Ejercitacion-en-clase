"""
    Modelar: un auto 

        atributos: 
            - una velocidad, al iniciar esta parado

        puede:
            - puede ver su velocidad
            - puede acelerar una determinada velocidad
            - puede detenerse 
            - pude saber si esta en movimiento
"""


class Auto(object):  
    """ 
        Clase Auto
        
        Metodos:
            -> velocidad: devuelve la velocidad
            -> acelerar: acelera la velocidad del vehiculo
            -> detenerse: detiene el auto
            -> estaEnMovimiento?: retorna true si esta en moviento
    """  
    def __init__(self) -> None:
      self.__velocidad = 0
      
    @property
    def velocidad(self): return self.__velocidad
    
    def acelerar(self, una_velocidad: int) -> None:
        """ Este método acelerará el auto """
        self.__velocidad += una_velocidad
        
    def detenerse(self) -> None:
        """ El auto se detiene """
        self.__velocidad = 0
        
    def enMovimiento(self) -> bool:
        """ Retorno True si el auto se encuentra en movimiento """
        return self.velocidad > 0


if __name__ == '__main__':
    pass