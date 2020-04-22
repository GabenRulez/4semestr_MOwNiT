import numpy as np
import scipy as sp

print(np.random.normal()/100)

np.random.normal()


# jejku, ile to zajmuje

####

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


A, B = uklad_rownan_liniowych(3)
print("macierz A:")
print(A)
print("macierz: B")
print(B)


def rozwiaz_metoda_Gaussa_Jordana(macierz_A, macierz_W):  # dostęp do macierzy definiuje jako macierz[y][x]
    n = len(macierz_W)

    for x in range(n):  # zaczynam iść od lewej strony macierzy głównej
        for y in range(x, n):  # szukam pierwszego niezerowego elementu w x-owej kolumnie
            if (macierz_A[y][x] == 0):
                pass
            else:   # jak znajdę niezerowy element, to od wszystkich wierszy usuwam wielokrotność wiersza
                for iterator in range(n):
                    if iterator==y:
                        pass
                    else:
                        wspolczynnik = float(macierz_A[iterator][x] / macierz_A[y][x])
                        macierz_A[iterator] = macierz_A[iterator] - wspolczynnik * macierz_A[y]
                        macierz_W[iterator] = macierz_W[iterator] - wspolczynnik * macierz_W[y]
                break
    return macierz_W


print("linalg.solve: ", np.linalg.solve(A, B))
print("moje: ", rozwiaz_metoda_Gaussa_Jordana(A, B))
