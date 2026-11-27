"""Exercice 8 — Espace de travail. Compléter les TODO."""

import math
import matplotlib.pyplot as plt
from ex05_bras_articule import position_robot

def espace_travail(L1, L2):
    xs, ys = [], []
    for theta1 in range(0, 360, 10):
        for theta2 in range(0, 360, 10):
            # TODO : calculer et stocker P
            pass
    return xs, ys

if __name__ == '__main__':
    xs, ys = espace_travail(40, 30)
    # TODO : contrôler les distances et tracer le nuage
    pass
