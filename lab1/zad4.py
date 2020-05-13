# Błędy zaokrągleń i odwzorowanie logistyczne

# Rozważ odwzorowanie logistyczne dane następującym wzorem rekurencyjnym
#       x_(n+1) = r * x_n * (1−xn)

# Przy czym 0 <= x_n <= 1 i r > 0.
# Zbadaj zbieżność procesu iteracyjnego określonego tym równaniem w zależności od wartości parametru r oraz x_0.

# a)    Dla różnych wartości r (1 <= r <= 4) oraz kilku wybranych wartości x_0 przedstaw na wykresie
#       wartości x_n uzyskane po wielu iteracjach odwzorowania logistycznego (diagram bifurkacyjny).
#       Dokonaj interpretacji otrzymanych wyników.

# b)    Dla tych samych wartości x_0 oraz r (3.75 <= r <= 3.8) porównaj trajektorie obliczone z użyciem pojedynczej
#       i podwójnej precyzji. Wyjaśnij otrzymane wyniki.

# c)    Dla r = 4 i różnych wartości x_0 wyznacz (pojedyncza precyzja) liczbę iteracji potrzebnych do osiągnięcia zera.
#       Przedstaw interpretację rezultatów.

import textFunctions
from textFunctions import *
import numpy as np
import matplotlib.pyplot as plt

def getNextElement(poprzedni, r):
    return r * poprzedni * (1-poprzedni)



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




def stworzDiagramyBifurkacyjneZx0(zasieg, skok, x_0, save=False, logs=False):
    filename = "{}__x0-{}__zakres-{}__skok-{}.png".format("Diagramy_Bifurkacyjne", x_0, zasieg, skok)
    printTitle("Rozpoczynam generowanie " + filename)

    x_0 = np.float32(x_0)

    r_1 = np.float32(1.253)
    r_2 = np.float32(2.5392)
    r_3 = np.float32(2.99924)

    wyniki_1 = [x_0]
    wyniki_2 = [x_0]
    wyniki_3 = [x_0]

    last_1 = x_0
    last_2 = x_0
    last_3 = x_0

    skoki = [0]

    i = 1
    while(i < zasieg):
        temp_1 = getNextElement(last_1, r_1)
        last_1 = temp_1
        wyniki_1.append(temp_1)

        temp_2 = getNextElement(last_2, r_2)
        last_2 = temp_2
        wyniki_2.append(temp_2)

        temp_3 = getNextElement(last_3, r_3)
        last_3 = temp_3
        wyniki_3.append(temp_3)

        skoki.append(i)
        if logs:
            print("Ukończono krok {}".format(i))
        i += skok

    fig1, ax1 = plt.subplots()
    ax1.set_title("Diagramy bifurkacyjne, skok:" + str(skok) )
    ax1.set_xlabel("Numer iteracji")
    ax1.set_ylabel("Wartość")
    ax1.plot(skoki, wyniki_1, label="x0={} r={}".format(x_0, r_1))
    ax1.plot(skoki, wyniki_2, label="x0={} r={}".format(x_0, r_2))
    ax1.plot(skoki, wyniki_3, label="x0={} r={}".format(x_0, r_3))
    ax1.legend()
    fig1.show()
    if save:
        fig1.savefig("zad4/plots/"+filename)
        printTitle("Plik " + filename + " został zapisany.")
        pass
    else:
        printTitle("Skończone generowanie " + filename)





printTitle("Początek programu")


# 4.a
# Stworzyłem

#stworzDiagramyBifurkacyjneZx0(150, 1, 0.5, save=True)
#stworzDiagramyBifurkacyjneZx0(20, 1, 0.21, save=True)

