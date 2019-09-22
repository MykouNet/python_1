#!/usr/bin/env python3
# ./exo_trouver_le_A.py  chaine de caractères comportant ou pas un 'a'
import re
import sys


def presenceA (list_E):
    list = list_E
    cpteurA = list.count('a')
    if cpteurA != 0:
        print ("a")
    else:
        print("")
    return


def main():
    if (len (sys.argv) != 2 ):
        print("invalid number of arguments.")
        return (-1)
    else:
        liste_retour = str(sys.argv[1])
        presenceA(liste_retour)
    return ()

if __name__ == '__main__':
    main()