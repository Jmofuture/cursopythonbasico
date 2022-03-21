# Los diccionarios en Python son una estructura de datos mutable las cuales almacenan diferentes
# tipos de valores sin darle importancia a su orden. Identifican a cada elemento por una clave (Key).
# Se escriben entre {}.

# Operaciones en diccionarios
# .keys():Retorna la clave de nuestro elemento.

# .values(): Retorna una lista de elementos (valores del diccionario).

# .items(): Devuelve lista de tuplas (primero la clave y luego el valor).

# .clear(): Elimina todos los items del diccionario.

# .pop(“n”): Elimina el elemento ingresado.

def run():
    diccionario = {
    "Nombre" : "Jean",
    "Apellido": "Olmedillo",
    "Edad": 5
    }
    print(diccionario) #Imprime todo el diccionario
    print(diccionario["Nombre"]) #Colocando la clave nos trae el valor

    #Podemos recorrer los diccionarios
    for persona in diccionario.keys(): #imprimimos solo las llaves
        print(persona)

    for persona in diccionario.values(): #imprimimos solo los valores
        print(persona)

    for persona, valor in diccionario.items(): #imprimimos ambas
        print(persona, valor)

if __name__ == "__main__":
    run()