import os,sys,time

ret = os.fork()

if not ret:
	print("soy el hijo")
	print("chau...me muero...")
	sys.exit()

print("padre paspando moscas")
time.sleep(100)