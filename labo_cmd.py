

class LaboException(Exception):
    """ Généralise les exceptions du laboratoire."""
    pass


class AbsentException(LaboException):
    pass


class PresentException(LaboException):
    pass


def Labo():

    return {}


def ajouter(labo, nom, bureau):
    if nom in labo:
        raise PresentException
    labo[nom] = bureau
    print(nom + " est ajouté au bureau " + bureau)


def supprimer(labo, nom):
    if not nom in labo:
        raise AbsentException
    else:
        labo.pop(nom)
        print(nom + "a été supprimé de la liste")


def modifier_nom(labo, nom, nv_nom):
    if not nom in labo:
        raise AbsentException
    else:
        labo[nom] = nv_nom


def modifier_bureau(labo, nom, nv_bureau):
    if not nom in labo:
        raise AbsentException
    else:
        labo[nom] = nv_bureau


def appartenir_labo(labo, nom):
    return nom in labo


def obtenir_bureau(labo, nom):
    if not nom in labo:
        raise AbsentException
    else:
        return labo[nom]


def obtenir_listin(labo):
    for nom, bureau in labo.items():
        print("Nom: {0}, Value: {1}" .format(nom, bureau))


def occupation_bureau(labo):
    bureaux = {}

    for nom, bureau in labo.items():
        if bureau in bureaux:
            bureaux[bureau].append(nom)
        else:
            bureaux[bureau] = [nom]
    return bureaux
