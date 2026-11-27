"""RoboLab S2 — ex03_angles_coude.py : compléter les TODO."""
import math
from ex01_accessibilite import est_accessible

def angles_coude(L1,L2,x,y):
    # TODO : vérifier la cible, calculer et borner le cosinus, retourner deux angles.
    raise NotImplementedError

if __name__ == '__main__':
    for x,y in [(40,30),(70,0),(10,0)]:
        print(x,y,angles_coude(40,30,x,y))
