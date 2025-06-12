class Vehiculos():
#se define __init_ para inicializar los atributos de la clase, este es el metodo constructor de la clase

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.en_marcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self. en_marcha = True
    
    def acelerar(self):
        self.acelera = True

    def Frenar(self):

        self.frena = True
    
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", 
              self.en_marcha,"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
    


class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado = cargar

        if (self.cargado):
            return print("La furgoneta está cargada")
        else:
            return ("La furgoneta no està cargada")

class moto(Vehiculos):
    hcaballito = ""
    
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"
        
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", 
              self.en_marcha,"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)
        
class v_electrico(Vehiculos):

    def __init__ (self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100
        
    def cargar_energia(self):
        self.cargando = True 




# class bicicleta_electrica(Vehiculos, v_electrico):
#     pass
# mi_moto = moto("Yamaha", "XTZ150")
# mi_moto.caballito()
# mi_moto.estado()

# mi_furgoneta = Furgoneta("Renault", "Kangoo")
# mi_furgoneta.arrancar()
# mi_furgoneta.acelerar()
# mi_furgoneta.carga(True)
# mi_furgoneta.estado()

# mi_carro_electrico = v_electrico()
# mi_carro_electrico.arrancar()
# mi_carro_electrico.cargar_energia(False)

mi_bici = v_electrico("Specialized", "Turbo Vado SL")
mi_bici.arrancar()
mi_bici.estado()