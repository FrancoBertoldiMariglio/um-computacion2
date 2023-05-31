""" Escribir un programa que reciba un mensaje desde otro proceso usando fifo (pipes con nombre). 
El proceso receptor deberá lanzar tantos hilos como líneas tenga el mensaje y deberá enviar cada línea a los hilos secundarios. 
Cada hilo secundario deberá calcular la cantidad de caracteres de su línea y COMPROBAR (asegurarse de que haya terminado) 
la cuenta de la línea anterior. """

import multiprocessing as mp
import threading as th
import os

def sender(pipeout):
    os.write(pipeout, "Computacion es re copada\nhola\nchau\n")

def receptor(pipein):
    txt = (os.read(pipein, 2024)).decode()
    print(txt)
    # contar cantidad de lineas, y lanzar un hilo por cada linea

def thread(line):
    # contar cantidad de caracteres de la linea
    print(f"La linea {line} tiene {len(line)} caracteres")

if __name__ == "__main__":
    pipe = "/tmp/fifo"
    if not os.path.exists(pipe):
        os.mkfifo(pipe)
    pipeout = os.open(pipe, os.O_WRONLY)
    pipein = os.open(pipe, os.O_RDONLY)
    p1 = mp.Process(target=sender, args=(pipeout,))
    p1.start()
    p1.join()
    receptor(pipein)

