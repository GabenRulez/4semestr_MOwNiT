# Sumowanie liczb pojedynczej precyzji

# 1.    Napisz program, który oblicza sumę N liczb pojedynczej precyzji przechowywanych w tablicy
#       o N = 10^7  elementach. Tablica wypełniona jest tą samą wartością v z przedziału [0.1, 0.9] np. v = 0.53125.

# 2.    Wyznacz bezwzględny i względny błąd obliczeń. Dlaczego błąd względny jest tak duży?

# 3.    W jaki sposób rośnie błąd względny w trakcie sumowania?
#       Przedstaw wykres (raportuj wartość błędu co 25000 kroków) i dokonaj jego interpretacji.

# 4.    Zaimplementuj rekurencyjny algorytm sumowania, działający jak na rysunku poniżej.
#       (niczym drzewo binarne)

# 5.    Wyznacz bezwzględny i względny błąd obliczeń. Dlaczego błąd względny znacznie zmalał?

# 6.    Porównaj czas działania obu algorytmów dla tych samych danych wejściowych.

# 7.    Przedstaw przykładowe dane wejściowe, dla których algorytm sumowania rekurencyjnego zwraca niezerowy błąd.


import numpy as np
import textFunctions
from textFunctions import *
import matplotlib.pyplot as plt
import time


def prostaSuma(tablica):
    wynik = np.float32(0)
    for i in range(len(tablica)):
        wynik += tablica[i]
    return wynik

def tworzLosowaMacierz(zakres_start, zakres_end, wielkosc):
    macierz = (zakres_end - zakres_start) * np.random.random_sample(wielkosc) + zakres_start
    return macierz

def tworzMacierzOJednakowychWartosciach(wartosc, wielkosc):
    macierz = np.full((wielkosc), wartosc, dtype=np.float32)
    return macierz

def losowaLiczbaZPrzedzialu(zakres_start, zakres_end):
    wartosc = (zakres_end - zakres_start) * np.random.random(1) + zakres_start
    return wartosc[0]

def bladBezwzgledny(wartosc_dokladna, wartosc_zmierzona):
    return abs(wartosc_dokladna - wartosc_zmierzona)

def bladWzgledny(wartosc_dokladna, wartosc_zmierzona):
    if wartosc_dokladna==0:
        wartosc_dokladna = 1e-16
    return ( bladBezwzgledny( wartosc_dokladna, wartosc_zmierzona ) ) / wartosc_dokladna

def sumaBinarna(tablica):
    start = 0
    koniec = len(tablica)-1
    return pomocSumyBinarnej(tablica, start, koniec)

def pomocSumyBinarnej(tablica, start, koniec):
    if start == koniec:
        return tablica[start]

    elif start + 1 == koniec:
        return tablica[start] + tablica[koniec]

    else:
        breakout = int( int(start+koniec)/2 )
        return pomocSumyBinarnej(tablica, start, breakout) + pomocSumyBinarnej(tablica, breakout+1, koniec)


def rysujWykres(wartosc, zasieg, skok, save=False, logs=False):
    filename = "{}__zakres-{}__skok-{}.png".format("wzrost-bledu-wzglednego", zasieg, skok)
    printTitle("Rozpoczynam generowanie " + filename)

    wartosc = np.float32(wartosc)

    bledy = []
    skoki = []

    i = skok
    while(i < zasieg):

        temp = bladWzgledny(wartosc * i, prostaSuma(tworzMacierzOJednakowychWartosciach(wartosc, i))) * 100
        bledy.append(temp)
        skoki.append(i)

        if logs:
            print("Ukończono obliczanie sumy {} elementów. Błąd względny wyniósł: {}%".format(i,temp))

        i += skok

    fig1, ax1 = plt.subplots()
    ax1.set_title("'{}', skok: {}".format("Wzrost błędu względnego", skok))

    ax1.set_xlabel("Ilość sumowań")
    ax1.set_ylabel("Błąd względny w %")
    ax1.plot(skoki, bledy)
    fig1.show()
    if save:
        fig1.savefig("zad1/plots/"+filename)
        printTitle("Plik " + filename + " został zapisany.")
        pass
    else:
        printTitle("Skończone generowanie " + filename)

###########################################################

printTitle("Początek programu")

wartosc = np.float32( losowaLiczbaZPrzedzialu(0.1, 0.9) )
N = 10000000    # N = 10^7
macierz = tworzMacierzOJednakowychWartosciach(wartosc, N)

print("Wartość wybranej losowej liczby to {}.".format(wartosc))
print("Wielkość macierzy to {}.".format(N))


printSpacer()


printTitle("'Prosta suma' - najzwyklejsze dodawanie")
tempProstaSuma = prostaSuma(macierz)
tempProsteMnozenie = wartosc * N
print("Obliczona suma: {}".format(tempProstaSuma))
print("Wynik mnożenia: {}".format(tempProsteMnozenie))
printSpacer()
tempBladBezwzgledny = bladBezwzgledny(tempProsteMnozenie, tempProstaSuma)
tempBladWzgledny = bladWzgledny(tempProsteMnozenie, tempProstaSuma)
print("Błąd bezwzględny: {}".format(tempBladBezwzgledny))
print("Błąd względny: {} = {}%".format(tempBladWzgledny, tempBladWzgledny*100))

# 1.2
# Błąd względny jest tak duży, z racji, że każda operacja dodawania wprowadza "błąd" (maszynowy epsilon),
# ściśle związany z dokładnością mantysy
# (tak naprawdę połową możliwej "różnicy" w zapisie liczby typu float32).


printSpacer()


printTitle("Suma liczona drzewem binarnym - rekurencyjnie")
tempSumaRekurencyjna = sumaBinarna(macierz)
tempProsteMnozenie = wartosc * N
print("Obliczona suma: {}".format(tempSumaRekurencyjna))
print("Wynik mnożenia: {}".format(tempProsteMnozenie))
printSpacer()
tempBladBezwzgledny = bladBezwzgledny(tempProsteMnozenie, tempSumaRekurencyjna)
tempBladWzgledny = bladWzgledny(tempProsteMnozenie, tempSumaRekurencyjna)
print("Błąd bezwzględny: {}".format(tempBladBezwzgledny))
print("Błąd względny: {} = {}%".format(tempBladWzgledny, tempBladWzgledny*100))

# 1.5
# Błąd względny znacznie zmalał zapewne z faktu, że dodawanie 'proste' bazowało na utworzeniu jednej dużej liczby
# i N operacjach dodania małych liczb.
# W takim przypadku znaczna część cyfr znaczących "małych liczb" nie zmieści się wśród cyfr znaczących dużej liczby.
# W sumowaniu binarnym natomiast, cyfry znaczące praktycznie zawsze się pokrywają,
# przez co powstały błąd jest niewielki, praktycznie znikomy.


printSpacer(2)


printTitle("Jak rośnie błąd względny w trakcie sumowania? ('prosta suma')", 0)

rysujWykres(wartosc, 10000000, 25000, save=False, logs=True)     # jeśli długo zajmuje, to proszę wykomentować ta linijkę

# 1.3
# Błąd względny "prostej sumy" rośnie logarytmicznie, ale "fazami".
# Bład wynika zapewne z dodawania małych liczb do jednej bardzo dużej
# - cyfry znaczące tych małych liczb nie mieszczą się w cyfrach znaczących dużej.
# "Fazy" - te nagłe spadki tłumaczyłbym faktem, że porównuję wynik dodawania z wynikiem mnożenia,
# zakładając, że wynik mnożenia jest w pełni poprawny, a nie jest to prawdą.
# Uskoki powstały w miejscach, gdzie następował "przeskok" na ostatnim, najmniej znaczącym bicie wyniku mnożenia.





printSpacer()


printTitle("Porównanie czasu wykonania dla dwóch algorytmów")

N2 = 1000000
print("Tworzę nową macierz o {} elementach.".format(N2))
macierz2 = tworzMacierzOJednakowychWartosciach(wartosc, N2)
printSpacer()

start = time.process_time()
prostaSuma(macierz2)
czas_1 = time.process_time() - start

start = time.process_time()
sumaBinarna(macierz2)
czas_2 = time.process_time() - start

print("Czas 'prostej sumy': {}s".format(czas_1))
print("Czas sumy 'binarnej': {}s".format(czas_2))

# 1.6
# Dodawanie rekurencyjne jest znacznie dłuższe, a wynika to zapewne z racji tworzenia nowych "tymczasowych" sum,
# które dopiero na samym końcu dodawania zapisywane są jako "odpowiedni wynik".



printSpacer()


printTitle("Przykładowe dane, dla których sumowanie rekurencyjne ma niezerowy błąd")

wartosc_przykladowa = np.float32(1.999899983406067)
ilosc_przykladowa = 10

macierz_przykladowa = tworzMacierzOJednakowychWartosciach(wartosc_przykladowa, ilosc_przykladowa)
print("Wartość sumowana: {} razy {}".format(wartosc_przykladowa, ilosc_przykladowa))
print("Błąd względny: {}".format( bladWzgledny(19.99899983406067, sumaBinarna(macierz_przykladowa)) ))

