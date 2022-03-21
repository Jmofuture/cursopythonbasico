#Haremos un conversor de monedas de pesos Uruguayos a Dolares

#Le pedimos al usuario que ingrese la cantidad de pesos
pesos = input("Ingresa la cantidad de pesos: ")
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

