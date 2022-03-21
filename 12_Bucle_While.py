# Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición
# (es decir, mientras la condición tenga el valor True).

def run():
    LIMITE = 6_000_000 #Establecemos el limete
    contador = 0 #Establecemos un contador
    potencia = 2 * contador #La operacion qu queremos realiza con el contador y el limite
    while potencia < LIMITE: #Mientras la potencia sea menor que el limite hacemos
        print("2 elevado a " + str(contador) + " es igual a: " + str(potencia)) #Imprimimos
        contador = contador + 1 #incrementamos en una unidad el contador
        potencia = 2 ** contador #Y realizamos la operacion de los contrariuo tendriamos un bucle infinito

def conteo():
    contador = 1
    print(contador)
    while contador < 100:
        contador += 1
        print(contador)


if __name__ == "__main__":
    run()
    conteo()