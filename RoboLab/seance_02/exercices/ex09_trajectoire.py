"""RoboLab S2 — ex09_trajectoire.py : compléter les TODO."""
import math
import matplotlib.pyplot as plt
from ex01_accessibilite import est_accessible
from ex05_cinematique_inverse import cinematique_inverse
from ex06_validation import position_robot
from ex08_selection_solution import choisir_solution,ecart_angle

def segment_accessible(L1,L2,depart,arrivee):
    # TODO : vérifier les extrémités puis la distance minimale du segment.
    raise NotImplementedError

def points_segment(depart,arrivee,N):
    # TODO : vérifier N, retourner N+1 tuples (x,y).
    raise NotImplementedError

def planifier(L1,L2,depart,arrivee,N,angles_depart):
    # TODO : vérifier le segment, calculer les postures successives.
    # TODO : déplier les angles avec ecart_angle ; retourner N+1 tuples.
    raise NotImplementedError

if __name__ == '__main__':
    configurations=planifier(40,30,(70,0),(30,40),20,(0,0))
    # TODO : reconstruire, vérifier et tracer les positions.
    # TODO : tester un segment inaccessible même avec N=1.
