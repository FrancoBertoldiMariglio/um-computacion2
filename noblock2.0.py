"""Considerando el programa noblock.py, realizar un programa que lance 10 procesos hijos 
que intenten encontrar el nonce para un No-Bloque con una dificultad dada. El hijo que lo 
encuentre primero debe comunicarse con el padre. Realizar todo utilizando multiprocessing"""

from hashlib import sha256
import json
import random
from multiprocessing import Process, Pipe, Pool
import signal
import os


class NoBlock:
    def __init__(self, seed, nonce=0):
        self.seed = seed
        self.nonce = nonce

    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()  # Devuelve el hash del bloque


def proof_of_work(block, child_conn, i):
    """
    Function that tries different values of nonce to get a hash
    that satisfies our difficulty criteria.
    """
    difficulty = 5

    computed_hash = block.compute_hash()

    print(f"{i+1}: {os.getpid()}")

    while not computed_hash.startswith("0" * difficulty):
        block.nonce += random.randrange(0, 10, 1)
        computed_hash = block.compute_hash()

    child_conn.send({"hash": computed_hash, "PID": os.getpid()})
    child_conn.close()

if __name__ == "__main__":
    b = NoBlock(seed="La semilla que quiera", nonce=0)
    # old_hash = b.compute_hash()
    child_conn, father_conn = Pipe()
    processes = []

    for i in range(10):
        process = Process(target=proof_of_work, args=(b, child_conn, i))
        processes.append(process)
        process.start()

    if father_conn.recv()["hash"]:
        new_hash = father_conn.recv()["hash"]
        winner = father_conn.recv()["PID"]
        for process in processes:
            if process.is_alive():
                os.kill(process.pid, signal.SIGKILL)
            process.join()

        print(f"new hash: {new_hash}, encontrado por: {winner}")


# COMENTARIO: la idea era que se guardaran todos los PIDs de los procesos, pero el tema es
# que a cada proceso no se le asigna un PID hasta ejecutar start().
