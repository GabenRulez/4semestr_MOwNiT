# Metoda potęgowa

# Napisz funkcję obliczającą metodą potęgową dominującą wartość własną (największą co do modułu)
# i odpowiadający jej wektor własny dla danej macierzy rzeczywistej symetrycznej.
# Sprawdź poprawność działania programu porównując własną implementację z wynikami funkcji bibliotecznej.
# Przedstaw na wykresie zależność czasu obliczeń od rozmiaru macierzy (rozmiary macierzy 100x100, 500x500, ...).

# • Powtarzaj mnożenie wektora xi przez macierz A: xi+1 = Axi, dzieląc za każdym razem wektor wynikowy przez ||xi+1||
# • Element wektora xi o największej wartości bezwzględnej zbiega do dominującej wartości własnej
# • Przeskalowany wektor xi zbiega do dominującego wektora własnego
# • Obliczenia powinny się zatrzymać po przekroczeniu maksymalnej liczby iteracji, albo w przypadku gdy ||xi −xi+1|| < e (kryterium małej poprawki)
# • Pod koniec obliczeń znormalizuj otrzymany wektor własny.

import numpy as np
import math
import time
import matplotlib.pyplot as plt

from textFunctions import *


def metodaPotegowa(matrix_A, iterations=1000, epsilon=0.000001):
    n = len(matrix_A)
    vector_X = np.zeros((n,1))
    for i in range(n):  # ustaw wartość wektora X
        vector_X[i][0] = float(np.random.randint(0,100))/100

    for i in range(iterations): # limit iteracji

        new_vector_X = np.zeros((n,1))
        for i in range(n):      # twórz nowy wektor i wypełnij go zgodnie z mnożeniem macierzy
            for j in range(n):
                new_vector_X[i][0] += matrix_A[i][j] * vector_X[j][0]



        temp = 0                # obliczanie normy i podzielenie przez nią wektora
        for i in range(n):
            temp += new_vector_X[i][0] * new_vector_X[i][0]
        forma_z_X = math.sqrt(temp)
        for i in range(n):
            new_vector_X[i][0] = new_vector_X[i][0] / forma_z_X;



        temp_Vector = vector_X  # sprawdzenie "kryterium małej poprawki"
        for i in range(n):
            temp_Vector[i][0] -= new_vector_X[i][0]
        temp = 0
        for i in range(n):
            temp += temp_Vector[i][0] * temp_Vector[i][0]
        forma_z_temp_Vector = math.sqrt(temp)
        if forma_z_temp_Vector < epsilon:
            break



        for i in range(n):      # zamiana starego wektora na nowy
            vector_X[i][0] = new_vector_X[i][0]

    dominujaca_wartosc_wlasna = 0
    for i in range(n):
        if abs(vector_X[i][0]) > dominujaca_wartosc_wlasna:
            dominujaca_wartosc_wlasna = vector_X[i][0]


    if np.linalg.norm(vector_X) != 0:
        return dominujaca_wartosc_wlasna, vector_X/np.linalg.norm(vector_X)
    else:
        return dominujaca_wartosc_wlasna, vector_X




printLineSpacer()

A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

dom_war_wla, wektor = metodaPotegowa(A)
print(dom_war_wla)
print(wektor)


w,v = np.linalg.eig(A)  # niestety nie wiem, skąd z tych funckji wyliczyć "wartość własną", jedyne co ona zwraca to dwie macierze
print(w)
print(v)


# Wyniki są podobne (tj. pierwsza kolumna dominującego wektora własnego)

printLineSpacer()


def porownaj_dwa_algorytmy(zasieg, skok, save=False, logs=False):
    filename = 'porownanie_czasu_algorytmow__zakres-' + str(zasieg) + '__skok-' + str(skok) + '.png'
    printTitle("Rozpoczynam generowanie " + filename)

    czasy_linalg = []
    czasy_moje = []
    skoki = []

    i = 0
    while(i < zasieg):

        macierz_A = np.random.randint(low=0, high=5, size=(i, i))

        start = time.process_time()
        np.linalg.eig(macierz_A)
        czas = time.process_time() - start
        czasy_linalg.append(czas)

        start = time.process_time()
        metodaPotegowa(macierz_A)
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
    ax1.plot(skoki, czasy_moje, label="moja implementacja metody potęgowej")
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


porownaj_dwa_algorytmy(1000, 25, True, True)

# w folderze zad1/plots znajdują się wygenerowane wykresy porównujące czasy wykonania mojego algorytmu i bibliotecznego