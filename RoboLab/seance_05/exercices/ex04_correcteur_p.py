"""RoboLab S5 — EX04 — étudiant. Compléter les TODO."""
import math
from support_s4 import grille, simuler_articulation, simuler_mission, couples, ROBOT

def correcteur_p(consigne, mesure, Kp):
    # TODO
    raise NotImplementedError

def simuler_p(Kp, consigne=math.pi/4, duree=10., dt=.01, perturbation=lambda t:0.):
    # TODO : appeler simuler_articulation avec une fonction loi
    raise NotImplementedError

if __name__ == "__main__":
    assert correcteur_p(1,.5,8)==4
    assert len(simuler_p(5))==1001
    print("Tests de base réussis")
