#!/usr/bin/env python3

liste=[45,45,23,97,56,46,2,94,16,6,3,17,35,35]
listeW=liste
liste_impaire=list(liste)

# identification nb pair/impair

for nb in liste:
    if (( nb % 2 ) == 0 ):
        liste_impaire.remove(nb)

print(liste_impaire)