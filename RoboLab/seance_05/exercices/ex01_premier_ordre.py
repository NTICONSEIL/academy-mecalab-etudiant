"""RoboLab S5 — EX01 — étudiant. Compléter les TODO."""
import math
from support_s4 import grille, simuler_articulation, simuler_mission, couples, ROBOT

def vitesse_analytique(t, J, b, couple):
    # TODO : solution exacte, vérifier J et b positifs
    raise NotImplementedError

if __name__ == "__main__":
    assert math.isclose(vitesse_analytique(0,.655,.8,1),0)
    assert math.isclose(vitesse_analytique(.655/.8,.655,.8,1),1.25*(1-math.exp(-1)))
    print("Tests de base réussis")
