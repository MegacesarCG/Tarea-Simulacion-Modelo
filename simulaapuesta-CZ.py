# Simulador de apuestas, hecho por César Zabala

import random

DINERO_INICIAL = 1000
DINERO_APOSTADO = 500
CANT_PARTIDAS = 100

# Si quiere mostrar los datos de rondas entre cada partida pon True.
verbose = True

def apostar(dinero):
    dado = random.randint(1, 6)
    if(dado % 2 == 0):
        dinero = dinero * 2
    else:
        dinero = 0
    return dinero

def simular_partida(dinero):
    rondas = 0
    while(dinero > 0):
        dinero = dinero - DINERO_APOSTADO
        dinero = dinero + apostar(DINERO_APOSTADO)
        rondas = rondas + 1
    return rondas

def promedio_rondas(registro_rondas):
    sumatoria = 0
    for r in registro_rondas:
        sumatoria = sumatoria + r
    return sumatoria // len(registro_rondas)

def simulacion():
    partidas = 0
    registro_rondas = []
    while(partidas < CANT_PARTIDAS):
        rondas = simular_partida(DINERO_INICIAL)
        partidas = partidas + 1
        registro_rondas = registro_rondas + [rondas]
        if verbose == True:
            print("Partida #", partidas, "=", rondas, "rondas")
    print("--------------------------------")
    return promedio_rondas(registro_rondas)

if __name__ == "__main__":
    print("Ejecutando simulacion de apuestas...")
    print("Promedio de entre partidas:", simulacion(),"rondas")
