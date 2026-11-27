"""RoboLab S4 — étudiant — ex02_profil_cubique"""
import math

def profil_cubique(theta_depart, theta_fin, T, t):
    # TODO : retourner theta, omega, alpha en SI
    raise NotImplementedError

if __name__ == '__main__':
    for t in (0,.5,1,1.5,2): print(t,profil_cubique(0,math.pi/2,2,t))
    q,w,a=profil_cubique(0,math.pi/2,2,1)
    assert math.isclose(q,math.pi/4) and math.isclose(w,3*math.pi/8) and abs(a)<1e-10
