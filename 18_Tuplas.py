# Las tuplas son estructuras de datos inmutables. Es decir, no puedes modificar una tupla a agregando o quitando un valor.
# Lo único que puedes hacer es definir de nuevo esa tupla a.
# Los objetos inmutables (como los strings) son tipos de datos para Python que apuntan a un
# lugar específico en memoria y que su contenido no puede ser cambiado. Al cambiar el contenido
# predefiniendo el contenido de la variable a, entonces cambiará su posición en memoria.


numeros = (35,23,29,15,1986,1999,1.86,1.60)#Almacenan numeros
print(numeros)

lista = ('Jean','Genesis','Guayaba')#Almacenan string
print(lista)

union = numeros + lista  #se pueden concatenar y crear una lista nueva y tener varioslementos de diferente tipo
print(union)

