#!/usr/bin/env python3

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

mot_a_crypter=str(input("entrer le message à coder : "))
index_max=(len(mot_a_crypter)-1)
mot_crypte = list(mot_a_crypter)
mot_crypte.clear()

# choisir le nb de décaage
decalage=int(input("entrer un nombre correspondant au décalage : "))

# crypter le mot
for i in range (0,len(mot_a_crypter)):
#    print(alphabet.index(mot_a_crypter[i]))
    j=alphabet.index(mot_a_crypter[i])
#    print(alphabet[j+decalage])
    mot_crypte.append(alphabet[j+decalage])
#    print(mot_crypte)

print("".join(mot_crypte))
