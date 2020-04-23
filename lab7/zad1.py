# Metoda potęgowa

# Napisz funkcję obliczającą metodą potęgową dominującą wartość własną (największą co do modułu)
# i odpowiadający jej wektor własny dla danej macierzy rzeczywistej symetrycznej.
# Sprawdź poprawność działania programu porównując własną implementację z wynikami funkcji bibliotecznej.
# Przedstaw na wykresie zależność czasu obliczeń od rozmiaru macierzy (rozmiary macierzy 100x100, 500x500, ...).

# • Powtarzaj mnożenie wektora xi przez macierz A: xi+1 = Axi, dzieląc za każdym razem wektor wynikowy przez ||xi+1||∞
# • Element wektora xi o największej wartości bezwzględnej zbiega do dominującej wartości własnej
# • Przeskalowany wektor xi zbiega do dominującego wektora własnego
# • Obliczenia powinny się zatrzymać po przekroczeniu maksymalnej liczby iteracji, albo w przypadku gdy ||xi −xi+1|| <  (kryterium małej poprawki)
# • Pod koniec obliczeń znormalizuj otrzymany wektor własny.

