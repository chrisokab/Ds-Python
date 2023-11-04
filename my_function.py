import re
import pandas as pd
import matplotlib.pyplot as plt

regex = re.compile(
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def validation_email(email):
    email = email.lower()

    if re.fullmatch(regex, email):
        return True
    else:
        if (email != ""):
            print("Le Mail que vous avez entré est invalide")
        return False


def unique_mail(email):
    with open("enregistrement.txt", "r") as file:
        lignes = file.readlines()
        for i in range(0, len(lignes), 2):
            mails_dans_la_base = lignes[i].strip().split(" ")[1]
            if (email.lower() == mails_dans_la_base):
                print("Cette adresse est déjà utilisée")
                return True


def verification_donnees(email_recherche, mot_de_passe_recherche):
    trouve = False
    with open("enregistrement.txt", "r") as file:
        lignes = file.readlines()
        for i in range(0, len(lignes), 2):
            email = lignes[i].strip().split(" ")[1]
            print(email)
            mot_de_passe = lignes[i + 1].strip().split(" ")[2]
            if email == email_recherche and mot_de_passe == mot_de_passe_recherche:
                trouve = True
                break

    if trouve:
        print("L'email et le mot de passe ont été trouvés dans le fichier.")
    else:
        print("L'email ou le mot de passe n'ont pas été trouvés dans le fichier.")

def show_dataset():
    
    data = {
        'Mois': ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'],
        'Temperature': [5, 6, 10, 15, 20, 25, 28, 27, 23, 18, 12, 7]
    }

    df = pd.DataFrame(data)

    dataset_dict = df.to_dict(orient='list')
    print("Dataset sous forme de dictionnaire:")
    print(dataset_dict)

    # Affichez un graphique des températures mensuelles
    plt.figure(figsize=(10, 6))
    plt.plot(df['Mois'], df['Temperature'], marker='o', color='b', label='Température')
    plt.xlabel('Mois')
    plt.ylabel('Température (°C)')
    plt.title('Variation mensuelle des températures')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()