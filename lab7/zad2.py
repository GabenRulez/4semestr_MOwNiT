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

from textFunctions import printLineSpacer, printTitle, printSpacer


def odwrotnaMetodaPotegowa(matrix_A, iterations=1000, epsilon=0.000001, sigma=0):
    n = len(matrix_A)
    vector_X = np.zeros(n)
    vector_X[0] = 1

    LU = scipy.linalg.lu_factor(matrix_A - sigma*np.identity(n))

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

printTitle("np.linalg.eig")
w,v = np.linalg.eig(A)
print(w)
printSpacer(1)
print(v)

printTitle("odwrotnaMetodaPotegowa", 1)
print("Dla sigma = w[0]")
print(odwrotnaMetodaPotegowa(A, sigma=w[0]))
print("Dla sigma = w[1]")
print(odwrotnaMetodaPotegowa(A, sigma=w[1]))
print("Dla sigma = w[2]")
print(odwrotnaMetodaPotegowa(A, sigma=w[2]))


# Jak wyraźnie widać, wyniki te pokrywają się z bibliotecznymi (kolumny / wiersze)



