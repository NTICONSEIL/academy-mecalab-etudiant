"""Exercice 7 — Représentation graphique. Compléter les TODO."""

import matplotlib.pyplot as plt
from ex05_bras_articule import position_robot

def afficher_robot(L1, L2, theta1, theta2):
    # TODO : calculer les points et tracer les segments
    plt.xlim(-80, 80)
    plt.ylim(-80, 80)
    plt.gca().set_aspect('equal')
    plt.grid()
    plt.xlabel('X (cm)')
    plt.ylabel('Y (cm)')
    plt.title('RoboLab R2')
    plt.show()

if __name__ == '__main__':
    afficher_robot(40, 30, 45, -60)
