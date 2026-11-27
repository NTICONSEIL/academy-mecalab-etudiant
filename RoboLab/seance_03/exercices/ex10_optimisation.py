"""RoboLab S3 — Étudiant : ex10_optimisation.py"""
from support_s2 import cinematique_inverse
from ex05_couples_moteurs import ROBOT,sollicitations

def choisir_posture(robot,x,y,charge):
    # TODO : comparer J des solutions ; retourner ((theta1,theta2),J)
    raise NotImplementedError

if __name__ == '__main__':
    posture,J=choisir_posture(ROBOT,.4,.3,.5)
    print(posture,J)
    # TODO : signaler non-admissibilité, tester cible inaccessible
