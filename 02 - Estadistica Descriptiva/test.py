import csv

from descriptiva import *

with open("datos.csv", mode="r") as file:
    lineas = csv.reader(file)
    primeralinea = True
    datos = []
    for fila in lineas:
        if primeralinea == True:
            primeralinea = False 
        else:
            datos = datos + [int(fila[0])]

if __name__ == "__main__":
    print("############################")
    print("MEDIDAS DE TENDENCIA CENTRAL")
    print("############################")
    print("Media:",media(datos))
    print("Moda:",moda(datos))
    print("Mediana:",mediana(datos))
    print("Quartiles:", quartiles(datos))
    print("Deciles:", deciles(datos))
    print("Percentiles:", percentiles(datos))
    print("\n############################")
    print("MEDIDAS DE DISPERSION")
    print("############################")
    print("Rango:",rango(datos))
    print("Varianza:",varianza(datos))
    print("Desviacion:",desviacion(datos))
    print("Coeficiente de Desviacion:", cv(datos))
