# """
# Operadores lógicos
# and ( y ): compara dos valores, y si ambos son verdaderos, devuelve True.
# or ( ó ): si al comparar dos valores y uno de los dos se cumple, devuelve True. Solo devuelve falso cuando los dos valores no se cumplen.
# not ( no): invierte el valor de una variable, dando el valor contrario al de la variable evaluada.
# Operadores de comparación
# == ( igual qué ): determina si dos valores son iguales o no.
# != (diferente de): determina si dos valores son distintos o no. Si los valores son diferentes devuelve True, si son iguales devuelve False.
# > (mayor que): compara dos valores, y determina si es mayor que el otro.
# < (menor que): compara dos valores y determina si es menor que el otro.
# >= (mayor o igual): compara dos valores y determinas si es mayor o igual que el otro.
# <= (menor o igual): compara dos valores y determinas si es menor o igual que el otro.
# """


#Operadores lógicos
es_estudiante = True
trabaja = False

print(es_estudiante and trabaja)

print(es_estudiante or trabaja)

print(not(es_estudiante))

#Operadores de comparación

num1 = 5
num2 = 5

print(num1 == num2) #Es igual?

num3 = 7

print(num1 == num3)#Es igual?

print(num1 != num3)#Es diferente?

print(num1 > num3)#Es mayor?

print(num1 < num3)#Es menor?

print(num1 >= num3)#Es mayor o igual?

print(num1 <= num3)#Es menor o igual?