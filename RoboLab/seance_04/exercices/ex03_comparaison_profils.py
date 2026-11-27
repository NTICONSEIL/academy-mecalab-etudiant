"""RoboLab S4 — étudiant — ex03_comparaison_profils"""
import math
import matplotlib.pyplot as plt
from ex02_profil_cubique import profil_cubique

def series(T,N=200):
    # TODO : retourner liste de (t,theta,omega,alpha), N+1 points
    raise NotImplementedError

if __name__ == '__main__':
    fig,axes=plt.subplots(3,1,sharex=True)
    for T in (1,2,4):
        data=series(T)
        # TODO : tracer chaque grandeur en fonction de t/T, légendes et unités
        assert len(data)==201
    plt.show()
