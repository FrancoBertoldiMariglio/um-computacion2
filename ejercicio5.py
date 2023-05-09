"""Realizar un programa que implemente fork junto con el parseo de argumentos. 
Deberá realizar relizar un fork si -f aparece entre las opciones al ejecutar el programa. 
El proceso padre deberá calcular la raiz cuadrada positiva de un numero y el hijo la raiz negativa."""

import argparse
import os
import math as ma


def fork():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numero", help="numero al que sacarle la raiz")
    parser.add_argument(
        "-f", "--fork", help="hace el fork del programa", action="store_true")
    args = parser.parse_args()

    if args.n > 0:
        if args.fork:
            ret = os.fork()
            if ret > 0:
                return ma.sqrt(int(args.numero))
            elif ret == 0:
                return -(ma.sqrt(int(args.numero)))
        return ma.sqrt(int(args.numero))
    return f"Ingrese un numero mayor que 0"


if __name__ == '__main__':
    print(fork())
