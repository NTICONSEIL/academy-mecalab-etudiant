"""RoboLab S3 — Étudiant : ex09_validation_mission.py"""
import matplotlib.pyplot as plt
from support_s2 import preparer_mission
from ex05_couples_moteurs import ROBOT,calculer_couples,sollicitations

def analyser_mission(robot,images,masse_piece):
    # TODO : liste de dictionnaires indice, charge, C1,C2,u1,u2
    raise NotImplementedError

if __name__ == '__main__':
    images=preparer_mission()
    assert len(images)==141
    bilan=analyser_mission(ROBOT,images,.5)
    # TODO : contrôle avant dépose, maxima, courbes, second essai à 1 kg
