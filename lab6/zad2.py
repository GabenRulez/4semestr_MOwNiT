# Faktoryzacja LU

# Napisz i sprawdź funkcję dokonującą faktoryzacji A = LU macierzy A.
# Zastosuj częściowe poszukiwanie elementu wiodącego oraz skalowanie.


import numpy as np
from textFunctions.textFunctions import *

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

###################################################

printTitle("Początek programu")
size = 3

a = tworz_macierz_kwadratowa(size)

p, l, u = rozklad_LUP(a)

###################################################

printTitle("Porównanie wyników")
print("moja implementacja")
print("P:")
print(p)
print("A:")
print(a)
print("L:")
print(l)
print("U:")
print(u)
printSpacer(2)
print("P * A:")
print(np.dot(p, a))
print("L * U")
print(np.dot(l, u))
printSpacer(1)
print("Różnica między tymi wynikami:")
print(np.dot(p, a) - np.dot(l, u))
printTitle("Koniec programu", 0)

# Jak widać, różnica między tymi wynikami jest znikoma, a tak naprawdę wynika zapewne z niedokładności liczb (float).

###################################################






####### Sekcja porażek ##################### (proszę nie oglądać niczego co jest poniżej)

def faktoryzuj_na_LUP(macierz_P, macierz_A):  # nie działa, podaje błędne wyniki
# macierze w tej formie nie są kopiowane, więc funkcja może je zmodyfikować
# Korzystam tutaj z rozkładu LUP, który bazuje na częściowym poszukiwaniu elementu wiodącego.
# psuje A

    N = len(macierz_A)

    for i in range(0, N-1):

        maxPivot = i    # ustawiamy największy element z kolumny, aby był na przekątnej
        for k in range(i+1, N):
            if abs(macierz_A[k][i]) > abs(macierz_A[i][i]):
                maxPivot = k

        if maxPivot != i:   # zamiana wierszy
            macierz_P[i], macierz_P[maxPivot] = macierz_P[maxPivot], macierz_P[i]
            macierz_A[i], macierz_A[maxPivot] = macierz_A[maxPivot], macierz_A[i]

        for k in range(i+1, N):
            macierz_A[k][i] = macierz_A[k][i] / macierz_A[i][i]

            for j in range(i+1,N):
                macierz_A[k][j] = macierz_A[k][j] - macierz_A[i][j] * macierz_A[k][i]

def moja_faktoryzacja_LUP(macierz):

    matrix_A = np.copy(macierz)
    n = len(matrix_A)
    matrix_P = tworz_macierz_kwadratowa_z_zerami(n)
    dodaj_diagonale(matrix_P, 1)

    matrix_L = tworz_macierz_kwadratowa_z_zerami(n)
    dodaj_diagonale(matrix_L,1)

    matrix_U = np.copy(matrix_A)
    matrix_U = matrix_U.astype(float)

    # skalowanie do wyboru elementów głównych
    for i in range(n):
        tempValue = np.max(matrix_U[i])
        matrix_P[i] /= tempValue
        matrix_U[i] /= tempValue

    for i in range(n):

        max = matrix_U[i][i]
        indeks = i

        for j in range(i, n):
            if matrix_U[j][i] > max:
                max = matrix_U[j][i]
                indeks = j

        #if indeks != i:
        matrix_U[[indeks, i]] = matrix_U[[i, indeks]]
        matrix_P[[indeks, i]] = matrix_P[[i, indeks]]
        matrix_L[[indeks, i]] = matrix_L[[i, indeks]]

        for k in range(i + 1, n):
            factor = matrix_U[k, i] / matrix_U[i, i]
            matrix_U[k] = matrix_U[k] - matrix_U[i] * factor
            matrix_U[k, i] = 0
            matrix_U[k, i] = factor
    np.fill_diagonal(matrix_L, 1)
    return matrix_L, matrix_U, matrix_P

def przygotuj_macierz_P(macierz_A):
    temp_size = len(macierz_A)

    temp_macierz_P = tworz_macierz_kwadratowa_z_zerami(temp_size)
    dodaj_diagonale(temp_macierz_P, 1)

    for j in range(temp_size):
        row = j
        for i in range(j, temp_size):
            if abs(macierz_A[i][j]) > abs(row):
                row = i

        if j != row:
            temp_macierz_P[j], temp_macierz_P[row] = temp_macierz_P[row], temp_macierz_P[j]

    return temp_macierz_P

def faktoryzacja_LU(macierz_P, macierz_A, macierz_L, macierz_U):
# Po wielu problemach z różnymi algorytmami, skończyłem na fakcie stworzenia macierzy P na samym początku.
# Do tej funkcji podaję już gotową macierz_P, która po przemnożeniu przez macierz_A pozwala się zfaktoryzować "zwykłym" LU.

    n = len(macierz_A)
    PA = np.dot(macierz_P, macierz_A)
    PA = macierz_A

    for j in range(n):

        for i in range(j+1):
            suma_1 = sum(macierz_U[k][j] * macierz_L[i][k] for k in range(i))
            macierz_U[i][j] = PA[i][j] - suma_1

        for i in range(j, n):
            suma_2 = sum(macierz_U[k][j] * macierz_L[i][k] for k in range(j))
            macierz_L[i][j] = (PA[i][j] - suma_2) / macierz_U[j][j]

    return macierz_L, macierz_U, macierz_P