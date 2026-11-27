"""RoboLab S3 — Étudiant : ex02_moment_force.py"""
import math
from ex01_poids import calculer_poids

def moment_force(x,y,Fx,Fy):
    # TODO : composante z du produit vectoriel
    raise NotImplementedError

def moment_poids(masse,longueur,angle):
    # TODO : coordonnées, poids vertical et moment
    raise NotImplementedError

if __name__ == '__main__':
    assert moment_force(0,2,3,0)==-6
    for a in [0,30,60,90,180]:
        print(a,moment_poids(1,.4,a))
