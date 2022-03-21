#Palindromo es un apalabra que se lee igual al derecho que al reves
def palindromo(palabra):
    palabra = palabra.replace(' ', '') #Eliminamos los espacios en medio
    palabra = palabra.upper() #Pasamos toda la palabra a mayusc o minuc
    palabra_invertida = palabra[::-1]#giramos la palabra con los pasos negativos
    if palabra == palabra_invertida:
        return True
    else: return False



def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es Palindromo")
    else:
        print("No es Palindromo")


if __name__ == '__main__': #Esto es un entry point debo buscar mas informacion al respecto
    run()