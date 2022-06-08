import multiprocessing

def print_cube(num):
    print("Cube: {}".format(num*num*num))

def print_square(num):
    print("Square: {}".format(num*num*num))

if __name__ == "__main__":
    p1 = multiprocessing.Process(print(print_cube(5,)))
    p2 = multiprocessing.Process(print(print_square(5)))

    p1.start()
    p2.start()