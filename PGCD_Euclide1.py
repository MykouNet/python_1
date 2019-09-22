#!/usr/bin/env python3
# ./PGCD_Euclide1.py, calcul via une fonction et de façon récursive

def euclide (m,n):
    r = m % n
    if ( r == 0 ):
        return print(n)
    m = n
    n = r
    euclide(m,n)

euclide(119, 544)