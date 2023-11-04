def chiffrement_cesar_lettres(mot, decalage):
    mot_chiffre = ""
    for lettre in mot:
        if lettre.isalpha():
            majuscule = lettre.isupper()
            lettre = lettre.lower()
            lettre_chiffree = chr((ord(lettre) - 97 + decalage) % 26 + 97)
            if majuscule:
                lettre_chiffree = lettre_chiffree.upper()
            mot_chiffre += lettre_chiffree
        else:
            mot_chiffre += lettre
    return mot_chiffre


def dechiffrement_cesar_lettres(mot,decalage):
    chiffre = chiffrement_cesar_lettres(mot, -decalage)
    return chiffre


def chiffrement_cesar_ascii(mot, decalage):
    mot_chiffre = ""
    for lettre in mot:
        if lettre.isalpha():
            code_ascii = ord(lettre)
            nouveau_code = (code_ascii - 65 + decalage) % 26 + \
                65 if lettre.isupper() else (code_ascii - 97 + decalage) % 26 + 97
            mot_chiffre += chr(nouveau_code)
        else:
            mot_chiffre += lettre
    return mot_chiffre


mot = "MJJQT"
decalage = 5
chiffre = (dechiffrement_cesar_lettres(mot,decalage))
print(chiffre)

# mot_dechiffre_lettres = chiffrement_cesar_lettres(chiffre, -decalage)
# # print(mot_dechiffre_lettres)

# print(chiffrement_cesar_ascii(mot, decalage))
