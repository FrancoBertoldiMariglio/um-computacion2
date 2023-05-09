"""Escribir un programa en Python que acepte argumentos de línea de comando para leer un 
archivo de texto. El programa debe contar el número de palabras y líneas del archivo e 
imprimirlas en la salida estándar. Además el programa debe aceptar una opción para imprimir 
la longitud promedio de las palabras del archivo. Esta última opción no debe ser obligatoria. 
Si hubiese errores deben guardarse el un archivo cuyo nombre será "errors.log" usando la redirección 
de la salida de error."""

import argparse
import sys

def txtFile():
    parser = argparse.ArgumentParser()
    
    try:
        parser.add_argument("-f", help="archivo de texto", type=str)
        parser.add_argument("-p", "--promedio", help="saca el promedio de palabras por linea")
        args = parser.parse_args()
        f = open(args.f, "r")
        file = f.read()
        lineas = file.split("\n")
        palabras = 0

        for i in lineas:
            cadena = i.split()
            palabras += len(cadena)

        print(f"Palabras: {palabras}, lineas: {len(lineas) - 1}", file=sys.stdout)
        
        if args.promedio:
            print(f"Promedio: {palabras/(len(lineas) - 1)}", file=sys.stdout)
    
    except:
        err = "ingrese el parmatro coreespondiente"
        with open("errors.log", "a") as f:
            f.write(f"{err}")
        sys.stderr.write(f"{err}")
        sys.exit(1)

if __name__ == '__main__':
    txtFile()