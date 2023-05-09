"""Escribir un programa en Python que acepte dos argumentos de línea de comando: una cadena de texto, 
un número entero. El programa debe imprimir una repetición de la cadena de texto tantas veces como el 
número entero."""

import getopt
import sys

def numCadena():
    number = int
    string = str
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv,"s:n:")

    for opt, arg in opts:
        if opt in ["-s"]:
            string = arg
        elif opt in ["-n"]:
            number = arg
        
    print(f"cadena {string}, numero {number}")

    if int(number) > 0:
        for i in range(int(number)):
            print(string)
    else:
        print("Ingrese un valor valido")


if __name__ == '__main__':
    numCadena()
