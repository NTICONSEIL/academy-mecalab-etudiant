"""RoboLab S3 — Étudiant : ex03_influence_angle.py"""
import matplotlib.pyplot as plt
from ex02_moment_force import moment_poids

def explorer_moments(masse,longueur):
    # TODO : retourner deux listes (angles, moments)
    raise NotImplementedError

if __name__ == '__main__':
    angles,moments=explorer_moments(1,.4)
    assert len(angles)==len(moments)==73
    # TODO : extrema, angles de moment nul, graphique légendé
