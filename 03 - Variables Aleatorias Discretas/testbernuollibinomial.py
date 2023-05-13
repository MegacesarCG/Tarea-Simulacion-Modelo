
from vardiscretas import probabilidad, bernuolli, media_bernuolli, var_bernuolli, binomial, media_binomial, var_binomial, hipergeometrica

CASOS_FAVORABLES = 1
CASOS_POSIBLES = 2
# Binomial
NUM_VECES = 10
NUM_EXITOS = 5

if __name__ == "__main__":
    print("Casos favorables:",CASOS_FAVORABLES)
    print("Casos posibles:",CASOS_POSIBLES)
    p = probabilidad(CASOS_FAVORABLES, CASOS_POSIBLES)
    print("Probabilidad:", p)
    print("----[Bernuolli]-----")
    print("Probabilidad:", bernuolli(p))
    print("Media:",media_bernuolli(p))
    print("Varianza:", var_bernuolli(p))
    print("----[Binomial]-----")
    print("Numero de repeticiones",NUM_VECES)
    print("Numero de exitos esperados:",NUM_EXITOS)
    print("Probabilidad:", binomial(p,NUM_VECES,NUM_EXITOS))
    print("Media:",media_binomial(p, NUM_VECES))
    print("Varianza:", var_binomial(p, NUM_VECES))
