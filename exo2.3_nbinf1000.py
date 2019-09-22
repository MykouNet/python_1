#!/usr/bin/env python3

liste = [50,1205,25,23,896,6222,7895,562]
liste_sup1000 = list(liste)

# identification nb inférieur à 1000

for nb in liste:
    if ( nb < 1000 ):
        print("nb lu < 1000", nb)
        liste_sup1000.remove(nb)

print(liste_sup1000)