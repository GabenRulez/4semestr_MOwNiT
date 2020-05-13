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

def getNextElement(poprzedni, r, precyzja=""):
    if precyzja=="single":
        poprzedni = np.float32(poprzedni)
        r = np.float32(r)
        return np.float32( r * poprzedni * (1-poprzedni) )

    elif precyzja=="double":
        poprzedni = np.float64(poprzedni)
        r = np.float64(r)
        return np.float64(r * poprzedni * (1 - poprzedni))

    else:
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




def stworzDiagramBifurkacyjny(r_start, r_koniec, dokladnosc=400, wartosci_x0=[], max_iterations=1000, save=False, dotted=False, logs=False, precyzja=""):
    filename = "Diagram_Bifurkacyjny__r-{}-{}__dokladnosc-{}".format(r_start, r_koniec, dokladnosc)
    if dotted:
        filename = filename + "_dotted"
    else:
        filename = filename + "_plotted"

    if precyzja!="":
        filename = filename + "_{}".format(precyzja)
    filename = filename + ".png"

    printTitle("Rozpoczynam generowanie " + filename)

    fig1, ax1 = plt.subplots()
    ax1.set_title("Diagram bifurkacyjny")
    ax1.set_xlabel("Wartość r")
    ax1.set_ylabel("Wartość x")

    wartosci_r = np.linspace(r_start, r_koniec, dokladnosc)

    for x_0_iter in range(len(wartosci_x0)):
        if logs:
            printTitle("Rozpoczynam obliczenia dla x0 = {}".format(wartosci_x0[x_0_iter]))

        wyniki_x0 = []
        for r in wartosci_r:
            temp_last = wartosci_x0[x_0_iter]

            if precyzja=="single":
                temp_last = np.float32(temp_last)
            elif precyzja=="double":
                temp_last = np.float64(temp_last)

            for i in range(max_iterations):

                if precyzja=="":
                    temp_last = getNextElement(temp_last, r)
                else:
                    temp_last = getNextElement(temp_last, r, precyzja)

            wyniki_x0.append(temp_last)

        if dotted:
            ax1.scatter(wartosci_r, wyniki_x0, label="x0={0:4}".format(wartosci_x0[x_0_iter]), s=2)
        else:
            ax1.plot(wartosci_r, wyniki_x0, label="x0={0:4}".format(wartosci_x0[x_0_iter]))

        if logs:
            printTitle("Koniec obliczeń dla x0 = {}".format(wartosci_x0[x_0_iter]))


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
# Stworzyłem diagram bifurkacyjny dla trzech różnych wartości x_0 i zakresu r [1.0, 4.0]
# (zad4/plots/Diagram_Bifurkacyjny__r-1.0-4.0__dokladnosc-400_plotted.png)
# Na obrazku widać, że dla r od 1 do ~3.0 poszczególne wykresy "nakładają się" i przypominają fragment krzywej logarytmicznej,
# lecz potem wręcz losowo "skaczą", oscylują między znacznie różnącymi się wartościami.

# Tak naprawdę łączenie tych elementów jako ciągły wykres może być złym pomysłem, dlatego zaimplementowałem też opcję
# z wykresem w postaci pojedynczych kropek (zad4/plots/Diagram_Bifurkacyjny__r-1.0-4.0__dokladnosc-400_dotted.png).


stworzDiagramBifurkacyjny(1.0, 4.0, 400, [0.4, 0.67, 0.9], dotted=True, save=False, logs=True)

printSpacer()

# 4.b


stworzDiagramBifurkacyjny(3.75, 3.8, 4001, [0.4, 0.67, 0.9], dotted=True, save=True, logs=True, precyzja="single")
stworzDiagramBifurkacyjny(3.75, 3.8, 4001, [0.4, 0.67, 0.9], dotted=True, save=True, logs=True, precyzja="double")
