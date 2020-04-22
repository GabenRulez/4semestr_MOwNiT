import numpy as np
import time
import matplotlib.pyplot as plt


import scipy as sp

# np.linalg.solve()

# np.linalg.lstsq()

# sp.linalg.lu()

def uklad_rownan_liniowych(n):  #
    #macierz_glowna = np.random.rand(0.0, 100.0, (n,n))
    #macierz_glowna = macierz_glowna / 1.0
    macierz_glowna = 10 * np.random.random_sample((n, n))

    #macierz_wynikow = np.random.randint(0.0,100.0,n)
    #macierz_wynikow = macierz_wynikow / 1.0
    macierz_wynikow = 10 * np.random.random_sample((n,1))

    return macierz_glowna, macierz_wynikow


def rozwiaz_metoda_Gaussa_Jordana(macierz_A, macierz_W):  # dostęp do macierzy definiuje jako macierz[y][x]
    n = len(macierz_W)

    for x in range(n):  # zaczynam iść od lewej strony macierzy głównej
        for y in range(x, n):  # szukam pierwszego niezerowego elementu w x-owej kolumnie
            if (macierz_A[y][x] == 0):
                pass
            else:   # jak znajdę niezerowy element, to dzielę wiersz przez taką liczbe, żeby w (x,y) było 1
                wspolczynnikA = macierz_A[y][x]
                macierz_A[y] = macierz_A[y] / wspolczynnikA
                macierz_W[y] = macierz_W[y] / wspolczynnikA
                for iterator in range(n):   # od wszystkich wierszy usuwam wielokrotność tego wiersza, aby powstała macierz diagonalna
                    if iterator==y:
                        pass
                    else:
                        wspolczynnikB = float(macierz_A[iterator][x] / macierz_A[y][x])
                        macierz_A[iterator] = macierz_A[iterator] - wspolczynnikB * macierz_A[y]
                        macierz_W[iterator] = macierz_W[iterator] - wspolczynnikB * macierz_W[y]
                break
    return macierz_W

##################################################

A, B = uklad_rownan_liniowych(3)
print("macierz A:")
print(A)
print("macierz: B")
print(B)

start = time.process_time()
print("linalg.solve: ", np.linalg.solve(A, B), "\n czas: ", time.process_time() - start)
start = time.process_time()
print("moje: ", rozwiaz_metoda_Gaussa_Jordana(A, B), "\n czas: ", time.process_time() - start)
    # jak widać, przy tak małych danych jak n=3 oba algorytmy wykonują się wręcz natychmiastowo - czas jest zbyt mały, by pokazać go we float'cie


##################################################

def porownaj_dwa_algorytmy(zasieg, skok, save=False):
    czasy_linalg = []
    czasy_moje = []
    skoki = []

    i = 0
    while(i < zasieg):

        macierz_A, macierz_W = uklad_rownan_liniowych(i)

        start = time.process_time()
        np.linalg.solve(macierz_A, macierz_W)
        czas = time.process_time() - start
        czasy_linalg.append(czas)

        start = time.process_time()
        rozwiaz_metoda_Gaussa_Jordana(macierz_A, macierz_W)
        czas = time.process_time() - start
        czasy_moje.append(czas)

        skoki.append(i)

        i += skok

    fig1, ax1 = plt.subplots()
    ax1.set_title("Porównanie czasu wykonania algorytmów, skok:" + str(skok) )
    ax1.set_xlabel("Szerokość macierzy NxN (number)")
    ax1.set_ylabel("Czas [seconds]")
    ax1.plot(skoki, czasy_linalg, label="linalg.solve")
    ax1.plot(skoki, czasy_moje, label="moja implementacja Gaussa-Jordana")
    ax1.legend()
    fig1.show()
    if save:
        filename = 'porownanie_czasu_algorytmow__zakres-' + str(zasieg) + '__skok-' + str(skok) + '.png'
        fig1.savefig(filename)
        pass



porownaj_dwa_algorytmy(100, 1, True)
porownaj_dwa_algorytmy(100, 10, True)
#porownaj_dwa_algorytmy(500, 10, True)
#porownaj_dwa_algorytmy(1000, 10, True)