"""RoboLab S4 — étudiant — ex10_validation_mission"""
import math
from support_s2 import MISSION,cinematique_inverse,choisir_solution,ecart_angle
from support_s3 import ROBOT,calculer_couples
from ex02_profil_cubique import profil_cubique
from ex09_dynamique_couplee import couples
from ex07_puissance_energie import integrer_trapezes

def postures():
    q=cinematique_inverse(.4,.3,*MISSION[0]['cible'])[0]
    result=[tuple(map(math.radians,q))]
    for etape in MISSION[1:]:
        cible=choisir_solution(cinematique_inverse(.4,.3,*etape['cible']),q)
        q=tuple(a+ecart_angle(a,b) for a,b in zip(q,cible))
        result.append(tuple(map(math.radians,q)))
    return result

def mouvement(q0,q1,T,charge,N=200):
    result=[]
    for k in range(N+1):
        t=T*k/N
        q,w,a=zip(*(profil_cubique(x,y,T,t) for x,y in zip(q0,q1)))
        c=couples(ROBOT,q,w,a,charge)
        result.append(dict(t=t,q=q,w=w,a=a,c=c,p=tuple(x*y for x,y in zip(c,w))))
    return result

def mission(T,charge=.5,N=200):
    # TODO : 7 mouvements ; masse transportée après saisie jusqu'à dépose
    # Contrôler chaque axe, les états statiques avant/après changement de masse,
    # maxima absolus, travail positif/négatif par axe et durée 7*T.
    # Retour : dictionnaire avec duree, admissible, maxima, travaux
    raise NotImplementedError

if __name__ == '__main__':
    assert len(postures())==8
    for charge in (.5,1):
        for T in (1,2,4):
            b=mission(T,charge)
            assert math.isclose(b['duree'],7*T)
            print(charge,T,b)
