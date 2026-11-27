"""RoboLab S3 — Étudiant : ex07_cartographie.py"""
import matplotlib.pyplot as plt
from ex05_couples_moteurs import ROBOT,sollicitations

def cartographier(robot,charge):
    # TODO : retourner angles, matrice_u1, matrice_u2
    raise NotImplementedError

def afficher_cartes(angles,U1,U2):
    # TODO : deux cartes thermiques, origine basse, axes et barres de couleur
    raise NotImplementedError

if __name__ == '__main__':
    angles,U1,U2=cartographier(ROBOT,1.)
    assert len(angles)==len(U1)==len(U2)==72
    # TODO : compter les configurations admissibles pour les deux moteurs, maxima, refaire à .5 kg
    afficher_cartes(angles,U1,U2)
