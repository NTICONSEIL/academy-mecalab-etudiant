"""RoboLab S5 — EX02 — étudiant. Compléter les TODO."""
import math
from support_s4 import grille, simuler_articulation, simuler_mission, couples, ROBOT

def simuler_euler(J, b, couple, duree, dt):
    # TODO : grille, vitesse initiale nulle, Euler explicite
    raise NotImplementedError

if __name__ == "__main__":
    t,w=simuler_euler(.655,.8,1,2,.01)
    assert len(t)==len(w)==201
    assert math.isclose(w[1],.01/.655)
    print("Tests de base réussis")
