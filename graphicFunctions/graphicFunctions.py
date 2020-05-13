import textFunctions
from textFunctions import *
import matplotlib.pyplot as plt


def rysujWykres(funkcja, zasieg, skok, save=False, logs=False, xlabel="", ylabel=""):
    # filename = 'porownanie_czasu_algorytmow__zakres-' + str(zasieg) + '__skok-' + str(skok) + '.png'
    filename = "{}__zakres-{}__skok-{}.png".format(funkcja.__name__, zasieg, skok)
    printTitle("Rozpoczynam generowanie " + filename)

    wyniki = []
    skoki = []

    i = 0
    while (i < zasieg):

        wynik = funkcja(i)
        wyniki.append(wynik)
        skoki.append(i)
        if logs:
            print("Ukończono wielkość {}".format(i))
        i += skok

    fig1, ax1 = plt.subplots()
    ax1.set_title("'{}', skok: {}".format(funkcja.__name__, skok))

    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.plot(skoki, wyniki)
    fig1.show()
    if save:
        fig1.savefig("plots/" + filename)
        printTitle("Plik " + filename + " został zapisany.")
        pass
    else:
        printTitle("Skończone generowanie " + filename)



class fibo:
    valuesList = [0, 1, 1]

    @staticmethod
    def get(i):
        if i >= len(fibo.valuesList):
            fibo.get(i-2)
            fibo.get(i-1)
            fibo.valuesList.append(fibo.valuesList[i-2] + fibo.valuesList[i-1])
        return fibo.valuesList[i]

