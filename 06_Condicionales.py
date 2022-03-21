# """Los condicionales son decisiones que se establecen desacuerdo a los parámetros que indiquemos,
# para obtener un tipo de resultado deseado.

# Ejemplo: si un número es mayor o igual que otro, los números deberán sumarse, de lo contrario deberán restarse.
# Debe cumplirse una condición para saber cuál será el camino a seguir.

# A continuación veremos cómo funcionan los condicionales en Python.

# if
# (Si) se usa para la condición principal.

# elif
# (Si no) en caso de que la condición principal o anterior no se cumpla, se puede utilizar para agregar otra condición.

# else
# (Sino) en caso de que la(s) condición(es) anterior(es) no se cumplan, se ejecuta como alternativa sin condicional.

# En lenguaje natural (español)
# ‘Si’ introduce una oración en la que se indica una condición real o hipotética que se ha de cumplir
# necesariamente para que sea cierto o se produzca lo que se expresa: Si corres, lo alcanzarás.

# ‘Sino’ es una conjunción adversativa que se escribe en una sola palabra y se usa, principalmente,
# para contraponer un concepto a otro: No estudia, sino que trabaja.

# ‘Si no’** introduce una oración condicional: Si no estudias, no aprobarás."""

#Haremos un condicional IF
#Pedimos al usuario que ingrese su edad y segun lo que ingrese le diremos si es menor de edad o no





edad = int(input("Ingresa tu edad: "))
#Agregamso el condicional if
#Empeiza copn al sentencia IF seguido de la condicion que queremos evaluar y dos puntos
if edad >= 18:
    print("Eres mayor de edad") #Bloque de codigo que queremos ejecutar
#Seguide la sentencia else que estable que hacer si la condicion no se cumple
else:
    print("Eres menor de edad")#Bloque de codigo que queremos ejecutar

#Agregamos una condicion mas
numero = int(input("Ingresa tu número: "))
#Empeiza copn al sentencia IF seguido de la condicion que queremos evaluar y dos puntos
if numero > 5:
    print("Es mayor a 5") #Bloque de codigo que queremos ejecutar
#Esta e sla nuva sentioca elif nos permite establecer tantas condciones ocmo necesitemos
elif numero == 5:
    print("Es igual a 5")
#Seguide la sentencia else que estable que hacer si la condicion no se cumple
else:
    print("Eres menor de edad")#Bloque de codigo que queremos ejecutar