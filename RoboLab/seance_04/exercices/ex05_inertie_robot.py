"""RoboLab S4 — étudiant — ex05_inertie_robot"""
import math
from support_s3 import ROBOT
from ex04_moments_inertie import inertie_tige_extremite,huygens_steiner,inertie_masse_ponctuelle

def inertie_coude(robot,charge):
    raise NotImplementedError # TODO

def inertie_epaule(robot,charge,b):
    # TODO : b en radians, coude bloqué
    raise NotImplementedError

if __name__ == '__main__':
    assert math.isclose(inertie_coude(ROBOT,.5),.087)
    assert math.isclose(inertie_epaule(ROBOT,.5,0),.655)
    assert math.isclose(inertie_epaule(ROBOT,.5,math.pi/2),.391)
