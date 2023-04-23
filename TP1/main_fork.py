from father import dad
from son import son
import os
import argparse
import time

# pipes
rIn, wIn = os.pipe()
rOut, wOut = os.pipe()

try:
# parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="file to read")
    args = parser.parse_args()

# archivo
    f = open("/home/franco/Escritorio/um-computacion2/prueba", "r")

except argparse.ArgumentError:
    print("Ingrese una direccion de archivo")
    exit()

except FileNotFoundError:
    print("Ingrese una direccion de archivo valida")
    exit()

    
lines = f.readlines()

# lista de lineas y largo de lineas
listLines = []
lenList = []

for i in range(len(lines)):
    listLines.append(lines[i].replace("\n", ""))
    lenList.append(len(listLines[i]))

# logica
dad = dad()
son = son()
for line in listLines:
    print(line)
print("----------------------------------")
dad.sendLines(wIn, listLines)

for len in lenList:
    rt = os.fork()
    if rt > 0:
        time.sleep(0.5)
        # print(f"Papa: {os.getpid()}")
        continue
    elif rt == 0:
        # print(f"Hijo: {os.getpid()}, papa: {os.getppid()}")
        son.invert(rIn, wOut, len)
        exit()

for len in lenList:
    print(dad.readLines(rOut, len))
