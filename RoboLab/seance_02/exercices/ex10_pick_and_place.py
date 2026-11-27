"""RoboLab S2 — ex10_pick_and_place.py : compléter les TODO."""
import matplotlib.pyplot as plt
from ex05_cinematique_inverse import cinematique_inverse
from ex06_validation import position_robot
from ex09_trajectoire import planifier

MISSION=[{'cible':(60,0),'action':'attente'}, {'cible':(50,20),'action':'approche'},
         {'cible':(50,10),'action':'saisie'}, {'cible':(50,30),'action':'degagement'},
         {'cible':(20,50),'action':'transfert'}, {'cible':(20,30),'action':'depose'},
         {'cible':(20,50),'action':'degagement'}, {'cible':(60,0),'action':'attente'}]

def preparer_mission(L1,L2,mission,N=20):
    # TODO : initialiser, planifier tous les segments, gérer l'état de la pince.
    # Retour attendu : liste de tuples (theta1,theta2,etat).
    raise NotImplementedError

def animer(L1,L2,images):
    # TODO : tracer chaque posture avec des limites fixes et afficher l'état.
    # Utiliser plt.pause(0.05), puis plt.show().
    raise NotImplementedError

if __name__ == '__main__':
    images=preparer_mission(40,30,MISSION)
    animer(40,30,images)
