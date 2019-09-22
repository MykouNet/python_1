#!/usr/bin/env python3
import sys
"""
https://www.w3resource.com/python-exercises/class-exercises/index.php#EDITOR
"""

class rectangle():
    def __init__(self):
        self.longueur = 0
        self.largeur = 0
        self.surface = 0

    def recupInfo(self):
        self.longueur = input("saisir longueur : ")
        self.largeur = input("saisir largeur : ")

    def calcSurface(self):
        self.surface = int(self.largeur) * int(self.longueur)
        print (" la surface est {}".format(self.surface))

def main():
    objetW = rectangle()
    objetW.recupInfo()
    objetW.calcSurface()
    return

if __name__ == '__main__':
    main()