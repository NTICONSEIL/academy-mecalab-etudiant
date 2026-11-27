"""RoboLab S5 — EX10 — étudiant. Compléter les TODO."""
import math
from support_s4 import grille, simuler_articulation, simuler_mission, couples, ROBOT

def creer_commande(mode, Kp=12., Ki=2., Kd=4.):
    # TODO : modes anticipation, pid, combine ; mémoire sur deux axes
    # loi(ref,etat,dt) retourne les deux couples totaux
    raise NotImplementedError

def bilan(data):
    # TODO : erreurs articulaires/cartésiennes, maxima, énergie, saturation
    raise NotImplementedError

if __name__ == "__main__":
    loi=creer_commande('anticipation')
    ref=dict(q=(0,0),w=(0,0),a=(0,0),charge=.5)
    assert all(math.isclose(x,y) for x,y in zip(loi(ref,dict(q=(0,0),w=(0,0)),.005),(11.4777,3.2373)))
    print("Tests de base réussis")
