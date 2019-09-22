#!/usr/bin/env python3
stri=str(input("entrer une chaine de caractère : "))
lon_stri=len(stri)
liste=list(stri)
liste.reverse()
print("".join(liste))