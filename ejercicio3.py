import argparse
import sys

def txtFile():
    parser = argparse.ArgumentParser()
    
    try:
        parser.add_argument("txt", help="archivo de texto", type=str)
        parser.add_argument("-promedio", help="saca el promedio de palabras por linea")

    except argparse.ArgumentError as err:
        print(err, file=sys.stderr)
        f = open("/home/franco/Escritorio/um-computacion2/errors.log", "a+")
        f.write(err)
        f.close()

    args = parser.parse_args()
    f = open(args.txt, "r")
    file = f.read()
    lineas = file.split("\n")
    palabras = 0

    for i in lineas:
        cadena = i.split()
        palabras += len(cadena)

    print(f"Palabras: {palabras}, lineas: {len(lineas) - 1}", file=sys.stdout)
    
    if args.promedio:
        print(f"Promedio: {palabras/(len(lineas) - 1)}", file=sys.stdout)

if __name__ == '__main__':
    txtFile()