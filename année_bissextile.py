#!/usr/bin/env python3
# python3 année_bissextile.py

def is_leap(year):
    if (( year %400 == 0 ) or (( year %4 == 0 ) and ( year %100 != 0 ))):
        print ("bissextile")
    else:
        print ("année non bissextile")
    return

year=int(input("entrer une année  : "))
is_leap(year)
