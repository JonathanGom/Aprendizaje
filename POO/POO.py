



class Coche():
#propiedades de la clase coche
    def __init__(self):
        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        self.__ruedas = 4
        self.__en_marcha = False
    

#metodos de la clase coche

    def arrancar(self,arrancamos):
        self.__en_marcha = arrancamos

        chequeo = self.__chequeo_interno()         

        if (self.__en_marcha and chequeo):
            return print("El coche está en marcha")
        
        elif (self.__en_marcha and chequeo == False):
            return print("El coche no puede arrancar, chequeo interno incorrecto")
        
        else:
            return print("El coche està detenido")
                
    def estado(self):
        print("El coche tiene un largo de ", self.__largo_chasis, "un ancho de ", self.__ancho_chasis, 
                "y tiene ", self.__ruedas, "ruedas")
        
    def __chequeo_interno(self):
        print("Realizando chequeo interno...")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "Cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "Cerradas"):
            return True
        else:
            return False
        
#instanciar una clase
mi_coche = Coche()
mi_coche.arrancar(True)
mi_coche.estado()

# print(mi_coche.largo_chasis)
# print(mi_coche.ancho_chasis)
# mi_coche.arrancar()
# print(mi_coche.estado())

# print("------------------Creando un segundo coche-------------------")
# mi_coche2 = Coche()
# mi_coche2.arrancar(False)
# mi_coche2.estado()
# print(mi_coche2.chequeo_interno())


