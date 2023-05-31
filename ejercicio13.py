""" Escribir un programa que reciba un mensaje desde otro proceso usando fifo (pipes con nombre). 
El proceso receptor deberá lanzar tantos hilos como líneas tenga el mensaje y deberá enviar cada línea a los hilos secundarios. 
Cada hilo secundario deberá calcular la cantidad de caracteres de su línea y ¿COMPROBAR (asegurarse de que haya terminado) 
la cuenta de la línea anterior?. """

import multiprocessing as mp
import threading as th
import os

def sender(pipeout):
    pipeout.send("Computacion es re copada\nhola\nchau\nhola\nchau\n")

def receptor(pipein):
    txt = pipein.recv().split("\n")
    for line in txt:
        if line != "":
            thread = th.Thread(target=worker, args=(line,))
            thread.start()
            thread.join()

def worker(line):
    print(f"Soy el hilo {th.current_thread().name} y mi linea tiene {len(line)} caracteres")

if __name__ == "__main__":
    pipein, pipeout = mp.Pipe([False])
    p1 = mp.Process(target=sender, args=(pipeout,))
    p1.start()
    p1.join()
    receptor(pipein)