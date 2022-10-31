class LaboException(Exception):
    """ Généralise les exceptions du laboratoire."""
    pass


class AbsentException(LaboException):
    pass


class PresentException(LaboException):
    pass


def Labo():
    return {}


def ajouter(Labo, nom, bureau):
    if nom in Labo:
        raise PresentException
    Labo[nom] = bureau
