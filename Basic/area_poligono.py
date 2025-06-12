

def calcular_area_poligono():

    print("Seleccione una opción:")
    print("1. Calcular área Triangulo")
    print("2. Calcular área Cuadrado")
    print("3. Calcular área Rectangulo")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción: ")
    
    if opcion == "1":

        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = str((base * altura) / 2)
        print(f"El área del triángulo es: {area}")
    elif opcion == "2":

        lado = float(input("Ingrese el lado del cuadrado: "))
        area = lado ** 2
        print(f"El área del cuadrado es: {area}")

    elif opcion == "3":

        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = base * altura
        print(f"El área del rectángulo es: {area}")
    
    else:

        print("Opción inválida. Por favor, intente de nuevo.")
        
    

calcular_area_poligono()