"""Support S4 et moteur de simulation fourni pour S5. SI, angles en radians."""
import math
from support_s2 import MISSION, cinematique_inverse, choisir_solution, ecart_angle
from support_s3 import ROBOT, calculer_couples

def profil_cubique(theta_depart, theta_fin, T, t):
    if T<=0 or not 0<=t<=T: raise ValueError('Temps invalide')
    u=t/T
    d=theta_fin-theta_depart
    return theta_depart+d*(3*u*u-2*u**3), d/T*(6*u-6*u*u), d/T**2*(6-12*u)


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
    M,h,G=termes_dynamiques(robot,q,w,charge)
    return tuple(sum(x*y for x,y in zip(row,a))+hi+gi for row,hi,gi in zip(M,h,G))


def postures():
    q=cinematique_inverse(.4,.3,*MISSION[0]['cible'])[0]
    result=[tuple(map(math.radians,q))]
    for etape in MISSION[1:]:
        cible=choisir_solution(cinematique_inverse(.4,.3,*etape['cible']),q)
        q=tuple(a+ecart_angle(a,b) for a,b in zip(q,cible))
        result.append(tuple(map(math.radians,q)))
    return result


J, B = .655, .8

def grille(duree, dt):
    if not (math.isfinite(duree) and math.isfinite(dt) and duree>0 and dt>0):
        raise ValueError("Durée et pas positifs requis")
    n=round(duree/dt)
    if n<1 or not math.isclose(n*dt,duree):
        raise ValueError("La durée doit être un multiple du pas")
    return [k*dt for k in range(n+1)]

def simuler_articulation(loi, duree=10., dt=.01, perturbation=lambda t:0., gravite=False, saturation=False):
    """loi(t,q,w,g,dt) retourne le couple correctif; g est la compensation."""
    q=w=0.; data=[]
    for t in grille(duree,dt):
        g=11.4777*math.cos(q) if gravite else 0.
        brut=g+loi(t,q,w,g,dt)
        c=max(-20.,min(20.,brut)) if saturation else brut
        a=(c-g-B*w+perturbation(t))/J
        data.append(dict(t=t,q=q,w=w,a=a,c=c,p=c*w,sature=abs(brut-c)>1e-10))
        q,w=q+dt*w,w+dt*a
    return data

def xy(q):
    a,b=q
    return (.4*math.cos(a)+.3*math.cos(a+b),.4*math.sin(a)+.3*math.sin(a+b))

def simuler_mission(loi,T=2.,dt=.005,charge=.5,charge_reelle=.6):
    """loi(ref,etat,dt) retourne deux couples totaux. Pas de remise à zéro entre segments.
    Saisie/dépose programmées, sans impact ni collision; masse nominale et réelle distinctes.
    """
    qs=postures(); q=qs[0]; w=(0.,0.); data=[]; m=mr=0.
    for j,(q0,q1) in enumerate(zip(qs,qs[1:]),1):
        ts=grille(T,dt)
        for k,t in enumerate(ts):
            qr,wr,ar=zip(*(profil_cubique(x,y,T,min(t,T)) for x,y in zip(q0,q1)))
            ref=dict(q=qr,w=wr,a=ar,charge=m,segment=j,t=(j-1)*T+t)
            brut=tuple(loi(ref,dict(q=q,w=w),dt if k<len(ts)-1 else 0.))
            c=tuple(max(-lim,min(lim,v)) for v,lim in zip(brut,(20.,8.)))
            M,h,G=termes_dynamiques(ROBOT,q,w,mr)
            d=(-.4 if 5<=ref['t']<6 else 0.,0.)
            z=[c[i]-h[i]-G[i]-(.8,.3)[i]*w[i]+d[i] for i in range(2)]
            det=M[0][0]*M[1][1]-M[0][1]**2
            a=((M[1][1]*z[0]-M[0][1]*z[1])/det,(M[0][0]*z[1]-M[0][1]*z[0])/det)
            data.append(dict(**ref,mesure=q,vitesse=w,acceleration=a,c=c,p=tuple(x*y for x,y in zip(c,w)),sature=any(abs(x-y)>1e-10 for x,y in zip(c,brut)),xy=xy(q),xy_ref=xy(qr)))
            if k<len(ts)-1: q,w=tuple(x+dt*y for x,y in zip(q,w)),tuple(x+dt*y for x,y in zip(w,a))
        action=MISSION[j]['action']
        if action=='saisie': m,mr=charge,charge_reelle
        elif action=='depose': m=mr=0.
    return data
