"""RoboLab S2 — ex06_validation.py : compléter les TODO."""
import math
from ex05_cinematique_inverse import cinematique_inverse

def position_robot(L1,L2,theta1,theta2):
    """Modèle direct fourni, issu des équations S1."""
    a,b=math.radians(theta1),math.radians(theta2)
    xA,yA=L1*math.cos(a),L1*math.sin(a)
    return xA,yA,xA+L2*math.cos(a+b),yA+L2*math.sin(a+b)

def erreur_reconstruction(L1,L2,x,y,solution):
    # TODO : reconstruire P et calculer la distance à la cible.
    raise NotImplementedError

if __name__ == '__main__':
    cas=[(40,30,2),(-40,30,2),(-40,-30,2),(40,-30,2),(70,0,1),(10,0,1),(0,50,2)]
    # TODO : vérifier nombre de solutions et erreurs par assert.
    # TODO : vérifier le rejet de (80,0), (0,0), (3,4).
