"""Considerando el programa noblock.py, realizar un programa que lance 10 procesos hijos 
que intenten encontrar el nonce para un No-Bloque con una dificultad dada. 
El hijo que lo encuentre primero debe comunicarse con el padre. Realizar todo utilizando multiprocessing"""

from hashlib import sha256
import json
import random
from multiprocessing import Process, Pipe
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


def proof_of_work(block, child_conn, old_hash):
    """
    Function that tries different values of nonce to get a hash
    that satisfies our difficulty criteria.
    """
    difficulty = 5

    computed_hash = block.compute_hash()

    while (
        not computed_hash.startswith("0" * difficulty)
        and computed_hash != "0" * difficulty + old_hash
    ):
        block.nonce += random.randrange(0, 10, 1)
        computed_hash = block.compute_hash()

    child_conn.send(computed_hash)


if __name__ == "__main__":
    b = NoBlock(seed="La semilla que quiera", nonce=0)
    old_hash = b.compute_hash()
    child_conn, father_conn = Pipe()
    processes = []

    for i in range(10):
        process = Process(target=proof_of_work, args=(b, child_conn, old_hash))
        processes.append(process)
        process.start()

    if father_conn.recv():
        new_hash = father_conn.recv()
        for process in processes:
            if process.is_alive():
                os.kill(process.pid, signal.SIGKILL)
                process.join()
        print(new_hash)
