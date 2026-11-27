"""RoboLab S2 — ex01_accessibilite.py : compléter les TODO."""
import math

def est_accessible(L1, L2, x, y):
    # TODO : contrôler les entrées, calculer la distance et tester les bornes.
    raise NotImplementedError

if __name__ == '__main__':
    for x,y in [(40,30),(70,0),(10,0),(80,0),(3,4),(0,0)]:
        print(x,y,est_accessible(40,30,x,y))
