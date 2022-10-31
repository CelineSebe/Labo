from labo_cmd import *


def main():
    irit = Labo()
    print(irit)
    ajouter(irit, "Xavier", "FBJO")
    print(irit)
    try:
        ajouter(irit, 'Xavier', 'FBJO')
        assert False
    except PresentException:
        print("Déjà enregistré")


main()


def depart():
    irit = Labo()
    print(irit)
    supprimer(irit, "Xavier", "FBJO")
    try:
        supprimer(irit, "Xavier", "FBJO")
    except AbsentException:
        print("Non trouvé")


depart()
