



def decimal_to_binario():
    
    decimal = int(input("Digite um número decimal: "))
    
    binario = ""
    
    if decimal == 0:
        print("0")

    elif decimal > 0:
        original_decimal = decimal
        while decimal > 0:
            binario = str(decimal % 2) + binario
            decimal //= 2
        print(f"El numero {original_decimal} al convertirse a binario da como resultado {binario}")
    else:
        print("El número debe ser positivo.")
        

decimal_to_binario()
