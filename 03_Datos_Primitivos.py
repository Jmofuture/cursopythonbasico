# """ Un objeto es una forma de modelar el mundo en programación. En los lenguajes de programación se caracterizan por tener métodos y atributos. En Python todo es un objeto.

# Podemos encontrar cuatro tipos de datos que vienen definidos por defecto en Python, a estos tipos de datos los conocemos como primitivos.

# Tipos de datos primitivos en Python
# Integers: números Enteros
# Floats: números de punto flotante (decimales)
# Strings: cadena de caracteres (texto) todo texto debe estar entre comillas dobles o simple.
# Boolean: boolenaos (Verdadero(True) o Falso(False))
# Algunos operadores aritméticos pueden funcionar para operar con otros tipos de datos. Por ejemplo: podemos sumar strings, lo que concatena el texto o multiplicar un entero por un string, lo que repetirá el _string _las veces que indique el entero.

# Tipos de dato adicionales
# Datos en texto: str
# Datos numéricos: int, float, complex
# Datos en secuencia: list, tuple, range
# Datos de mapeo: dict
# Set Types: set, frozenset
# Datos booleanos: bool
# Datos binarios: bytes, bytearray, memoryview
# ¿Cómo saber el tipo de dato que estoy usando?
# Usamos el comando type() """


#Enteros int
edad = 35
print(type(edad))

#Flotantes float

estatura = 1.86
print(type(estatura))

#Strings
nombre =  "Jean Olmedillo"
print(type(nombre))

#Booleano True o False , se usan mayormente para condicionales

mascota = False
cafe = True

print(type(mascota))
print(type(cafe))

"""
    Cómo convertir un tipo de dato a otro en Python:

Sintaxis Descripción

int(var) variable a entero
float(var) variable a flotante
str(var) variable a texto
bool(var)variable a booleano
abs(var) variable a valor absoluto

    """

#la funcion input nos permite pedir datos al usuario por consola,
# todo dato que recibe input se recibe como string sino le especificamos el tipo de dato

numero = input("Escribe un numero: ")

print(numero)
#Recibimos el numero por consola y lo convertimos

print(int(numero))

#O podemos hacer la conversion directo en la solicitud

numero2 = int(input("Escribe un numero: "))

print(numero2)
