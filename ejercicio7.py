"""Verificar si es posible que dos procesos hijos (o nieto) lean el PIPE del padre."""

import os

def family():
    r, w = os.pipe()
    rt0 = os.fork()
    rt1 = os.fork()

    if rt0 > 0:
        os.close(r)
        input = bytes("line", 'utf-8')
        os.write(w, input)

    elif rt0 == 0:
         os.close(w)
         output = os.read(r, 4)
         print(f"{output}, PID: {os.getpid()}, PPID: {os.getppid()}")
         exit()
    
    elif rt1 == 0 and rt0 == 0:
        os.close(w)
        output = os.read(r, 4)
        print(f"{output}, PID: {os.getpid()}, PPID: {os.getppid()}")
        exit()

if __name__ == '__main__':
    family()