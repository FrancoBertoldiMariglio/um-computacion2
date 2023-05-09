""" Memoria Compartida
Etapa 1
Escribir un programa que reciba por argumento la opción -f acompañada de un path_file
El programa deberá crear un segmento de memoria compartida y generar dos hijos H1 y H2.
H1 deberá leer desde sdtin lo que ingrese el usuario, línea por línea, enviando una señal USR1 al padre en cada línea leida.
Una vez ingresada una línea, el proceso padre leerá la memoria compartida y mostrará la línea leida por pantalla y enviará una señal USR1 a H2.
Al recibir la señal USR1, H2 leerá la línea desde la memoria compartida y la escribirá en mayúsculas en el archivo recibido como argumento.
Etapa 2
Cuando el usuario introduzca "bye" en la terminal, H1 enviará al padre la señal USR2 y terminará.
Al recibir la señal USR2, el padre, la enviará a H2 que también terminará.
El padre esperará a ambos hijos y terminará también. """


import signal
import argparse
import mmap
import os
import sys
import time

def h1():
    while True:  
        input = os.read(sys.stdin, 2024)
        if input != "bye":
            mem.write(input)
            mem.seek(0)
            os.kill(os.getppid(), signal.SIGUSR1)
            continue
        os.kill(os.getppid(), signal.SIGUSR2)
  

def fatherUSR1Handler(s, r):   
    line = mem.read()
    print(str(line))
    os.kill(rt2, signal.SIGUSR1)

def fatherUSR2Handler(s, r):   
    pass

def h2USR1Handeler(s, r):
    line = mem.read()
    line = line.decode()
    f.write(line.upper())

parser = parser = argparse.ArgumentParser()
parser.add_argument("-f", help="file to read")
args = parser.parse_args()
f = open(args.f, "w+")

mem = mmap.mmap(-1, 64)
print(os.getpid())    
rt1 = os.fork()

if rt1 != 0:
    
    signal.signal(signal.SIGUSR1, fatherUSR1Handler)
    signal.signal(signal.SIGUSR2, fatherUSR2Handler)
    
    rt2 = os.fork()
    if rt2 == 0:
        signal.signal(signal.SIGUSR1, h2USR1Handeler)
        signal.pause()
    else:
        try:
            while True:
                os.wait()
        except ChildProcessError:
            exit()

if rt1 == 0:
    while True:  
        var = os.read(0, 2024)
        if var.decode() != "bye":
            mem.write(var)
            mem.seek(0)
            print(f'PID: {os.getppid()}')
            os.kill(os.getppid(), signal.SIGUSR1)
            continue
        os.kill(os.getppid(), signal.SIGUSR2)
        break