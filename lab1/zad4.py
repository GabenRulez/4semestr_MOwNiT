# Błędy zaokrągleń i odwzorowanie logistyczne

# Rozważ odwzorowanie logistyczne dane następującym wzorem rekurencyjnym
#       x_(n+1) = r * x_n * (1−xn)

# Przy czym 0 <= x_n <= 1 i r > 0.
# Zbadaj zbieżność procesu iteracyjnego określonego tym równaniem w zależności od wartości parametru r oraz x_0.

# a)    Dla różnych wartości r (1 <= r <= 4) oraz kilku wybranych wartości x_0 przedstaw na wykresie
#       wartości x_n uzyskane po wielu iteracjach odwzorowania logistycznego (diagram bifurkacyjny).
#       Dokonaj interpretacji otrzymanych wyników.

# b)    Dla tych samych wartości x_0 oraz r (3.75 <= r <= 3.8) porównaj trajektorie obliczone z użyciem pojedynczej
#       i podwójnej precyzji. Wyjaśnij otrzymane wyniki.

# c)    Dla r = 4 i różnych wartości x_0 wyznacz (pojedyncza precyzja) liczbę iteracji potrzebnych do osiągnięcia zera.
#       Przedstaw interpretację rezultatów.



def eta(s, n, singlePrecision=True):
    if singlePrecision:
        wynik = np.float32(0.0)
        for k in range(1, n + 1):  # dla k=1,2, ... , n
            wynik = np.float32(wynik + (-1) ** (k - 1) * (1 / (k ** s)))

    else:
        wynik = np.float64(0.0)
        for k in range(1, n + 1):  # dla k=1,2, ... , n
            wynik = np.float64(wynik + (-1) ** (k - 1) * (1 / (k ** s)))
    return wynik