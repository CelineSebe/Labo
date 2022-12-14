from labo_cmd import *


def main():
    quitter = False
    labo = Labo()
    ajouter(labo, "celine", "70")
    ajouter(labo, "Dinah", "60")
    ajouter(labo, "Dih", "60")

    while not quitter:
        print(labo)
        print()
        # afficher le menu
        print("1- Enregistrer une nouvelle personne")
        print("2- Enregistrer le départ d'une personne")
        print("3- Modifier le bureau occupé par une personne")
        print("4- Changer le nom d'une personne du laboratoire")
        print("5- Savoir si une personne est membre du laboratoire")
        print("6- Obtenir le bureau d'une personne")
        print("7- Donner le listing de tous les personnels avec le bureau occupé")
        print("8- Afficher l'occupation des bureaux en mode texte")

        # sélectionner un choix
        choice = int(input("Votre choix : "))

        # traiter le choix
        if choice == 1:
            # enregistrer une nouvelle personne
            print("Ajouter une personne")
            nom = str(input("Nom : "))
            print("Ajouter un bureau: ")
            bureau = str(input("Bureau: "))
            ajouter(labo, nom, bureau)

        elif choice == 2:
            # enregistrer le départ d'une nouvelle personne
            print("Supprimer une personne: ")
            nom = str(input("Nom : "))
            supprimer(labo, nom)

        elif choice == 3:
            # modifier le bureau d'une personne
            print("Vous souhaitez modifier le bureau, donner le nom de la personne: ")
            nom = str(input("Nom : "))
            print("Ajouter un nouveau bureau: ")
            bureau = str(input("Bureau: "))
            modifier_bureau(labo, nom, bureau)

        elif choice == 4:
            # modifier le nom d'une personne
            print("Vous souhaitez modifier un bureau, donner le nom de la personne: ")
            nom = str(input("Nom : "))
            print("Ajouter un nouveau nom: ")
            nv_nom = str(input("Nom : "))
            modifier_nom(labo, nom, nv_nom)

        elif choice == 5:
            # savoir si une personne est dans le Labo
            print("Vous souhaitez savoir si quelqu'un est listé.")
            print("Donner le nom de la personne: ")
            nom = str(input("Nom : "))
            appartenir_labo(labo, nom)

        elif choice == 6:
            # obtenir le bureau d'une personne
            print("Vous souhaitez obtenir le bureau de quelqu'un déjà listé.")
            print("Donner le nom de la personne: ")
            nom = str(input("Nom : "))
            bureau = obtenir_bureau(labo, nom)

        elif choice == 7:
            # donner le listing de tous les personnels
            print("Vous souhaitez obtenir le listing complet.")
            obtenir_listin(labo)

        elif choice == 8:
            # afficher_bureau({'B105': ['Jean', 'Claude'], 'B106': ['Pierre']})
            bureaux = occuper_bureau(labo)
            print("bureaux =", bureaux)
            afficher_bureau(bureaux)
            ecrire_bureau(bureaux)

        else:
            quitter = True


def ecrire_bureau(bureaux):

    occupants = './occupants.html'

    with open(occupants, 'w') as fichier:
        for bureau, nom in sorted(bureaux.items()):
            fichier.write('<p>' + bureau + ':' + '<p>')
            print("\n")
            fichier.write('<ul>')
            fichier.write('<li>' + str(nom[0]) + '</li>')
            fichier.write('<li>' + str(nom[1]) + '</li>')
            fichier.write('</ul>')


def afficher_bureau(bureaux):
    for key in bureaux:
        print(key, bureaux[key])
        print()


main()
