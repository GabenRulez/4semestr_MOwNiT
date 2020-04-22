# Faktoryzacja LU

# Napisz i sprawdź funkcję dokonującą faktoryzacji A = LU macierzy A.
# Zastosuj częściowe poszukiwanie elementu wiodącego oraz skalowanie.


import numpy as np
from textFunctions.textFunctions import *
import scipy.linalg


def tworz_macierz_kwadratowa(n, zakres_start=0, zakres_end=10):
    macierz = (zakres_end - zakres_start) * np.random.random_sample((n, n)) + zakres_start
    return macierz

def tworz_macierz_kwadratowa_z_zerami(n):
    macierz = np.zeros((n, n))
    return macierz

def dodaj_diagonale(macierz, wartosc):
    n = len(macierz)
    for i in range(n):
        macierz[i][i] = wartosc
    return

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




printTitle("Początek programu")

size = 2

macierz_A = tworz_macierz_kwadratowa(size)

macierz_P = przygotuj_macierz_P(macierz_A)

macierz_L = tworz_macierz_kwadratowa_z_zerami(size)
dodaj_diagonale(macierz_L, 1)

printTitle("macierz L na strrt")
print(macierz_L)

macierz_U = tworz_macierz_kwadratowa_z_zerami(size)

##################################################

P, L, U = scipy.linalg.lu(macierz_A.copy())    # obliczone z bibliotecznych funkcji

#L2, U2, P2 = faktoryzacja_LU(macierz_P, macierz_A, macierz_L, macierz_U)    # obliczone z funkcji zaimplementowanej przeze mnie
L2, U2, P2 = faktoryzacja_LU(macierz_P,macierz_A,macierz_L,macierz_U)

###################################################

printTitle("Porównanie wyników")
print("scipy.linalg.lu")
print("L:")
print(L)
print("U:")
print(U)
#print("P:")
#print(P)

printSpacer(2)

print("moja implementacja")
print("L:")
print(L2)
print("U:")
print(U2)
#print("P:")
#print(P2)

printTitle("Koniec wyników")
printTitle("Koniec programu", 0)






#import scipy as sp

# np.linalg.solve()

# np.linalg.lstsq()

# sp.linalg.lu()





####### Sekcja porażek



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

