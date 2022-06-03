from multiprocessing import Pool
import os

pid = os.getpid()

def double(i):
    print("I'm process", pid())
    return i * 2
 
with Pool() as pool:
    result = pool.map(double, [2, 3, 4, 5])
    print(pid)