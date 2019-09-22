#!/usr/bin/env python3


print("ce programme calcule la suite de Fibonacci")
fibo=int(input("Entrer une valeur enti=C3=A8re pour le calcul de la suite de Fibonacci :"))

# la liste de Fibonacci
fibonacci_liste = [0,1]


# boucle it=C3=A9rative
print("F(0) = ", fibonacci_liste[0])
print("F(1) = ", fibonacci_liste[1])


for i in range (2, fibo+1):
#    print(i)
    x=(int(fibonacci_liste[i-1]) + int(fibonacci_liste[i-2]))
    fibonacci_liste.append(x)
    y=fibonacci_liste[i]
    print("F(",i,") = ", y)
