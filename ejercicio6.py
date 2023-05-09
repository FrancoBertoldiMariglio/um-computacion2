""" Escribir un programa en Python que comunique dos procesos. El proceso padre 
deberá leer un archivo de texto y enviar cada línea del archivo al proceso hijo 
a través de un pipe. El proceso hijo deberá recibir las líneas del archivo y, 
por cada una de ellas, contar la cantidad de palabras que contiene y mostrar ese número."""

import os
import argparse
import time


def pipe():
    parser = argparse.ArgumentParser()
    r, w = os.pipe()
    rt = os.fork()

    if rt > 0:
        os.close(r)
        parser.add_argument("-f", help="archivo de texto", type=str)
        args = parser.parse_args()
        f = open(args.f, "r")
        file = f.read()
        lines = file.split("\n")
        for line in lines:
            esc = bytes(line, 'utf-8')
            os.write(w, esc)
            time.sleep(1)

    elif rt == 0:
        os.close(w)
        int = 1
        while True:
            line = os.read(r, 2024)
            length = len(line)
            print(f"Linea {int}: {length}")
            int += 1
            if len(line) == 0:
                break
        exit()


if __name__ == '__main__':
    pipe()
