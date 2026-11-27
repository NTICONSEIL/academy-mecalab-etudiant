"""RoboLab S2 — ex05_cinematique_inverse.py : compléter les TODO."""
from ex03_angles_coude import angles_coude
from ex04_angle_epaule import angle_epaule

def normaliser(angle):
    # TODO : utiliser le modulo.
    raise NotImplementedError

def cinematique_inverse(L1,L2,x,y):
    # TODO : assembler les solutions, normaliser et éliminer les doublons.
    raise NotImplementedError

if __name__ == '__main__':
    for x,y in [(40,30),(70,0),(10,0),(80,0)]:
        try:
            print(x,y,cinematique_inverse(40,30,x,y))
        except ValueError as erreur:
            print(erreur)
