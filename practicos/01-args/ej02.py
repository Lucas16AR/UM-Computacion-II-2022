#Ejercicio 2 - Argparse

from asyncore import write
from distutils.file_util import write_file
import os, argparse

parser = argparse.ArgumentParser(description = "test")

parser.add_argument('-i', "--source_file", type = str, required = True, help = "Nombre de archivo origen")
parser.add_argument('-o', "--destiny_file", type = str, help = "Nombre de archivo destino")
args = parser.parse_args()

#try:
#    file = open(args.file,  'r')
#except FileNotFoundError as error:
#    print(f"El archivo {args.file} no existe en el disco, error: {error}")
#    exit()
#
#lines = file.readlines()
#file.close()

if os.path.isfile(args.source_file):
    print("El archivo origen existe")
    file = open(args.source_file, 'r')
    cont = file.read()
    file.close()
    file2 = open(args.destiny_file, 'a+')
    file2.write(cont)
    file2.close()
    print("Contenido copiado existosamente")
else:
    print("El archivo origen no existe")


#write_file()