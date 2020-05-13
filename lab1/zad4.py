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
# Stworzyłem dwa diagramy
# (zad4\plots\Diagram_Bifurkacyjny__r-3.75-3.8__dokladnosc-10000_dotted_single.png) i
# (zad4\plots\Diagram_Bifurkacyjny__r-3.75-3.8__dokladnosc-10000_dotted_double.png)

# w których obliczenia wykonywałem z użyciem pojedynczej(single) i podwójnej(double) precyzji.
# Same wykresy wyglądają bardzo podobnie, i choć może to być jedynie moje złudzenie to mam wrażenie,
# że obliczenia podwójną precyzją stworzyły bardziej płynne linie (przy attractorach).

# Oba wykresy pokazały, że występuje w r ~= 3.775 moment "wyjścia z chaosu", gdzie powstało kilka linii,
# na których są wszystkie punkty z tego zakresu.
# Niedaleko dalej wszystko znowu przechodzi w chaos i widać niektóre miejsca, w których punkty "bardziej się zbierają"
# (średnia wartość x nie jest 0.5).

#stworzDiagramBifurkacyjny(3.75, 3.8, dokladnosc=10000, wartosci_x0=[0.4, 0.67, 0.9], dotted=True, save=True, logs=True, precyzja="single")
#stworzDiagramBifurkacyjny(3.75, 3.8, dokladnosc=10000, wartosci_x0=[0.4, 0.67, 0.9], dotted=True, save=True, logs=True, precyzja="double")


printSpacer()



# 4.c
# Przy r = 4 ilość iteracji dla różnych x0 potrzebna do osiągnięcia zera jest niewielka (~2000).
# Przy testowaniu wpisanych przeze mnie liczb, wszystkie zmierzały do 0.
# Dopiero gdy zmieniłem te x0 na wartości losowe napotkałem parę przypadków,
# gdzie twardy limit miliona iteracji był niewystarczający.
# Można chyba założyć, że te konkretne wartości oscylują w nieskończoność pomiędzy 0 a 1.
# Porównując wartości bardzo sobie bliskie (jak x0 = 0.3 i x0 = 0.30001) ilość iteracji
# zdaje się być zupełnie ze sobą niepowiązana i nieprzewidywalna.

printTitle("Ile iteracji przy r=4, aby x_n = 0")

r = 4
rozne_x0 = []
for i in range(10):
    rozne_x0.append( np.random.random(1)[0] )

srednia = 0

for x_0 in rozne_x0:
    print("Dla x0 = {}".format(x_0))
    iteracje = 0
    x = np.float32(x_0)
    while x!=0:
        x = getNextElement(x, r, "single")
        iteracje = iteracje + 1

        if iteracje>=1000000:   # hardlimit, na wypadek niespodziewanej pętli
            break
    srednia += iteracje
    print("Ilość iteracji: {}".format(iteracje))
    printSpacer()

srednia = srednia / len(rozne_x0)
printTitle("Średnia ilość iteracji: {}".format(srednia))


