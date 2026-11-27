"""RoboLab S2 — ex04_angle_epaule.py : compléter les TODO."""
import math
from ex03_angles_coude import angles_coude

def angle_epaule(L1,L2,x,y,theta2):
    # TODO : convertir theta2, calculer les deux orientations et leur différence.
    raise NotImplementedError

if __name__ == '__main__':
    for b in angles_coude(40,30,40,30):
        print(angle_epaule(40,30,40,30,b),b)
