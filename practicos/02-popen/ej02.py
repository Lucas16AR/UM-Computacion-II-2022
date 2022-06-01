#Ejercicio 2 - subprocess.Popen

import sys
import subprocess
import getopt
import datetime as dt

try:
    opt, args = getopt.getopt(sys.argv[1:], 'c:f:l:')
    if len(opt) != 3:
        print("Ingrese la cantidad de argumentos: ")
        exit()
except getopt.GetoptError as error:
    print("Hay un error: " + error)
    exit()

command = ''
output_file = ''
log_file = ''

for opt, arg in opt:
    if opt == '-c':
        command = arg
    elif opt == '-f':
        output_file = open(arg, 'w')
    elif opt == '-l':
        log_file = arg

process = subprocess.Popen([command], stdout=output_file, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
error = process.communicate()[1] 

if not error:
    date = dt.datetime.now()
    to_write = f'{date}: Comando {command} se ha ejecuta correctamente'
    file_to_write = open(log_file, 'a')
    file_to_write.write(to_write)
    file_to_write.write('\n')
    file_to_write.close()
else:
    date = dt.datetime.now()
    to_write = f"{date}: >> {error}"
    file_to_write = open(log_file, "a")
    file_to_write.write(to_write)
    file_to_write.write("\n")
    file_to_write.close()

output_file.writelines('\n')
output_file.close()