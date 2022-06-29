import getopt
import multiprocessing as mp
import sys
from math import sqrt, log10
from functools import partial

try:
    opt,arg = getopt.getopt(sys.argv[3:], 'p:f:c')
    if len(opt) != 3:
        print("Ingrese bien la cantidad de argumentos: ")
        exit()
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()


for (opt,arg) in opt:
    if opt == '-p':
       num_processes = int(arg)
    elif opt == '-f':
        path = str(arg)
    elif opt == '-c':
        calculator = str(arg)

def read(path) -> list:
    with open(path, 'r') as file:
        matrix = file.readlines()
        matrix = [line.split(',') for line in matrix]
        return matrix

def calculate(fun, matriz) -> list:
    new_matrix: list= []
    for row in matriz:
        new_file = []
        for element in row:
            element = calculate(fun, element)
            new_file.append(element)
        new_matrix.append(new_file)
    return new_matrix

def log(element) -> int:
    return log10(int(element))

def raiz(element) -> int:
    return sqrt(int(element))

def pot(element) -> int:
    return int(element)**int(element)

def calculate(fun, element) -> int:
    functions = {
        'pot': pot(element),
        'raiz': raiz(element),
        'log': log(element)
    }
    return functions[fun]

def main() -> None:
    pool = mp.Pool(processes = num_processes)
    results = pool.starmap(partial(calculator, calculate), [[read(path=path)]])
    print(results[0])

if __name__ == '__main__':
    main()