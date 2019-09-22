#!/usr/bin/env python3
# ./maff_alpha.py
# passage des consonnes en majuscule, les voyelles présentes dans une liste reste en minuscule
import re
import sys


def upperLowerCase(alphabetE):
    alphabetW = list(alphabetE)
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    for ix in range (0,len(alphabetW)):
        if alphabetW [ix] not in voyelles:
            ltr_maj = str(alphabetW[ix]).upper()
            alphabetW[ix] = str(ltr_maj)
    return print(alphabetW)


def main():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upperLowerCase(alphabet)
    return ()

if __name__ == '__main__':
    main()