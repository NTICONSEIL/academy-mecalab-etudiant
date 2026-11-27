"""Exercice 10 — Animation du mouvement (bonus). Compléter les TODO."""

import matplotlib.pyplot as plt
from ex05_bras_articule import position_robot
from ex09_trajectoire import configurations

def animer():
    fig, ax = plt.subplots()
    bras, = ax.plot([], [], 'o-', linewidth=3)
    trace, = ax.plot([], [], '--')
    ax.set(xlim=(-80,80), ylim=(-80,80), xlabel='X (cm)', ylabel='Y (cm)')
    ax.set_aspect('equal')
    ax.grid()
    xs, ys = [], []
    for theta1, theta2 in configurations((0,0), (90,-90), 20):
        if not plt.fignum_exists(fig.number):
            break
        # TODO : calculer A et P, actualiser bras et trace
        plt.pause(0.1)
    plt.show()

if __name__ == '__main__':
    animer()
