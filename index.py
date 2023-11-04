from cesar import chiffrement_cesar_ascii, chiffrement_cesar_lettres, dechiffrement_cesar_lettres
from my_function import *
from password_handler import *
import getpass
from dictionnary import *
from enregistrement import *
import os

print("BIENVENUE SUR MON PROGRAMME")
print("_______________")


value = 0
while (value != 1 and value != 2):
    print("1. Enregistrement")
    print("2. Authentification")
    value = int(input("Quel est votre choix ? : "), 10)
    print(value)

if value == 1:
    enregistrement()

if value == 2:
    isConnected = connexion()
    choix = ""
    estChiffre = False
    decalage = 0
    mot_chiffre = ""
    if isConnected:
        while True:
            print("A. Donnnez un mot à hacher")
            print("B. Décalagage de César")
            print("C. Collection du Dataset")

            choix = input("Votre choix : ").upper()
            if (choix.upper() == "A"):
                while True:
                    isHashed = False
                    mot = str(getpass.getpass(
                        "Donnez le mot à hacher (d pour revenir en arrière) : "))
                    # print("a - Hacher le mot", mot)
                    print("b - Attaquer par dictionnaire le mot ", mot)
                    print("d - Revenir au menu principal")
                    if (mot == "d"):
                        os.system('cls')
                        break

                    choix_a = input("Votre choix : ").lower()

                    if (choix_a == "b"):
                        mot = hasher_mot(mot)
                        attack(mot)

                    elif (choix_a == "d"):
                        os.system('cls')
                        break

                    # print(hasher_mot(mot))
                    # Attaque du mot par dictionnaire
            elif (choix.upper() == "B"):
                print("DECALAGE DE CESAR MON POTE")
                os.system('cls')
                while True:
                    print("a- Pour chiffrer le message")
                    print("b- Pour déchiffrer le message")
                    print("c- Pour revenir au menu principal")
                    choix_methode = input("Votre choix : ")
                    os.system("cls")
                    mot = ""

                    if (choix_methode.lower() == "a"):
                        estChiffre = False
                        mot = str(input("Donnez un mot à chiffrer : "))
                        decalage = int(input("Donnez un decalage : "))
                        while True:
                            print("1 Pour Cesar avec Code ASCII")
                            print("2 Pour Cesar dans les 26 Lettres")
                            print("autre chiffre pour quitter")
                            choix_cesar = int(input("Votre choix : "))
                            if (choix_cesar == 1):
                                print("Cesar avec Code ASCII")
                                mot_chiffre = chiffrement_cesar_ascii(
                                    mot, decalage)
                                print(mot_chiffre)
                                estChiffre = True
                            elif (choix_cesar == 2):
                                print("Cesar dans les 26 Lettres")
                                mot_chiffre = chiffrement_cesar_lettres(
                                    mot, decalage)
                                print(mot_chiffre)

                            else:
                                break
                    elif (choix_methode.lower() == "b"):

                        if (estChiffre):
                            print("VOULEZ-VOUS DECHIFFRER LE MOT ",
                                  mot_chiffre, " ? ")
                            print("1 - OUI")
                            print("2 - NON, choisir un autre mot")
                            choix_cesar = int(input("Votre choix : "))
                            try:
                                if (choix_cesar == 1):
                                    print(dechiffrement_cesar_lettres(
                                        mot_chiffre, decalage
                                    ))
                                    estChiffre=False
                                elif (choix_cesar == 2):
                                    mot = str(
                                        input("Donnez un mot à déchiffrer svpl: "))
                                    decalage = int(
                                        input("Donnez un decalage pour le déchiffrement: "))
                                    print(dechiffrement_cesar_lettres(mot, decalage))
                                    mot_chiffre=""
                                    decalage=0
                                    estChiffre=False
                                else:
                                    print("CHOIX INCORRECT")
                            except:
                                print("CHOIX INCORRECT")

                        elif (estChiffre == False):
                            mot = str(input("Donnez un mot à déchiffrer : "))
                            decalage = int(
                                input("Donnez un decalage pour le déchiffrement: "))
                            print(dechiffrement_cesar_lettres(mot, decalage))
            elif(choix.upper() == "C"):
                show_dataset()
            else:
                print("CHOIX INCORRECT")
                os.system('cls')
