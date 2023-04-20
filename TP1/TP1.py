from father import dad
from son import son
import os
import time
import argparse

# if __name__ == '__main__':

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
f = open("/home/franco/Escritorio/um-computacion2/prueba", "r")
lines = f.readlines()

# codigaso
dad = dad()
son = son()
for line in lines:
    print(line)
print("----------------------------------")
dad.sendLines(wIn, lines)

for i in range(len(lines)):
    rt = os.fork()
    if rt == 0:
        time.sleep(3)
        continue
    elif rt > 0:
        son.aLaburarMijo(rIn, wOut)
        exit()

dad.readLines(rOut)
