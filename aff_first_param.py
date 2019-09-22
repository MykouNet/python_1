#!/usr/bin/env python3
# ./aff_first_param.py AFFICHE_CET_ARGUMENT 2 fois via le print


import sys
print (sys.argv[1])

def main():
    if len(sys.argv) == 1:
        return -1
    else:
        print(sys.argv[1])

if __name__ == '__main__':
   main()