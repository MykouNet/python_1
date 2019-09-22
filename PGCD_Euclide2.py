#!/usr/bin/env python3
#./PGCD_Euclide2.py 119 544, les arguments sont passés en ligne de commande

import sys

def main():
    if (len (sys.argv) != 3 ):
        print("invalid number of arguments.")
        return (-1)
    else:
        (dividende, diviseur) = (int(sys.argv[1]), int(sys.argv[2]))
        modulo = dividende % diviseur
        while modulo != 0:
            dividende = diviseur
            diviseur = modulo
            modulo = dividende % diviseur
        else:
            print("PGCD :", diviseur)
    return

if __name__ == '__main__':
    main()
