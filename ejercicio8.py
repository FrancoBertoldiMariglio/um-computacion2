"""Verificar si el PIPE sigue existiendo cuendo el padre muere (termina el proceso),
 cuando el hijo muere [o cuendo mueren ambos] $ ls -l /proc/[pid]/fd/"""

import os
import time


def pipeClose():
    os.pipe()
    rt = os.fork()

    if rt > 0:
        print(os.getpid())
        exit()

    elif rt == 0:
        print(os.getpid())
        time.sleep(100)
        print("hola")

if __name__ == '__main__':
    pipeClose()
