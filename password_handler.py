import hashlib
import os
import re
# Pour protéger le mot de passe haché contre une attaque
# par dictionnaire, nous avons utiliser une technique de salage.
# Le salage consiste à ajouter une chaîne aléatoire (sel)
# au mot de passe avant de le hacher.


def generer_sel():
    return os.urandom(16).hex()


def hasher_mot(mot):
    h=hashlib.new("SHA256")
    h.update(mot.encode())
    sha256 = h.hexdigest()
    return sha256


def validation_password(password):
    # Ici code
    flag = 0
    
    while True:
        if (len(password) <= 8):
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$!%*?&#^+,.-]", password):
            flag = -1
            break
        elif re.search("\s", password):
            flag = -1
            break
        else:
            flag = 0
            return True


# print(f"Le sel utilisé est : {sel}")
