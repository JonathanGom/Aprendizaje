class Persona():

    def __init__(self, nombre, edad, ubicacion):
        
        self.nombre = nombre
        self.edad = edad
        self.ubicacion = ubicacion
    
    def descripcion(self):
        print(f"Nombre: {self.nombre}, \nEdad: {self.edad}, \nUbicación: {self.ubicacion}")
    


class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, ubicacion_empleado):

        super().__init__(nombre_empleado, edad_empleado, ubicacion_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "\nAntigüedad: ", self.antiguedad, " años")

Antonio = Empleado(1500, 5, "Juan", 30, "Bogota")
Manuel = Persona("Manuel", 25, "Madrid")
Antonio.descripcion()
print (isinstance(Manuel, Empleado))