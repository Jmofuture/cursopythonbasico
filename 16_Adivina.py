#Para el siguiente ejemplo, utilizaremos módulos en Python para crear la funcionalidad de nuestro código.
# Un módulo es un archivo con funciones ya predefinidas, que tenemos disponibles para ejecutarlas.
import random as r

def run():
    aleatorio = r.randint(1,100)
    numero = int(input("Elige un numero entre 1 y 100 "))
    while numero != aleatorio:
        if numero < aleatorio:
            print("Elige un numero mas grande")
        else:
            print("El numero es mas pequeño")
        numero = int(input("Elige otro numero "))
    print("Ganaste")

if __name__ == '__main__':
    run()