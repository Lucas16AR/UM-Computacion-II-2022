import os
 
#crea procesos hijos usando metodos fork
val = os.fork()
 
#Testing the values returned by fork() method
if val == 0:
    pid = os.getpid()
    print(f"Child Process - PID: {pid}.")
elif val > 0:
    pid = os.getpid()
    print(f"Parent Process - PID: {pid} and PID {val} is Child Process.")
else:
    print("Sorry!! Child Process creation has failed...")