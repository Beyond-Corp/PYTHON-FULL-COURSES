
# print("Convertisseur de valeur")
# A = "A- Pouces vers Cm"
# B = "B- Cm vers Pouces"
# print(A)
# print(B)
#
#
# def convertisseur_de_valeurs_de_cm_en_pouces_vice_versa():
#     choix = ""
#     while choix != A and choix != B:
#         choix = input(f"Souhaitez vous convertir de {A} ou de {B} ? Choose between: A and B or q for Quit the programme:  ")
#         print("")
#
#         if choix == "A" or choix == "a":
#
#             while True:  # La boucle commence et continuera indéfiniment
#                 try:
#                     A_valeur_str = (input("Enter the valor to convert: "))
#
#                     if A_valeur_str == "q" or A_valeur_str == "Q":
#                         exit("THANKS :)")
#                     A_valeur_int = int(A_valeur_str)
#                     A_valeur_float = float(A_valeur_int)
#                     convertion = round(A_valeur_float * 2.54, 2)
#                     print(f"{A_valeur_float} Pouces est {convertion} cm")
#                     break
#                 except ValueError:
#                     print("Please you should enter a number or q for Quit the programme: ")
#
#         elif choix == "B" or choix == "b":
#
#             while True:
#                 try:
#                     B_valeur_str = input("Enter the valor to convert: ")
#                     if B_valeur_str == "q" or B_valeur_str == "Q":
#                         quit("THANKS :)")
#                     B_valeur_float = float(B_valeur_str)
#                     convertion = round(B_valeur_float * 0.394, 3)
#                     print(f"{B_valeur_float} Cm est {convertion} Pouces")
#                     break
#                 except ValueError:
#                     print("Please you should enter a number or q for Quit the programme: ")
#
#         elif choix == "q":
#             quit("THANKS:)")
#
#         else:
#             print("Please you should enter a A or B")
#
#
# convertisseur_de_valeurs_de_cm_en_pouces_vice_versa()
#
#



# ========VERSION 2 ==========================================================================================================
print("Convertisseur de valeurs")
print("A - Pouces vers Cm")
print("B - Cm vers Pouces")


def convertir(valeur, facteur_conversion):
    """Convertit une valeur donnée en appliquant un facteur de conversion."""
    return round(valeur * facteur_conversion, 3)


def demander_valeur():
    """Demande à l'utilisateur d'entrer une valeur et gère les erreurs."""
    while True:
        valeur = input("Entrez la valeur à convertir (ou Q pour quitter) : ").strip().lower()
        if valeur == "q":
            print("Merci d'avoir utilisé le convertisseur. À bientôt !")
            exit()
        try:
            return float(valeur)
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide ou Q pour quitter.")


def convertisseur_de_valeurs():
    while True:
        choix = input("\nChoisissez une option (A ou B, ou Q pour quitter) : ").strip().lower()

        if choix == "a":
            print("\nConversion : Pouces → Cm")
            valeur = demander_valeur()
            resultat = convertir(valeur, 2.54)
            print(f"{valeur} pouces est égal à {resultat} cm.")

        elif choix == "b":
            print("\nConversion : Cm → Pouces")
            valeur = demander_valeur()
            resultat = convertir(valeur, 0.394)
            print(f"{valeur} cm est égal à {resultat} pouces.")

        elif choix == "q":
            print("Merci d'avoir utilisé le convertisseur. À bientôt !")
            break  # sortie du while

        else:
            print("Veuillez choisir une option valide : A, B, ou Q.")


convertisseur_de_valeurs()



"""

Pour que tu puisses apprendre à améliorer un code en te posant les bonnes questions, voici une série d’interrogations 
que tu pourrais te poser lorsque tu analyses ou écris du code. Elles t’aident à identifier les répétitions et 
à créer un code plus lisible, efficace et maintenable. 🚀

1. Sur la logique générale :
Quelles parties de mon code se répètent ?

Exemple : La logique de conversion entre A et B dans ton code était presque identique.
Puis-je regrouper des blocs similaires en une seule fonction ?

Exemple : Les calculs (* 2.54 et * 0.394) pouvaient être gérés par une fonction générique convertir().
Est-ce que mon code peut être utilisé pour d’autres cas similaires ?

Exemple : Avec une fonction comme convertir(), tu peux facilement ajouter de nouvelles conversions (exemple : miles → km)
 sans copier-coller.
 
 
 
 
 
2. Sur la gestion des entrées :
Est-ce que je traite les erreurs utilisateur de façon uniforme ?

Exemple : Le code répétait la gestion de l’entrée invalide dans les deux blocs. En centralisant 
cela dans demander_valeur(), tu simplifies le code.
Comment puis-je rendre la gestion des entrées plus intuitive ?

Exemple : En rendant l’entrée insensible à la casse (lower()) et en gérant q partout, ton programme devient plus convivial.




3. Sur la modularité :
Est-ce que chaque partie de mon code a un objectif clair et unique ?

Exemple : Une fonction comme convertir() se concentre uniquement sur la conversion mathématique, sans gérer l’affichage
 ou l’entrée utilisateur.
Puis-je découper mon code en fonctions réutilisables ?

Exemple : Les parties de ton code liées à la gestion des erreurs et des conversions sont maintenant séparées.






4. Sur la lisibilité :
Mon code est-il facile à comprendre pour une autre personne ou pour moi-même plus tard ?

Exemple : En évitant les répétitions et en nommant les fonctions de manière explicite (convertir, demander_valeur), 
ton code devient plus compréhensible.
Les noms de mes variables et fonctions décrivent-ils bien leur rôle ?

Exemple : Des noms comme convertir() ou demander_valeur() expliquent clairement ce que fait chaque partie.




5. Sur l’efficacité :
Est-ce que mon code est plus long ou plus complexe qu’il ne devrait l’être ?

Exemple : Les deux boucles while pour A et B étaient redondantes, mais elles ont été fusionnées dans une logique générique.
Puis-je réduire les calculs ou les étapes inutiles ?

Exemple : Dans ton code initial, tu convertissais une chaîne en int, puis en float. Une seule conversion en float suffit.





6. Sur la flexibilité :
Si je devais ajouter une nouvelle fonctionnalité, combien de changements seraient nécessaires ?

Exemple : Avec la version améliorée, ajouter une nouvelle conversion (ex. : Celsius → Fahrenheit) ne nécessite que
 l’ajout d’un nouveau choix et facteur.
Puis-je rendre mon code plus générique tout en restant simple ?

Exemple : En utilisant une fonction unique comme convertir(valeur, facteur_conversion), ton code devient générique 
tout en restant clair.




7. Sur l’expérience utilisateur :
Est-ce que les messages que j’affiche sont clairs et utiles ?

Exemple : Tu as ajouté des messages comme "Entrez une valeur ou Q pour quitter", ce qui améliore l’interaction.
Est-ce que mon programme réagit bien aux erreurs courantes de l’utilisateur ?

Exemple : La gestion des erreurs dans demander_valeur() garantit que ton programme ne plante pas si l’utilisateur entre
 autre chose qu’un nombre.
En te posant ces questions régulièrement, tu développes une façon de penser structurée pour identifier les répétitions 
et améliorer ton code. Avec la pratique, cela deviendra une seconde nature ! 😊




"""