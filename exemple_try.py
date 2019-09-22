#!/usr/bin/env python3

"""
Gérer les exceptions : try/except (+else, finally)
"""

try :
    ageUtilisateur = int(input("quel âge as-tu ? "))
    assert  ageUtilisateur > 18
except AssertionError:
    print("tu es mineur(e) !")
else:
    print("tu as ", ageUtilisateur, " ans")
finally:
    exit()