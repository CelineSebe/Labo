from labo_cmd import *


def main():
    irit = Labo()
    print(irit)
    ajouter(irit, "Xavier", "FBJO")
    print(irit)
    assert appartenir_labo(irit, "Xavier")
    assert not appartenir_labo(irit, "Sisi")
    assert obtenir_bureau(irit, "Xavier") == "FBJO"

    obtenir_listin()

    try:
        ajouter(irit, "Xavier", "FBJO")
        assert False

    except PresentException:
        print("Déjà enregistré")

    modifier_nom(irit, "Xavier", "xav")
    print(irit)


main()
