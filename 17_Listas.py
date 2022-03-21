# Las listas nos permiten guardar múltiples valores en una sola variable.
# Estas listas en Python nos permiten guardar elementos del mismo tipo o diferentes,
# por lo que podemos tener strings, números enteros y decimales juntos en una misma variable.
# Las listas también son conocidas como arrays en otros lenguajes programación.

numeros = [35,23,29,15,1986,1999,1.86,1.60]#Almacenan numeros
print(numeros)

lista = ['Jean','Genesis','Guayaba']#Almacenan string
print(lista)

union = numeros + lista  #se pueden concatenar y crear una lista nueva y tener varioslementos de diferente tipo
print(union)

for i in union:  #Se pueden recorrer
    print(i)