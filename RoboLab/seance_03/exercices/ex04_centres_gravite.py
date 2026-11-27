"""RoboLab S3 — Étudiant : ex04_centres_gravite.py"""
import math

def position_robot(L1,L2,theta1,theta2):
    # TODO : retourner xA,yA,xP,yP en mètres
    raise NotImplementedError

def centres_gravite(L1,L2,theta1,theta2):
    # TODO : retourner xG1,yG1,xG2,yG2
    raise NotImplementedError

if __name__ == '__main__':
    for angles,attendu in [((0,0),(.2,0,.55,0)),((90,-90),(0,.2,.15,.4))]:
        assert all(math.isclose(a,b,abs_tol=1e-9) for a,b in zip(centres_gravite(.4,.3,*angles),attendu))
