print("Convertisseur de valeur")
print("A- Pouces vers Cm")
print("B- Cm vers Pouces ")



def convertir(valeur, facteur_conversion):
    return round(valeur * facteur_conversion, 2)


def demander_valeur():
    while True:
        valeur = input("Entrer la valeur a convertir (ou Q pour quitter)").strip().lower()
        if valeur=="q":
            print("Merci d'avoir utilisé le convertisseur. À bientôt !")
            exit()
        try:
            return float(valeur)
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide ou Q pour quitter.")

            # pourquoi on ne fint pas avec un breack ??

def convertisseur_de_valeurs():
    while True:
        choix = input("\nChoisissez une option (A ou B, ou Q pour quitter) : ").strip().lower()
        if choix=="a":
            print("\nConversion : Pouces → Cm")
            valeur = demander_valeur()
            resultat = convertir(valeur, 2.54)
            print(f"{valeur} pouces est égal à {resultat} cm.")
        elif choix =="b":
            print("\nConversion : Cm → Pouces")
            valeur = demander_valeur()
            resultat = convertir(valeur, 0.394)
            print(f"{valeur} cm est égal à {resultat} pouces.")

        elif choix =="q":
            print("Merci d'avoir utilisé le convertisseur. À bientôt !")
        break  # sortie du while

    else:
        print("Veuillez choisir une option valide : A, B, ou Q.")


convertisseur_de_valeurs()






