#!/usr/bin/env python3
# on écrit la commande cat, prend en argument un nom de fichier et l'imprime sur la sortie standard
# ./ouvrirFichier.py  FileEAAfficher

import sys

def fctQuiVaFaireCat(filename):
    file_object = open(filename, mode="r")
    for line in file_object:
        print(line, end='')
    return

def main():
    if (len (sys.argv) != 2 ):
        print("invalid number of arguments.")
        return (-1)
    else:
        fctQuiVaFaireCat(sys.argv[1])
    return ()

if __name__ == '__main__':
    main()
