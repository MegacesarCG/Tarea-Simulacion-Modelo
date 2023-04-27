import statistics


# MEDIDAS DE TENDENCIA CENTRAL

def media(datos):
    return statistics.mean(datos)

def moda(datos):
    return statistics.mode(datos)

def mediana(datos):
    return statistics.median(datos)

def quartiles(datos):
    return statistics.quantiles(datos, n=4)

def deciles(datos):
    return statistics.quantiles(datos, n=10)

def percentiles(datos):
    return statistics.quantiles(datos, n=100)

# MEDIDAS DE DISPERSION

def rango(datos):
    return abs(max(datos) - min(datos))

def varianza(datos):
    return statistics.variance(datos)

def desviacion(datos):
    return statistics.stdev(datos)

def cv(datos):
    return abs(desviacion(datos) / media(datos))
