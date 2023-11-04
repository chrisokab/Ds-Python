import getpass
from password_handler import *
from my_function import *


def enregistrement():
    email = ""
    password = ""
    while not validation_email(email) or unique_mail(email):
        email = str(input("Email : "))

    while not validation_password(password):
        password = str(getpass.getpass("Mot de passe : "))
        if not validation_password(password):
            print("Entrez un mot de passe fort, \n 8 caracteres minimum, \n une lettre majuscule, \n une lettre minuscule, \n un chiffre et \n un caractere speciale.")
    password = hasher_mot(password)

    with open("enregistrement.txt", "a") as file:
        file.write(f"Email: {email}\n")
        file.write(f"Mot de passe: {password}\n")


def connexion():
    email = ""
    password = ""

    while (email == ""):
        email = str(input("Email : "))
    while (password == ""):
        password = str(getpass.getpass("Mot de passe : "))
    mot_de_passe_hash_utilisateur = hasher_mot(password)

    with open("enregistrement.txt", "r") as file:
        lignes = file.readlines()
        for i in range(0, len(lignes), 2):
            mails_dans_la_base = lignes[i].strip().split(" ")[1]
            mot_de_passe_enregistre_hash = lignes[i + 1].strip().split(" ")[3]
            if (email.lower() == mails_dans_la_base):
                if (mot_de_passe_hash_utilisateur == mot_de_passe_enregistre_hash):
                    print("Connexion reussie")
                    return True
                else:
                    print("Email / Mot de Passe Incorrecte")
                    return False
            else:
                print("Email / Mot de Passe Incorrecte")
                return False
