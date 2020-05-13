# Sumy częściowe

# Rozważ sumy częściowe szeregu deﬁniującego funkcję dzeta Riemanna:
#       dzeta(s) = // suma od k=1 do k=n z ( 1 / ( k^s)  )  //

# oraz funkcję eta Dirichleta:
#       eta(s) = // suma od k=1 do k=n z ( (-1)^(k-1) * ( 1 / ( k^s ) ) ) //

# Dla:
#   s = 2, 3.6667, 5, 7.2, 10       oraz        n = 50, 100, 200, 500, 1000
#   oblicz wartości funkcji dzeta(s) i eta(s) w pojedynczej precyzji sumując w przód, a następnie wstecz.
#   Porównaj wyniki z rezultatami uzyskanymi dla podwójnej precyzji. Dokonaj interpretacji otrzymanych wyników.

# Wskazówka
# Porównaj oszacowania względnych błędów dla działań
#   fl(fl(x + y)+ z)
#   oraz
#   fl(x + fl(y + z))
#   przy założeniu, że |x + y| < |y + z|.


import numpy as np
from textFunctions import *
import textFunctions

def dzeta(s, n, singlePrecision=True):
    if singlePrecision:
        print("here1")
        wynik = np.float32(0.0)
        for k in range(1, n+1):  # dla k=1,2, ... , n
            wynik = np.float32(wynik + 1 / (k ^ s))     # "castowanie" było potrzebne, gdyż Python sam dokonywał zamiany typów

    else:
        print("here2")
        wynik = np.float64(0.0)
        for k in range(1, n+1):  # dla k=1,2, ... , n
            wynik = np.float64(wynik + 1 / (k ^ s))
    return wynik


def dzeta_backwards(s,n, singlePrecision=True):
    if singlePrecision:
        print("here1")
        wynik = np.float32(0.0)
        for k in range(n, 0, -1):
            wynik = np.float32(wynik + 1 / (k ^ s))

    else:
        print("here2")
        wynik = np.float64(0.0)
        for k in range(n, 0, -1):
            wynik = np.float64(wynik + 1 / (k ^ s))
    return wynik

print(dzeta(0,5))


printSpacer()
print(dzeta_backwards(0,5))
print(dzeta_backwards(0,5,False))

#print(dzeta_backwards(0,5,False))