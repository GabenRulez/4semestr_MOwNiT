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
        wynik = np.float32(0.0)
        for k in range(1, n + 1):  # dla k=1,2, ... , n
            wynik = np.float32( wynik + 1 / (k ** s) )  # "castowanie" było potrzebne, gdyż Python sam dokonywał zamiany typów

    else:
        wynik = np.float64(0.0)
        for k in range(1, n + 1):  # dla k=1,2, ... , n
            wynik = np.float64(wynik + 1 / (k ** s))
    return wynik


def dzeta_backwards(s, n, singlePrecision=True):
    if singlePrecision:
        wynik = np.float32(0.0)
        for k in range(n, 0, -1):
            wynik = np.float32(wynik + 1 / (k ** s))

    else:
        wynik = np.float64(0.0)
        for k in range(n, 0, -1):
            wynik = np.float64(wynik + 1 / (k ** s))
    return wynik


def eta(s, n, singlePrecision=True):
    if singlePrecision:
        wynik = np.float32(0.0)
        for k in range(1, n + 1):  # dla k=1,2, ... , n
            wynik = np.float32(wynik + (-1) ** (k - 1) * (1 / (k ** s)))

    else:
        wynik = np.float64(0.0)
        for k in range(1, n + 1):  # dla k=1,2, ... , n
            wynik = np.float64(wynik + (-1) ** (k - 1) * (1 / (k ** s)))
    return wynik


def eta_backwards(s, n, singlePrecision=True):
    if singlePrecision:
        wynik = np.float32(0.0)
        for k in range(n, 0, -1):
            wynik = np.float32(wynik + (-1) ** (k - 1) * (1 / (k ** s)))

    else:
        wynik = np.float64(0.0)
        for k in range(n, 0, -1):
            wynik = np.float64(wynik + (-1) ** (k - 1) * (1 / (k ** s)))
    return wynik


printTitle("Początek programu")

wartosci_s = [2, 3.6667, 5, 7.2, 10]
wartosci_n = [50, 100, 200, 500, 1000]

print("Wartości s: ", wartosci_s)
print("Wartości n: ", wartosci_n)

printSpacer()

printTitle("Obliczenia dzeta Riemanna i eta Dirichleta")

for s in wartosci_s:
    for n in wartosci_n:
        printTitle("s = {}   n = {}".format(s,n))
        print("Pojedyncza precyzja:")
        print("dzeta 'w przód': {0:<18}      eta 'w przód':  {0:<18}".format( dzeta(s, n, True), eta(s, n, True) ))
        print("dzeta 'w tył':   {0:<18}      eta 'w tył':    {0:<18}".format( dzeta_backwards(s, n, True), eta_backwards(s, n, True) ))
        printSpacer()
        print("Podwójna precyzja:")
        print("dzeta 'w przód': {0:<18}      eta 'w przód':  {0:<18}".format(dzeta(s, n, False), eta(s, n, False)))
        print("dzeta 'w tył':   {0:<18}      eta 'w tył':    {0:<18}".format(dzeta_backwards(s, n, False), eta_backwards(s, n, False) ))

printTitle("Koniec programu")


# 3
# W przypadku liczb pojedynczej precyzji:
# Obliczanie dzety "w tył" tworzy bardziej dokładny wynik.
# Moim zdaniem jest to wynik dodawania dużych liczb do małej liczby, zamiast dodawania małych liczb do jednej dużej.

# W przypadku liczb podwójnej precyzji:
# Tutaj kolejność wykonywania (w przód / w tył) nie ma już takiego wpływu na wynik,
# a różnice między jednym a drugim występują jedynie na ostatniej / ostatnich dwóch najmniej znaczących cyfrach.