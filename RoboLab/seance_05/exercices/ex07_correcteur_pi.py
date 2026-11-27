"""RoboLab S5 — EX07 — étudiant. Compléter les TODO."""
import math
from support_s4 import grille, simuler_articulation, simuler_mission, couples, ROBOT

def correcteur_pi(erreur, integrale, Kp, Ki, dt):
    # TODO : intégration rectangulaire et commande
    raise NotImplementedError

if __name__ == "__main__":
    u,I=correcteur_pi(.5,0,4,2,.1)
    assert math.isclose(I,.05) and math.isclose(u,2.1)
    print("Tests de base réussis")
