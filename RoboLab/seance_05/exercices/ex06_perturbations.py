"""RoboLab S5 — EX06 — étudiant. Compléter les TODO."""
import math
from support_s4 import grille, simuler_articulation, simuler_mission, couples, ROBOT

from ex04_correcteur_p import simuler_p

def perturbation(t):
    # TODO : -1 N.m dès t=5 s
    raise NotImplementedError

def erreur_theorique(Kp):
    # TODO : erreur permanente en rad
    raise NotImplementedError

if __name__ == "__main__":
    assert perturbation(4.99)==0 and perturbation(5)==-1
    assert math.isclose(erreur_theorique(10),.1)
    print("Tests de base réussis")
