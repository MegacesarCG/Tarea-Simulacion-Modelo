import csv
from random import randint

CANT_ELEMENTOS = 1000
MIN_EDAD = 10
MAX_EDAD = 80

def generarLista():
    lista = []
    for i in range(CANT_ELEMENTOS):
        elem = randint(MIN_EDAD, MAX_EDAD)
        lista = lista + [elem]
    return lista

with open("datos.csv", mode="w") as file:
    file.write("Edad\n")
    for elem in generarLista():
        file.write(str(elem)+"\n")
    
if __name__ == "__main__":
    print("Generado")
