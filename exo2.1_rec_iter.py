#!/usr/bin/env python3
#./exo2.1_rec_iter.py

def     fct_recursive(n):
    if n == 0:
        return 1
    return ((n * fct_recursive(n - 1)))

def     fct_iterative(n):
    i = 1
    fact = 1
    for i in range (1,n):
        i = i + 1
        fact = fact * i
    return fact

print("calcul de la factorielle de n")
x=int(input("indiquer un nombre n dont le progragramme va calculer la factorielle  "))
y=input("indiquer si le calcul doit se faire de façon itérative 'i' ou récursive (tout autre choix)  ")

if y == "i":
    print(fct_iterative(x))
else:
    print(fct_recursive(x))



#choix_fonction = {  'i' : fct_iterative(x),
#                    'f' : fct_recursive(x)
#                    }
#rint(int(choix_fonction[y](x)))
