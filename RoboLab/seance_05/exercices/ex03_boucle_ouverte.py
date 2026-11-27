"""RoboLab S5 — EX03 — étudiant. Compléter les TODO."""
import math
from support_s4 import grille, simuler_articulation, simuler_mission, couples, ROBOT

def simuler_boucle_ouverte(theta_initiale, omega_initiale, couple, J, b, duree, dt):
    # TODO : retourner temps, positions, vitesses
    raise NotImplementedError

if __name__ == "__main__":
    t,q,w=simuler_boucle_ouverte(0,0,1,.655,.8,2,.01)
    assert q[1]==0 and math.isclose(w[1],.01/.655)
    assert q[-1]>0
    print("Tests de base réussis")
