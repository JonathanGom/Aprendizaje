
```python
print("Hola, Mundo")
```

## Variables

```python
# Variable: Es un espacio en memoria que almacena un valor.
# <var> = <valor>

# Los nombres de variables en Python deben empezar con una letra minúscula o un guion bajo. No pueden comenzar con números.
# Python distingue entre mayúsculas y minúsculas: 'numero' y 'Numero' son diferentes.

Numero = 10
print(Numero)
```

## Tipos de Datos

### Números Enteros

```python
NumeroEntero = int(10)
print(type(NumeroEntero))
```

### Números Flotantes

```python
NumeroFlotante = float(10.5)
print(type(NumeroFlotante))
```

### Booleanos

```python
ValorBooleano = bool(True)
print(type(ValorBooleano))
```

### Cadenas de Texto

```python
CadenaTexto = str("Hola, Mundo")
print(type(CadenaTexto))
print(len(CadenaTexto))  # Longitud
print(CadenaTexto[8])    # Índice específico
print(CadenaTexto[0:4])  # Slicing
print(CadenaTexto[0:10:2])
print(CadenaTexto[::])
print(CadenaTexto[::-1])
print(CadenaTexto[5:])
print(CadenaTexto[:5])
```

### Métodos de Cadenas

```python
print(CadenaTexto.capitalize())
print(CadenaTexto.upper())
print(CadenaTexto.lower())
print(CadenaTexto.replace("Mundo", "Python"))
print(CadenaTexto.split(","))
print(CadenaTexto.strip())
print(CadenaTexto.find("Mundo"))
print(CadenaTexto.count("o"))
```

### Concatenación

```python
CadenaTexto2 = " Python"
```

### Entrada de Datos

```python
NumeroUsuario = int(input("Introduce un numero: "))
print("El numero que has introducido es: " + str(NumeroUsuario))
```

## Operadores

- **Aritméticos**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Lógicos**: `and`, `or`, `not`
- **Asignación**: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`
- **Relacionales**: `==`, `!=`, `<`, `>`, `<=`, `>=`

## Condicionales

```python
if NumeroUsuario > 10:
    print("El numero es mayor que 10")
elif NumeroUsuario == 10:
    print("El numero es igual a 10")
else:
    print("El numero es menor que 10")
```

## Listas

```python
ListaNumerosCuadrados = [x**2 for x in range(1, 11)]
print(ListaNumerosCuadrados)

ListaMixta = [1, "Hola", True, 3.14, [1, 2, 3]]

ListaNumeros = [1, 2, 3, 4, 5]
print(ListaNumeros[3])
```

### Métodos de Listas

```python
listaPrueba = []
for i in range(0, 200):
    i += 1
    listaPrueba.append(i)

print(listaPrueba)
print(56 in listaPrueba)

listaPrueba.append(6)
listaPrueba.reverse()
listaPrueba.remove(3)
listaPrueba.pop()
listaPrueba.insert(2, 10)
listaPrueba.extend([7, 8, 9])
listaPrueba.index(2)
listaPrueba.count(2)
listaPrueba.sort()

print(listaPrueba)
```

## Tuplas

```python
tuplaPrueba = (1, "Hola", True, 3.14, (10, 2, 3), 1)
print(tuplaPrueba.count(12))
```

## Diccionarios

```python
diccionarioPrueba = {
    "clave1": "valor1",
    "clave2": 2,
    "clave3": True,
    "clave4": [1, 2, 3],
    "clave5": (4, 5, 6)
}

print(diccionarioPrueba["clave1"])
diccionarioPrueba["clave6"] = "valor6"
print(diccionarioPrueba.get("clave2"))
del diccionarioPrueba["clave2"]
print(diccionarioPrueba.keys())
print(diccionarioPrueba.values())
diccionarioPrueba["Nombre"] = "Jonathan"
print(diccionarioPrueba)
diccionarioPrueba["Nombre"] = "Juan"
print(diccionarioPrueba.get("Nombre"))
```

## Funciones Built-in

Algunas funciones útiles: `abs()`, `all()`, `any()`, `bin()`, `bool()`, `chr()`, `dict()`, `dir()`, `enumerate()`, `eval()`, `float()`, `int()`, `len()`, `list()`, `map()`, `max()`, `min()`, `next()`, `oct()`, `ord()`, `pow()`, `range()`, `round()`, `set()`, `sorted()`, `str()`, `sum()`, `type()`, `zip()`

## Ciclo `for`

```python
for num in range(1, 100, 2):
    num += 1
    print("Los multiplos de 2 son: " + str(num))
```

### Iterar Diccionario

```python
for clave, valor in diccionarioPrueba.items():
    print(f"La clave es: {clave} y el valor es: {valor}")
```

## Ciclo `while`

```python
contador = 0
while contador < 10:
    print("El contador es: " + str(contador))
    contador += 1

x = 20
while x < 35:
    print("El valor de x es: " + str(x))
    x += 3
```

## Funciones

```python
def mostrar_doble(num):
    print(num * 2)

print(mostrar_doble(20))
```

### Función con Retorno

```python
def sumar(a, b):
    return a + b

print(sumar(5, 10))
```

### Función Recursiva: Factorial

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(55))
```

### Función Recursiva: Fibonacci

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(120))
```