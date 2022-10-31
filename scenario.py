from labo_cmd import *


def main():
    irit = labo()
    print(irit)
    ajouter(irit, "Xavier", "FBJO")
    print(irit)
    try:
        ajouter(irit, 'Xavier', 'FBJO')
        assert False
    except PresentException:
        print("Déjà enregistré")


main()
