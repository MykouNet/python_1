#!/usr/bin/env python3
import sys

"""
https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-9.php
"""


class IOString():
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("saisir un message : ")

    def printString(self):
        print(self.string.upper())

def main():
    stringToPrint = IOString()
    stringToPrint.getString()
    stringToPrint.printString()

    return

if __name__ == '__main__':
    main()
