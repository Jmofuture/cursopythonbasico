
# Un detalle muy importante en cualquier lenguaje de programación es conocer las diferencias entre los condicionales.
# En Python en particular, es crucial mencionar la diferencia entre if, elif y else.

# Diferencias entre if, else y elif
# if:
# if se encarga de iniciar el condicional y solicitar un requisito para ejecutar todo el código por debajo,
# que conocemos como bloque de código.

# else:
# Si se desea ejecutar otro código en caso de que no se cumpla el if. Por ejemplo: el usuario no elige la opción 1,
# entonces (else)…

# elif:
# Se utiliza cuando utilizamos múltiples condiciones, lo que en el código de esta clase son la opción 2 y 3.
# En esta clase, teníamos la opción 1, pero debemos también evaluar qué pasa si el usuario elige la opción 2 o 3,
# por lo que decimos “que estamos evaluando múltiples condiciones”.


menu = """
Bienvenido al conversor de monedas 🪙

Escoge tu que moneda deseas convertir:

1 - Pesos Argentinos
2 - Pesos Uruguayos
3 - Pesos Chilenos
"""

opcion = int(input(menu))


if opcion == 1:
    #Haremos un conversor de monedas de pesos Uruguayos a Dolares

    #Le pedimos al usuario que ingrese la cantidad de pesos
    pesos = input("Ingresa la cantidad de pesos Argentinos: ")
    #Ese  numero lo convertimos en un numero flotante, recordar que todo lo que ingresa por input ers un String
    pesos = float(pesos)
    #Asignaos el valor de la tasa de cambio en una constante
    USD = 200
    #Realizamso la conversion diviendo la cantidad de pesos entre la tasa de cambio USD
    cambio = pesos / USD
    #Vamso a usar la funcion round() para asignar la cantida de deciames que queremos ver,de lo contrario mostrara un montn
    cambio = round(cambio, 2)
    #Convertimos el valor de cambio a String para poder imprimirlo
    cambio = str(cambio)
    #Imprimimos
    print("El cambio fue realizado con éxito :" + "$" + cambio + " Dólares")
elif opcion == 2:
    #Haremos un conversor de monedas de pesos Uruguayos a Dolares

    #Le pedimos al usuario que ingrese la cantidad de pesos
    pesos = input("Ingresa la cantidad de pesos Uruguayos: ")
    #Ese  numero lo convertimos en un numero flotante, recordar que todo lo que ingresa por input ers un String
    pesos = float(pesos)
    #Asignaos el valor de la tasa de cambio en una constante
    USD = 45.45
    #Realizamso la conversion diviendo la cantidad de pesos entre la tasa de cambio USD
    cambio = pesos / USD
    #Vamso a usar la funcion round() para asignar la cantida de deciames que queremos ver,de lo contrario mostrara un montn
    cambio = round(cambio, 2)
    #Convertimos el valor de cambio a String para poder imprimirlo
    cambio = str(cambio)
    #Imprimimos
    print("El cambio fue realizado con éxito :" + "$" + cambio + " Dólares")
elif opcion == 3:
        #Haremos un conversor de monedas de pesos Uruguayos a Dolares

    #Le pedimos al usuario que ingrese la cantidad de pesos
    pesos = input("Ingresa la cantidad de pesos Chilenos: ")
    #Ese  numero lo convertimos en un numero flotante, recordar que todo lo que ingresa por input ers un String
    pesos = float(pesos)
    #Asignaos el valor de la tasa de cambio en una constante
    USD = 1500
    #Realizamso la conversion diviendo la cantidad de pesos entre la tasa de cambio USD
    cambio = pesos / USD
    #Vamso a usar la funcion round() para asignar la cantida de deciames que queremos ver,de lo contrario mostrara un montn
    cambio = round(cambio, 2)
    #Convertimos el valor de cambio a String para poder imprimirlo
    cambio = str(cambio)
    #Imprimimos
    print("El cambio fue realizado con éxito :" + "$" + cambio + " Dólares")
else:
    print("No ingresaste un numero valido")
