from celery import Celery
from math import sqrt, log10

app = Celery('server_calc', broker='redis://localhost:6379', backend='redis://localhost:6379')

@app.task
def pot(element):
    return pow(element, element)

@app.task
def root(element):
    return sqrt(element)

@app.task
def log(element):
    return log10(element)