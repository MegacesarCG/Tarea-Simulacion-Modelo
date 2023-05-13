from vardiscretas import hipergeometrica, media_hipergeometrica, var_hipergeometrica

# Ejemplo base, obtener en 5 cartas dos ases en una baraja de cartas.
POBLACION = 52
MUESTRA = 5
NUM_CATEGORIA = 4
CANT_CATEGORIA = 2

if __name__ == "__main__":
    print("----[Hipergeometrica]-----")
    print("Poblacion total:", POBLACION)
    print("Muestra extraida:", MUESTRA)
    print("Elementos en la categoria deseada", NUM_CATEGORIA)
    print("Numero de elementos de categoria en la muestra:", CANT_CATEGORIA)
    print("Probabilidad:", hipergeometrica(POBLACION, MUESTRA, NUM_CATEGORIA, CANT_CATEGORIA))
    print("Media", media_hipergeometrica(POBLACION, MUESTRA, NUM_CATEGORIA))
    print("Varianza", var_hipergeometrica(POBLACION, MUESTRA, NUM_CATEGORIA))
