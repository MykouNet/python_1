#!/usr/bin/env python3
import random

print ("on va jouer à pierre feuille ciseaux")

def affichage_choix(joueur, choix):
    choix=str(choix)
    if joueur == 'application':
        joueur = "l'application a joué : "
    else: joueur = "le joueur a joué : "

    if choix == '1' :
        print (joueur, '1-pierre')
    elif choix == '2' :
        print(joueur, '2-feuille')
    elif choix == '3' :
        print(joueur, '3-ciseaux')

def     choix_joueur():
    cj = input ("entrer 1 pour pierre, 2 pour feuille, 3 pour ciseaux  ")
    affichage_choix("joueur", cj)

    if cj.isnumeric() == True:
        cj = int(cj)

    if (( cj == 1 ) or ( cj == 2 ) or ( cj == 3 )):
        pass
    else:
        bien_joue = False

        while not bien_joue:
            print("choix : ", cj, " non valable !! Rejouez")
            cj = input("entrer 1 2 3 ")
            affichage_choix("joueur", cj)
            if cj.isnumeric() == True:
                cj = int(cj)

            if (( cj == 1 ) or ( cj == 2 ) or ( cj == 3 )):
                bien_joue=True
                affichage_choix("joueur", cj)
    return cj;

def     choix_python():
    liste =[1,2,3]
    cp = int(random.choice(liste))
    appli = "application"
    affichage_choix(appli, cp)
    return cp;

def     choix_plus_fort(joueur, python):

    if ( joueur == python ):
        print ("pareil, rejouez")
        choix_plus_fort(choix_joueur(), choix_python())
    elif (( joueur == 1 ) and (python == 3 )):
        print("Vous avez gagné : 1-Pierre plus fort que 3-Ciseaux")
    elif (( joueur == 2 ) and (python == 1 )):
        print ("Vous avez gagné : 2-Feuille plus fort que 1-Pierre")
    elif (( joueur == 3 ) and (python == 2 )):
        print("Vous avez gagné : 3-Ciseaux plus fort que 2-Feuille")
    else:
        print ("Vous avez perdu !")
    return



choix_plus_fort(choix_joueur(), choix_python())