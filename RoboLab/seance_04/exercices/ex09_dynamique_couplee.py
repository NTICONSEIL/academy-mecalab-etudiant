"""RoboLab S4 — étudiant — ex09_dynamique_couplee"""
import math
from support_s3 import ROBOT,calculer_couples

def coefficients(robot,charge):
    L1,L2,m1,m2,mp=(robot[k] for k in ('L1','L2','m1','m2','masse_pince'))
    m=mp+charge
    return (m1/3+m2+m)*L1**2,(m2/3+m)*L2**2,(m2/2+m)*L1*L2

def termes_dynamiques(robot,q,w,charge):
    A,B,D=coefficients(robot,charge)
    b=q[1]; w1,w2=w
    M=[[A+B+2*D*math.cos(b),B+D*math.cos(b)],[B+D*math.cos(b),B]]
    h=(-D*math.sin(b)*(2*w1*w2+w2*w2),D*math.sin(b)*w1*w1)
    G=calculer_couples(robot,*map(math.degrees,q),charge)
    return M,h,G

def couples(robot,q,w,a,charge):
    # TODO : calcul matriciel M*a + h + G
    raise NotImplementedError

if __name__ == '__main__':
    c=couples(ROBOT,(0,0),(0,0),(0,0),.5)
    assert all(math.isclose(x,y) for x,y in zip(c,(11.4777,3.2373)))
    c=couples(ROBOT,(0,0),(0,0),(1,0),.5)
    assert all(math.isclose(x,y) for x,y in zip(c,(12.1327,3.4563)))
