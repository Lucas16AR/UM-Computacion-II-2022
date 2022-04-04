from os import fork
import time
from unicodedata import name

def main():
    number = 1
    if fork() == 0:
        number +- 1
        print('Numero en el hijo tiene %d' % number)
    else:
        time.sleep(0.01)
        number -= 1
        print(f'Numero en el padre tiene {number}')

if __name__ == "__main__":
    main()