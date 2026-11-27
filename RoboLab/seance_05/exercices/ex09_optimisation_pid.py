"""RoboLab S5 — EX09 — étudiant. Compléter les TODO."""
import math
from support_s4 import grille, simuler_articulation, simuler_mission, couples, ROBOT

from ex08_correcteur_pid import creer_loi

def evaluer(data, consigne=math.pi/4):
    # TODO : IAE par trapèzes, maxima, admissibilité S4
    raise NotImplementedError

def optimiser():
    # TODO : grille de gains du TP, nouvelle loi pour chaque essai
    raise NotImplementedError

if __name__ == "__main__":
    d=[dict(t=0,q=0,w=0,a=0,c=0,p=0),dict(t=1,q=1,w=0,a=0,c=0,p=0)]
    assert math.isclose(evaluer(d,1)['iae'],.5)
    print("Tests de base réussis")
