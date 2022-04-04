from fileinput import close
import sys
import getopt
from pip import main

#def calc():
try:
    (opt,arg) = getopt.getopt(sys.argv[1:], 'o:n:m:')
    if len(opt) !=3:
        print("La cantidad de parametros y argumentos es incorrecto ")
        exit()
    
except getopt.GetoptError as error:
    print("Ocurrio un error ", str(error))
    print("Por favor, ingrese las opciones: ", opt)
    exit()
#else:          

for (op,ar) in opt:
    if op == '-o':
        ope = ar
    elif op == '-n':
        num1 = int(ar)
    elif op == '-m':
        num2 = int(ar)

def calculator(ope, num1, num2):

    if ope == '+':
        print(num1 + num2)
    elif ope == '-':
        print(num1 - num2)
    elif ope == '*':
        print(num1 * num2)
    elif ope == '/':
        print(num1 / num2)
    
if ope in ['+','-','*','/']:
    calculator(ope, num1, num2)
else:
    print('Operador invalido: ')

#if __name__ == "__main__":
#   calculator()

#print('TP1')