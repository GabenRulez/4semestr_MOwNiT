# Metoda potęgowa

# Napisz funkcję obliczającą metodą potęgową dominującą wartość własną (największą co do modułu)
# i odpowiadający jej wektor własny dla danej macierzy rzeczywistej symetrycznej.
# Sprawdź poprawność działania programu porównując własną implementację z wynikami funkcji bibliotecznej.
# Przedstaw na wykresie zależność czasu obliczeń od rozmiaru macierzy (rozmiary macierzy 100x100, 500x500, ...).

# • Powtarzaj mnożenie wektora xi przez macierz A: xi+1 = Axi, dzieląc za każdym razem wektor wynikowy przez ||xi+1||
# • Element wektora xi o największej wartości bezwzględnej zbiega do dominującej wartości własnej
# • Przeskalowany wektor xi zbiega do dominującego wektora własnego
# • Obliczenia powinny się zatrzymać po przekroczeniu maksymalnej liczby iteracji, albo w przypadku gdy ||xi −xi+1|| < e (kryterium małej poprawki)
# • Pod koniec obliczeń znormalizuj otrzymany wektor własny.

import numpy as np
import math



def metodaPotegowa(matrix_A, iterations=10000, epsilon=0.00000001):
    n = len(matrix_A)
    vector_X = np.zeros((n,1))
    for i in range(n):  # ustaw wartość wektora X
        vector_X[i][0] = float(np.random.randint(0,100))/100

    for i in range(iterations): # limit iteracji

        new_vector_X = np.zeros((n,1))
        for i in range(n):      # twórz nowy wektor i wypełnij go zgodnie z mnożeniem macierzy
            for j in range(n):
                new_vector_X[i][0] += matrix_A[i][j] * vector_X[j][0]



        temp = 0                # obliczanie normy i podzielenie przez nią wektora
        for i in range(n):
            temp += new_vector_X[i][0] ** new_vector_X[i][0]
        forma_z_X = math.sqrt(temp)
        for i in range(n):
            new_vector_X[i][0] = new_vector_X[i][0] / forma_z_X;



        temp_Vector = vector_X  # sprawdzenie "kryterium małej poprawki"
        for i in range(n):
            temp_Vector[i][0] -= new_vector_X[i][0]
        temp = 0
        for i in range(n):
            temp += temp_Vector[i][0] * temp_Vector[i][0]
        forma_z_temp_Vector = math.sqrt(temp)
        if forma_z_temp_Vector < epsilon:
            break;



        for i in range(n):      # zamiana starego wektora na nowy
            vector_X[i][0] = new_vector_X[i][0]

    dominujaca_wartosc_wlasna = 0
    for i in range(n):
        if abs(vector_X[i][0]) > dominujaca_wartosc_wlasna:
            dominujaca_wartosc_wlasna = vector_X[i][0]


    return dominujaca_wartosc_wlasna, vector_X/np.linalg.norm(vector_X)



A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])


dom_war_wla, wektor = metodaPotegowa(A)
print(dom_war_wla)
print(wektor)


w,v = np.linalg.eig(A)  # niestety nie wiem, skąd z tych funckji wyliczyć "wartość własną", jedyne co ona zwraca to dwie macierze
print(w)
print(v)