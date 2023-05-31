
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