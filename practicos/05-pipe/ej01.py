import getopt
import imp
import sys
import os

try:
    opt,arg = getopt.getopt(sys.argv[1:], 'f:')
except getopt.GetoptError as error:
    print(f'Ha habido un error: {error}')
    exit()

for (op,ar) in opt:
    if op == '-f':
        file_to_read = ar

def read():
    file = open(file_to_read, 'r')
    return file.readlines()

lines = []

def create(line):
    if not os.fork():
        os.write(w, line[::-1].encode('ascii'))
        os._exit(0)
    else:
        value = os.read(r, 100)
        lines.append(value.decode())

if __name__ == '__main__':
    lines = read()
    r, w = os.pipe()

    for line in lines:
        create(line)
    
    for line in lines:
        os.wait()

    for line in lines:
        print(line)