from labo_cmd import *


def main():
    quitter = False
    while not quitter:
        # afficher le menu
        print("1- Enregistrer une nouvelle personne")
        print("2- Supprimer les infos d'une personne")
        print("3- Modifier les infos d'une personne")
        print("4- Quitter")

        # demander le choix
        choice = int(input("Votre choix : "))

        # traiter le choix
        if choice == 1:
            ajouter()
        elif choice == 2:
            supprimer()
        elif choice == 3:
            modifier()
        else:
            quitter = True


main()
