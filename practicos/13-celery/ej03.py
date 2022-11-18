from math import sqrt, log10
from ej01 import app

@app.task
def log(element) -> int:
    return log10(int(element))

@app.task
def root(element) -> int:
    return sqrt(int(element))

@app.task
def pot(element) -> int:
    return int(element)**int(element)
