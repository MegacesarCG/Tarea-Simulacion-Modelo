from vardiscretas import poisson, media_poisson, var_poisson

EXITOS_INTERVALO = 0.5
NUM_VECES = 1

if __name__ == "__main__":
    print("----[Poisson]----")
    print("Numero de exitos en el intervalo:", EXITOS_INTERVALO)
    print("Cantidad de aciertos:", NUM_VECES)
    print("Probabilidad:", poisson(EXITOS_INTERVALO,NUM_VECES))
    print("Media:", media_poisson(EXITOS_INTERVALO))
    print("Varianza:", var_poisson(EXITOS_INTERVALO))
