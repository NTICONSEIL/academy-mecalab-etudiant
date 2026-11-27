"""RoboLab S4 — étudiant — ex07_puissance_energie"""
import math
import matplotlib.pyplot as plt
from ex06_couples_dynamiques import simuler

def puissance_mecanique(couple,vitesse):
    raise NotImplementedError # TODO

def integrer_trapezes(valeurs,dt):
    raise NotImplementedError # TODO

def bilan(T,charge=.5,N=200):
    # TODO : retourner (travail net, positif, négatif), tracer P et travail cumulé dans main
    raise NotImplementedError

if __name__ == '__main__':
    net,pos,neg=bilan(2,N=1000)
    print(net,pos,neg)
    assert abs(net-11.4777)<1e-4
    assert math.isclose(net,pos+neg,abs_tol=1e-9)
