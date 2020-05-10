# Odwrotna metoda potęgowa

# Opierając się na twierdzeniu o transformacji widma macierzy:

#   Twierdzenie 1 Macierz (A−σI)−1 (jeśli istnieje),
#   to ma wartości własne równe 1 λk −σ( λk jest k-tą wartością macierzy A)
#   i wektory własne identyczne z macierzą A.

# oraz wykorzystując metodę potęgową i faktoryzację LU zaimplementuj odwrotną metodę potęgową
# pozwalającą na szybkie znalezienie wektorów własnych macierzy A, dla wartości σ bliskich odpowiedniej wartości własnej.

# Wykorzystaj fakt, że mnożenie wektora xi przez macierz A−1 (xi+1 = A−1xi) odpowiada rozwiązaniu układu równań Axi+1 = xi.

import numpy as np
import scipy.linalg


# Moja funkcja z lab6/zad2.py
def rozklad_LUP(a):  # korzystam z algorytmu z Kincaida, str. 167
    n = len(a)

    u = np.copy(a)
    u = u.astype(float)
    p = tworz_macierz_kwadratowa_z_zerami(n)
    dodaj_diagonale(p, 1)
    l = tworz_macierz_kwadratowa_z_zerami(n)


    for i in range(n):  # skalowanie
        p[i] = p[i] / np.max(u[i])
        u[i] = u[i] / np.max(u[i])

    for i in range(n):

        # częściowe poszukiwanie elementu wiodącego
        max = u[i][i]
        indeks = i

        for j in range(i, n):
            if u[j][i] > max:
                max = u[j][i]
                indeks = j

        if indeks != i:
            u[[indeks, i]] = u[[i, indeks]]
            p[[indeks, i]] = p[[i, indeks]]
            l[[indeks, i]] = l[[i, indeks]]


        for k in range(i + 1, n):
            czynnik = u[k][i] / u[i][i]
            u[k] = u[k] - u[i] * czynnik
            u[k][i] = 0
            l[k][i] = czynnik

    dodaj_diagonale(l, 1)
    return p, l, u

def tworz_macierz_kwadratowa(n, zakres_start=0, zakres_end=10, asint=False):
    macierz = (zakres_end - zakres_start) * np.random.random_sample((n, n)) + zakres_start
    if asint:
        macierz = macierz.astype(int)
    else:
        macierz = macierz.astype(float)
    return macierz

def tworz_macierz_kwadratowa_z_zerami(n):
    macierz = np.zeros((n, n))
    macierz = macierz.astype(float)
    return macierz

def dodaj_diagonale(macierz, wartosc):
    n = len(macierz)
    for i in range(n):
        macierz[i][i] = wartosc
    return
# Koniec funkcji z lab6/zad2.py



















def odwrotnaMetodaPotegowa(matrix_A, iterations=1000, epsilon=0.000001, sigma=0):
    n = len(matrix_A)
    vector_X = np.zeros(n)
    vector_X[0] = 1

    p, l, u = rozklad_LUP(matrix_A)
    LU = np.dot(l,u)
    print(LU)

    for i in range(iterations):
        new_vector_X = scipy.linalg.lu_solve(LU, vector_X)
        new_vector_X /= np.linalg.norm(new_vector_X)

        if(np.linalg.norm(new_vector_X - vector_X) < epsilon):
            break;
        vector_X = new_vector_X
    return vector_X


A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])


odwrotnaMetodaPotegowa(A)




