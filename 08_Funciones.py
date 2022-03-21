# Las funciones ayudan a optimizar el código. Es decir, utilizar la menor cantidad de líneas dentro del código y
# evitar escribir acciones repetitivas.

# Esto nos sirve para entregar un código más limpio y con buenas prácticas,
# que no desperdicia recursos innecesariamente. En Python, para definir funciones empleamos def.

# Gracias a def, podemos “definir” funciones que emplearemos más tarde. Una función,
# en programación, es un grupo de instrucciones con un objetivo en particular y que se ejecuta cuando es “invocada”.

# Cuando la definimos, estamos dándole un conjunto de instrucciones o un algoritmo.
# Al ahorrar líneas de código con funciones logramos también que la legibilidad de este sea más fácil.

# print("Repetido")
# print("Como print")
# print("Y esto lo quiero imprimir 3 veces")

# print("Repetido")
# print("Como print")
# print("Y esto lo quiero imprimir 3 veces")

# print("Repetido")
# print("Como print")
# print("Y esto lo quiero imprimir 3 veces")

# def imprimir_tres():
#     print("Repetido")
#     print("Como print")
#     print("Y esto lo quiero imprimir 3 veces")

# imprimir_tres()
# imprimir_tres()
# imprimir_tres()

#Funcion con parametro

# opcion = int(input("Elige una opcion entre 1 y 3: "))

# if opcion == 1:
#     print("Hola")
#     print("Cómo estas?")
#     print("Elegiste la opcion 1")
#     print("Adios")
# elif opcion == 2:
#     print("Hola")
#     print("Cómo estas?")
#     print("Elegiste la opcion 2")
#     print("Adios")
# elif opcion == 3:
#     print("Hola")
#     print("Cómo estas?")
#     print("Elegiste la opcion 3")
#     print("Adios")
# else:
#     print("No elegiste una opcion válida")


#Para no repetir toda esta logica usamo una funcion con parametros

opcion = int(input("Elige una opcion entre 1 y 3: "))

def conversacion(mensaje):#le asignamo s ala funcion un parametro que le va allegar mediante el input
    print("Hola")
    print("Cómo estas?")
    print(mensaje) #Aca recivimos el parametro
    print("Adios")

if opcion == 1:
    conversacion("Elegiste la opcion 1")
elif opcion == 2:
    conversacion("Elegiste la opcion 2")
elif opcion == 3:
    conversacion("Elegiste la opcion 3")
else:
    print("No elegiste una opcion válida")


#Si queremos guarada el valor que la funcion devuelve devemo susar el return

def suma (a,b): #funcion que va a sumar dos numero
    print("Se suman dos numero") #Imprimimos un mensaje
    resultado = a + b #asignamos la suma a na variable
    return resultado #con return podemos usar este resulktado fuera de la funcion almacenandola en otra variable

sumatoria = suma(35,23) #resivimos los valores de la variable resultado qeu regresa la funcion
print(sumatoria)