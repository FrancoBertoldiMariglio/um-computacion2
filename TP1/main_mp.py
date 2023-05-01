from father import dad
from son import son
import os
import argparse
from multiprocessing import Process

# pipes
rIn, wIn = os.pipe()
rOut, wOut = os.pipe()

try:
    # parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="file to read")
    args = parser.parse_args()

# archivo
    f = open(args.f, "r")

except argparse.ArgumentError:
    print("Ingrese una direccion de archivo")
    exit()

except FileNotFoundError:
    print("Ingrese una direccion de archivo valida")
    exit()


lines = f.readlines()

# lista de lineas, largo de lineas y procesos hijos
listLines = []
lenList = []
processes = []

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
    process = Process(target=son.invert, args=(rIn, wOut, len))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

for len in lenList:
    print(dad.readLines(rOut, len))
