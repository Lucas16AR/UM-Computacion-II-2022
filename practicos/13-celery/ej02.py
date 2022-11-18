from ej01 import pot, root, log
import click

def read_matrix(path):
    with open(path, 'r') as file:
        matrix = file.readlines()
        matrix = [line.split(',') for line in matrix]
        return matrix

def calculator(fun, matrix):
    new_matrix: list= []
    for row in matrix:
        new_row = []
        for element in row:
            element = calculate(fun, element)
            new_row.append(element)
        new_matrix.append(new_row)
    return new_matrix

def calculate(fun, element):
    functions = {
        'pot': pot.delay(element),
        'raiz': root.delay(element),
        'log': log.delay(element)
    }
    return functions[fun]

@click.command()
@click.option('-f', '--file', help="Ruta del archivo")
@click.option('-c', '--calcfunc', help="Funcion a utilizar")

def main():
    results = calculator(click.calcfunc, read_matrix(click.file))
    print(results)

if __name__ == '__main__':
    main()