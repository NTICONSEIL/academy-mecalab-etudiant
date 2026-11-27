"""RoboLab S2 — ex07_visualisation.py : compléter les TODO."""
import matplotlib.pyplot as plt
from ex05_cinematique_inverse import cinematique_inverse
from ex06_validation import position_robot

def afficher_solutions(L1,L2,x,y):
    fig,ax=plt.subplots()
    # TODO : tracer les postures, la cible et les cercles (plt.Circle).
    ax.set(xlim=(-80,80),ylim=(-80,80),xlabel='X (cm)',ylabel='Y (cm)')
    ax.set_aspect('equal')
    ax.grid()
    # TODO : ajouter la légende.
    plt.show()

if __name__ == '__main__':
    afficher_solutions(40,30,40,30)
