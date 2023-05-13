
from math import e

def probabilidad(a,b):
    return a/b

def coeficiente_binomial(n,x):
    i = n - x
    numerador = 1
    while(n > x and n > i):  
        numerador = numerador * n
        n = n - 1
    if(n == x):
        return numerador / factorial(i)
    else:
        return numerador / factorial(x)

def factorial(n):
    if(n == 0):
        return 1
    else:
        return n * factorial(n - 1)

# Distibucion de Bernuolli

def bernuolli(p):
    return 1 - p

def media_bernuolli(p):
    return p

def var_bernuolli(p):
    return p * (1 - p)

# Distibucion Binomial

def binomial(p,n,x):
    return coeficiente_binomial(n,x) * pow(p,x) * pow(1 - p, n - x)

def media_binomial(p, n):
    return n * p

def var_binomial(p, n):
    return n * p * (1 - p)

# Distribucion Hipergeometrica

def hipergeometrica(N,n,K,x):
    return (coeficiente_binomial(K,x) * coeficiente_binomial(N-K,n-x)) / coeficiente_binomial(N,n)

def media_hipergeometrica(N,n,K):
    return (n * K) / N

def var_hipergeometrica(N,n,K):
    return ((n * K) / N) * ((N - K) / N) * ((N - n) / (N - 1))

# Distribucion de Poisson

def poisson(lam, x):
    return (pow(e, 0 - lam) * pow(lam, x)) / factorial(x)

def media_poisson(lam):
    return lam

def var_poisson(lam):
    return lam

def exponencial():
    return 

if __name__ == "__main__":
    print(poisson(0.75,4))
