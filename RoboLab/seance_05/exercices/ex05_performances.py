"""RoboLab S5 — EX05 — étudiant. Compléter les TODO."""
import math
from support_s4 import grille, simuler_articulation, simuler_mission, couples, ROBOT

def calculer_depassement(positions, consigne):
    # TODO : échelon positif depuis zéro, résultat en %
    raise NotImplementedError

def calculer_temps_reponse(temps, positions, consigne):
    # TODO : dernier point hors bande ±5 %, None si non établi
    raise NotImplementedError

def calculer_erreur_finale(positions, consigne):
    # TODO : erreur signée, radians
    raise NotImplementedError

if __name__ == "__main__":
    assert math.isclose(calculer_depassement([0,1.2,1],1),20)
    assert calculer_temps_reponse([0,1,2,3],[0,1,1.2,1],1)==3
    assert calculer_temps_reponse([0,1],[0,.8],1) is None
    assert math.isclose(calculer_erreur_finale([.9],1),.1)
    print("Tests de base réussis")
