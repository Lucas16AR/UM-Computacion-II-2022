#Ejercicio 1 Ejemplo, solucion de problema final

import getopt
import sys

#(opt,arg) = getopt.getopt(sys.argv[1:], 'ab:c')
#python getopt_ejemplos.py -a -b 123 -c
try:
    opt,arg = getopt.getopt(sys.argv[1:], 'o:n:m:')
    if len(opt) != 3:
        print("Por favor ingrese bien la cantidad de argumentos")
        exit()
except getopt.GetoptError as error:
    print(f"Ha habido un error: {error}")
    exit()

#print(f"opciones {opt}")
#print(f"argumentos {arg}")

for (op,ar) in opt:
    if op == '-o':
        ope = ar
    elif op == '-n':
        num1 = int(ar)
    elif op == '-m':
        num2 = int(ar)

def calc(ope, num1, num2):
    if ope == '+':
        print(num1+num2)
    elif ope == '-':
        print(num1-num2) 
    elif ope == '*':
        print(num1*num2)
    elif ope == '/':
        print(num1/num2)


if ope in["+","-","*","/"]:
    calc(ope, num1, num2)
else:
    print("El operador es invaldo, por favor solo usar +, -, *, /")