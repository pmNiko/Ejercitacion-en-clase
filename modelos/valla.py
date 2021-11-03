"""
    Modelar: una valla

        atributos: 
            - estado por defecto esta levantada

        puede:
            - ver su estado
            - cambiar su estado
"""
class Valla(object):
    """ 
        Clase Valla
        
        Metodos:
            ✅ alta: recupera el estado
            ✅ cambiarSuEstado: invierte el estado de la valla
    """
    
    def __init__(self) -> None:
        self.__alta = True

    @property
    def alta(self): return self.__alta
    
    def cambiarSuEstado(self) -> None:
        """ Cambia el estado """
        self.__alta = not self.alta


if __name__ == '__main__':
    pass