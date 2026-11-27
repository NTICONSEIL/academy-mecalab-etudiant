"""RoboLab S3 — Étudiant : ex08_charge_maximale.py"""
from ex05_couples_moteurs import ROBOT,admissible

def bornes_charge(robot):
    # TODO : retourner les deux bornes analytiques à l'horizontale
    raise NotImplementedError

def recherche_charge(robot,pas=.001,limite=5.):
    # TODO : recherche par multiples entiers du pas ; gérer le cas à vide et la limite de recherche
    raise NotImplementedError

if __name__ == '__main__':
    b1,b2=bornes_charge(ROBOT)
    print(b1,b2,recherche_charge(ROBOT))
