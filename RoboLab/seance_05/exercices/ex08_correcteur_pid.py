"""RoboLab S5 — EX08 — étudiant. Compléter les TODO."""
import math
from support_s4 import grille, simuler_articulation, simuler_mission, couples, ROBOT

def correcteur_pid(erreur, integrale, vitesse_mesuree, Kp, Ki, Kd, dt):
    # TODO : dérivée sur mesure, retourner commande et intégrale candidate
    raise NotImplementedError

def creer_loi(Kp, Ki, Kd, consigne=math.pi/4, anti_windup=True):
    # TODO : closure ou objet callable, mémoire intégrale indépendante
    # signature loi(t,q,w,g,dt), retourner correction sans g
    raise NotImplementedError

if __name__ == "__main__":
    u,I=correcteur_pid(.5,0,.2,4,2,3,.1)
    assert math.isclose(u,1.5) and math.isclose(I,.05)
    loi=creer_loi(8,2,3)
    assert callable(loi)
    print("Tests de base réussis")
