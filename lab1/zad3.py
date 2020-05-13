# Sumy częściowe

# Rozważ sumy częściowe szeregu deﬁniującego funkcję dzeta Riemanna:
#       dzeta(s) = // suma od k=1 do k=n z ( 1 / ( k^s)  )  //

# oraz funkcję eta Dirichleta:
#       eta(s) = // suma od k=1 do k=n z ( (-1)^(k-1) * ( 1 / ( k^s ) ) ) //

# Dla:
#   s = 2,3.6667,5,7.2,10       oraz        n = 50,100,200,500,1000
#   oblicz wartości funkcji dzeta(s) i eta(s) w pojedynczej precyzji sumując w przód, a następnie wstecz.
#   Porównaj wyniki z rezultatami uzyskanymi dla podwójnej precyzji. Dokonaj interpretacji otrzymanych wyników.

# Wskazówka
# Porównaj oszacowania względnych błędów dla działań
#   fl(fl(x + y)+ z)
#   oraz
#   fl(x + fl(y + z))
#   przy założeniu, że |x + y| < |y + z|.