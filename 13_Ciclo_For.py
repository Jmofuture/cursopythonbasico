# El ciclo for es un tipo de bucle usado cuando se conozcan la cantidad de veces a iterar.

# Un contador es una variable que se encarga de contener valores que irán incrementando o
# decrementando cada vez que se ejecuta una acción que lo contenga. El incremento o decremento es
# llamado paso del contador y es siempre constante.

# Ejemplo: El marcador de un partido de fútbol, cada vez que un equipo anote un gol,
# aumenta su marcador en una unidad.

# Ejemplo 2: En las carreras de autos, cuando un vehículo pasa por la línea de meta, se
# incrementa en una unidad el número de vueltas dadas al circuito, o bien se decrementa el número de vueltas que faltan por realizar.

# Entonces, el incremento es siempre constante, el paso del contador no necesariamente puede ser una unidad, también puede incrementarse o decrementarse de a dos, tres, cuatro, hasta n. Es decir, puede ser cualquier número que conserve siempre el mismo valor durante todo el programa.

# Su sintaxis es:
# variable = variable + constante(al incrementar)
# variable = variable - constante(al decrementar)

# o de manera resumida:

# variable += constante
# variable -= constante

# for contador in range(1, 1001):#Range pone un tope hasta hasta el numero anterior si es 1000 imprime hasta el 999
#     print(contador)


# for i in range(10):
#     print(11 * i)


#Recorrer Strings Recorrer un string con el ciclo For es tomar la cadena de caracteres y separarlas una a una.




def run():
    frase = input("Escribe una frase: ")
    # for letra in nombre:
    #     print(letra)
    for letra in frase:
        print(letra.upper())




if __name__ == "__main__":
    run()