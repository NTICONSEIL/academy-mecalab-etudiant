"""RoboLab S3 — Étudiant : ex05_couples_moteurs.py"""
import math
from ex04_centres_gravite import position_robot, centres_gravite
from ex02_moment_force import moment_force
from ex01_poids import calculer_poids

ROBOT={'L1':.4,'L2':.3,'m1':1.2,'m2':.8,'masse_pince':.2,'couple_max_1':20.,'couple_max_2':8.,'securite':1.5}

def calculer_couples(robot,theta1,theta2,charge):
    # TODO : contrôler la charge, isoler les deux systèmes et compenser les moments
    raise NotImplementedError

def sollicitations(robot,theta1,theta2,charge):
    # TODO : retourner u1,u2 (fractions, pas pourcentages)
    raise NotImplementedError

def admissible(robot,theta1,theta2,charge):
    # TODO : vérifier simultanément les deux limites
    raise NotImplementedError

if __name__ == '__main__':
    print(calculer_couples(ROBOT,0,0,.5))
    assert admissible(ROBOT,0,0,.5)
