from father import dad
from son import son
import os
import argparse

# pipes
rIn, wIn = os.pipe()
rOut, wOut = os.pipe()

# parser
try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="file to read")
    args = parser.parse_args()
except:
    print("Ingrese una direccion de archivo valida")

# archivo
f = open(args.f, "r")
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
        # time.sleep(1)
        # print(f"Papa: {os.getpid()}")
        continue
    elif rt == 0:
        # print(f"Hijo: {os.getpid()}, papa: {os.getppid()}")
        son.invert(rIn, wOut, len)
        exit()

for len in lenList:
    print(dad.readLines(rOut, len))
