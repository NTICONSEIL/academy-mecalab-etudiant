"""RoboLab S4 — étudiant — ex06_couples_dynamiques"""
import math
from support_s3 import ROBOT,calculer_couples
from ex02_profil_cubique import profil_cubique
from ex05_inertie_robot import inertie_epaule,inertie_coude

def couple_dynamique(couple_statique,inertie,acceleration):
    raise NotImplementedError # TODO

def simuler(T,charge=.5,N=200):
    # TODO : rotation épaule 0 -> pi/2, coude bloqué à 0
    # Retour : liste de dictionnaires t,q,w,a,c1,c2
    # M21 = J2 + (m2/2 + masse_pince + charge)*L1*L2
    # c2 = G2 + M21*a ; conversion radians -> degrés pour S3
    raise NotImplementedError

if __name__ == '__main__':
    s=simuler(2)
    print(s[0],s[-1])
    assert math.isclose(s[0]['c1'],11.4777+.655*3*math.pi/4)
    assert math.isclose(s[0]['c2'],3.2373+.219*3*math.pi/4)
