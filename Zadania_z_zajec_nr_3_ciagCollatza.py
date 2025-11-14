# Ciąg Collatza zdefiniowany jest następująco:
# Rozpoczynamy od podanej ze standardowego wejścia liczby x (od 1 do 100).
# Jeśli x jest liczbą parzystą, to kolejny wyraz ciągu będzie obliczony jako x/2.
# W przeciwnym przypadku kolejny wyraz ciągu będzie równy 3x+1.
# W ten sam sposób obliczamy kolejne wyrazy ciągu, aż pojawi się liczba 1.

# Napisz program, który wypisze długość ciągu Collatza dla podanego ze standardowego wejścia x.
# X może przyjmować wartości od 1 do 100.

x = int(input("Podaj liczbę od 1 do 100: "))


if x < 1 or x > 101:
    print("Liczba musi być w zakresie od 1 do 100.")
    exit()

print("Ciąg Collatza zaczynający się od", x, ":")
    
while x != 1:
    print(x, end=' ')
    if x % 2 == 0:
        x = x // 2
    else:
        x = 3 * x + 1
        
print(1)  # Wypisujemy ostatni wyraz ciągu, czyli 1