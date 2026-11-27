"""Support S3 autonome : angles en degrés (interface historique)."""
import math
ROBOT={'L1':.4,'L2':.3,'m1':1.2,'m2':.8,'masse_pince':.2,'couple_max_1':20.,'couple_max_2':8.,'securite':1.5}
def calculer_couples(robot,theta1,theta2,charge):
    if not math.isfinite(charge) or charge < 0: raise ValueError('Charge invalide')
    a,b=map(math.radians,(theta1,theta2))
    L1,L2,m1,m2,mp=(robot[k] for k in ('L1','L2','m1','m2','masse_pince'))
    m=mp+charge
    c2=9.81*(m2/2+m)*L2*math.cos(a+b)
    return 9.81*(m1/2+m2+m)*L1*math.cos(a)+c2,c2

def sollicitations(robot,theta1,theta2,charge):
    c=calculer_couples(robot,theta1,theta2,charge)
    return tuple(robot['securite']*abs(v)/robot[f'couple_max_{i}'] for i,v in enumerate(c,1))
def admissible(robot,theta1,theta2,charge):
    return max(sollicitations(robot,theta1,theta2,charge))<=1
