"""RoboLab S4 — étudiant — ex04_moments_inertie"""
import math

def inertie_masse_ponctuelle(masse,distance):
    raise NotImplementedError # TODO

def inertie_tige_extremite(masse,longueur):
    raise NotImplementedError # TODO

def huygens_steiner(Jg,masse,distance):
    raise NotImplementedError # TODO

if __name__ == '__main__':
    assert math.isclose(inertie_masse_ponctuelle(.5,.3),.045)
    assert math.isclose(inertie_tige_extremite(1.2,.4),.064)
    assert math.isclose(huygens_steiner(.016,1.2,.2),.064)
