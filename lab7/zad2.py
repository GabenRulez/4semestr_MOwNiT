# Odwrotna metoda potęgowa

# Opierając się na twierdzeniu o transformacji widma macierzy:

#   Twierdzenie 1 Macierz (A−σI)−1 (jeśli istnieje),
#   to ma wartości własne równe 1 λk −σ( λk jest k-tą wartością macierzy A)
#   i wektory własne identyczne z macierzą A.

# oraz wykorzystując metodę potęgową i faktoryzację LU zaimplementuj odwrotną metodę potęgową
# pozwalającą na szybkie znalezienie wektorów własnych macierzy A, dla wartości σ bliskich odpowiedniej wartości własnej.

# Wykorzystaj fakt, że mnożenie wektora xi przez macierz A−1 (xi+1 = A−1xi) odpowiada rozwiązaniu układu równań Axi+1 = xi.