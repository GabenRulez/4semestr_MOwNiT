# Metoda Gaussa-Jordana

# Napisz i sprawdź funkcję rozwiązującą układ równań liniowych n × n metodą Gaussa-Jordana.
# Dla rozmiarów macierzy współczynników większych niż 500 × 500 porównaj
# czasy działania zaimplementowanej funkcji z czasami uzyskanymi dla
# wybranych funkcji bibliotecznych.


import numpy as np
import time
import matplotlib.pyplot as plt
from textFunctions.textFunctions import *


def uklad_rownan_liniowych(n, zakres_start=0, zakres_end=10):
    macierz_glowna = (zakres_end - zakres_start) * np.random.random_sample((n, n)) + zakres_start
    macierz_wynikow = (zakres_end - zakres_start) * np.random.random_sample((n,1)) + zakres_start

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

printTitle("Początek programu")
A, B = uklad_rownan_liniowych(3)
print("macierz A:")
print(A)
printSpacer(1)
print("macierz: B")
print(B)

printTitle("Porównanie wyników i czasów")
start = time.process_time()
print("linalg.solve: ")
print(np.linalg.solve(A, B), "\n czas: ", time.process_time() - start)

printSpacer(1)
start = time.process_time()
print("moje: ")
print(rozwiaz_metoda_Gaussa_Jordana(A, B), "\n czas: ", time.process_time() - start)
printLineSpacer(1)

# jak widać, przy tak małych danych jak n=3 oba algorytmy wykonują się wręcz natychmiastowo
# - czas jest zbyt mały, by nawet pokazać go we float'cie

# wyniki zaimplementowanego przeze mnie algorytmu pokrywają się z tymi z biblioteki,
# przez co wnioskuję, że poprawnie go zaimplementowałem


##################################################

def porownaj_dwa_algorytmy(zasieg, skok, save=False, logs=False):
    filename = 'porownanie_czasu_algorytmow__zakres-' + str(zasieg) + '__skok-' + str(skok) + '.png'
    printTitle("Rozpoczynam generowanie " + filename)

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
        if logs:
            print("Ukończono macierz " + str(i) + "x" + str(i))

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
        fig1.savefig("zad1/plots/"+filename)
        printTitle("Plik " + filename + " został zapisany.")
        pass
    else:
        printTitle("Skończone generowanie " + filename)


# tutaj uruchamiam generowanie prób
# argumenty są w kolejności ( zasięg, skok o N, czy zapisać do pliku?, czy pisać logi z generowania )

# używam "skoku", gdyż przy zakresie od 0 do 1000 nie potrzeba nam informacji z dokładnością do 1
# (losowość przy generowaniu macierzy tworzy "szum")


porownaj_dwa_algorytmy(100, 1, True)
#porownaj_dwa_algorytmy(100, 5, True)
#porownaj_dwa_algorytmy(250, 10, True)
#porownaj_dwa_algorytmy(500, 10, True)
#porownaj_dwa_algorytmy(1000, 25, True)
#porownaj_dwa_algorytmy(1000, 1, True, True)


# Jak można zauważyć na tych przykładach:

# - czas obliczenia jest zależny od wprowadzonych danych,
#   tj. istnieją układy, które rozwiązują się szybciej niż inne dla tej samej wartości N

# - zaimplementowany przeze mnie algorytm zdaje się mieć mniej "szumu",
#   tj. różnice pomiędzy czasem wykonania dla N=50 i N=60 różnią się niewiele (zazwyczaj o jednostkę dokładności float)
#   a z kolei algorytm w tablicy miewa momenty, w których rozwiązuje układ w czasie zerowym
#   (a przynajmniej tak małym, że float nie jest w stanie wyrazić tej wielkości)

# - zaimplementowany przeze mnie algorytm w porównaniu z bibliotecznym
#   jest przy dużych wartościach N (>100) o wiele gorszy
#   np. dla N=2500 "mój" algorytm zakończył pracę w ~55sekund, a "linalg.solve" w niecałą sekundę
