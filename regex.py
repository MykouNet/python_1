#!/usr/bin/env python3
# utilisation REGEX
# recherche d'une chaine de caractères ressemblant à .xxxxCI

import sys, re
print(sys.argv[1])
nb_arg = str(sys.argv[1])
x = re.search(r"^.*CI$", nb_arg)
if (x):
  print("YES! We have a match!")
else:
  print("No match")