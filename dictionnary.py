from password_handler import *


def attack(mot):
    trouve = False
    i = 0
    with open("dico.txt", "r", encoding="utf-8") as file:
        try:
            mots = file.read().strip().splitlines()
        except:
            pass
        # lignes = file.readlines()
        # for i in range(0, len(lignes), 2):
        #     email = lignes[i].strip().split(" ")[1]
        #     mot_de_passe = lignes[i + 1].strip().split(" ")[2]
        #     if email == mot and mot_de_passe == "12345":
        #         print("L'email et le mot de passe ont été moinsvés dans le fichier.")
    # print(mots[875])
    for element in mots:
        # print(element)
        # print(mot)
        if hasher_mot(element) == mot:
            trouve = True

            break
        i = i+1
    if trouve:
        print("Le mot " + element +
              " se trouve dans le dictionnaire et se trouve dans la position ", i+1)
    else:
        print("Le mot ne se retrouve pas")
