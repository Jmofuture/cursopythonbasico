# RECURSOS
# MARCADORES
# Para trabajar con cadenas de texto en Python, vamos a aplicar una serie de métodos a las variables que hayamos creado anteriormente.
# Método: es una función especial, que existe para un tipo de dato en particular. Por ejemplo,
# si queremos que el texto ingresado se transforme en mayúsculas.

# Métodos para trabajar con texto en Python
# variable.strip(): El método strip eliminará todos los caracteres vacíos que pueda contener la variable

# variable.lower(): El método lower convertirá a las letras en minúsculas.

# variable.upper(): El método upper convertirá a las letras en mayúsculas.

# variable.capitalize(): El método capitalize convertirá a la primera letra de la cadena de caracteres en mayúscula.

# variable.replace (‘o’, ‘a’): El método replace remplazará un caracterer por otro. En este caso remplazará todas
# las ‘o’ por el caracter ‘a’.

# len(variable): Te indica la longitud de la cadena de texto dentro de la variable en ese momento.

# Índices:
# Se escriben entre corchetes al lado de la variable y son apuntadores numéricos a cada caracter. Por ejemplo,
# para el nombre Facundo, cuando utilizamos la variable nombre[1], aparece la letra ‘a’, dado que dicha variable tiene almacenada
# en ese momento la cadena de caracteres ‘Facundo’ donde la ‘a’ es el segundo caracterer.

# Aclaración: se comienza a contar caracteres desde el 0 (que es el primer número en informática).
# Siguiendo el ejemplo, la letra ‘F’ de ‘Facundo’ es el caracter número 0. Por ende, nombre[0], nos devolvería una F.

nombre = input("Cúal es tu nombre: ")

#Metodo upper nos pasa el todo el texto a mayusculas

mayusculas = nombre.upper()
print(mayusculas)

#Metodo lower pasa el todo el texto a minuscolas

minusculas = mayusculas.lower()
print(minusculas)

#Metodo capitalize nos coloca solo la primera letra en mayuscula

primera_letra = nombre.capitalize()
print(primera_letra)

#Metodo strip elimina los espacios vacios al principio o alfinal de un texto

espacios = nombre.strip()
print(espacios)

#Metodo replace, es una funcion que recibe parametro, el valor uqe queros reemplazar y el valor a asignar
#Puede ser una letra o el texto entero

replace = nombre.replace("Jean", "Michell")
print(replace)

replace_letra = nombre.replace("J", "G")
print(replace_letra)

#Si queremos saber el caracter de un indice debemos colcoar al nombre de la variable y entre corchetes [1] y el numero del indice
#Tomando en cuentra que cuenta que el conteo comienza en 0

print(nombre[0])

#Metodo len nos permite saber el largo de una cadena de caracteres, esto incluye los espacios en blanco
#Se usa de manera uinversa, no con el dot metod, sino s ele pasa como parametro la varieble o la cadena

print(len(nombre))

#Metodo slice [No se escribe slice] nos permite devidir las cadenas de texto
#Este metodo no spide dos parametro encerrados en corchetes sepaados por dos puntos [0:3]
#Debemos indicar el indice apartir del cual queremos dividir y el indice hasta el que quemos llegar +1
#Es decir ai quere dividir esta palabra CASA en dos CA y SA debemos hacer lo siguiente
# CASA[0:2] si bien casa tiene 4 carateres debemso recordar que lo indices se cuentan desde el 0
#Por lo que se queremos llega a la primera A que es el indice 1 en el slice debemos colocar como limite el indice 2
#Si contamos apartir del indice 0 podemos simplemente dejar elespcio en blanco y solo colocar el indice tope [:2]
#Si queremos cortar apartir de un dice y tomar el resto del texto podemos invertir la regla anterior [2:] esto dividira
#la cadena en dos una con los indices 0 y 1, otra mitad con todo lo que haya desde el indice 2 en adelante
#Tambien podemos extrar carateres siguien pasos dentro del slice con un tercer parametro [1:5:2]
#Por defecto el tecer parametro es 1 por lo que nos trae siempre la cadena con los carcteres seguido
#Pero si le asignamos un 2 por ejemplo cada dos caractere por lo que Michell seria ihl
slice = nombre
print(slice[:2])
print(slice[2:])
print(slice[2:])
print(slice[1::2])


