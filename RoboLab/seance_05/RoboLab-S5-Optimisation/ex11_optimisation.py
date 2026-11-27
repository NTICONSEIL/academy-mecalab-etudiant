"""Optimisation reproductible, modèle S5 inchangé hors commande et profil."""
import math,itertools
import support_s4 as s
from ex10_mission_asservie import bilan,creer_commande

def quintique(x,y,T,t):
    u=t/T; d=y-x
    return x+d*(10*u**3-15*u**4+6*u**5),d/T*(30*u**2-60*u**3+30*u**4),d/T**2*(60*u-180*u**2+120*u**3)

CUBIQUE=s.profil_cubique

def commande(gains, friction=True):
    I=[0.,0.]
    def loi(ref,etat,dt):
        ff=s.couples(s.ROBOT,ref['q'],ref['w'],ref['a'],ref['charge']); out=[]
        for i,(kp,ki,kd) in enumerate(gains):
            f=ff[i]+((.8,.3)[i]*ref['w'][i] if friction else 0)
            e=ref['q'][i]-etat['q'][i]; de=ref['w'][i]-etat['w'][i]; lim=(20,8)[i]
            trial=I[i]+dt*e; raw=f+kp*e+ki*trial+kd*de
            if not ((raw>lim and e>0) or (raw< -lim and e<0)): I[i]=trial
            out.append(f+kp*e+ki*I[i]+kd*de)
        return tuple(out)
    return loi

def sim(gains,T=2,dt=.005,profil='quintique',friction=True,charge=.6):
    old=s.profil_cubique
    try:
        s.profil_cubique=quintique if profil=='quintique' else CUBIQUE
        return s.simuler_mission(commande(gains,friction),T,dt,charge_reelle=charge)
    finally: s.profil_cubique=old

def evaluer(data):
    b=bilan(data); b['duree']=data[-1]['t']; b['points_mm']=[1000*math.dist(r['xy'],r['xy_ref']) for i,r in enumerate(data) if i==len(data)-1 or data[i+1]['segment']!=r['segment']]; b['valide']=b['admissible'] and b['xy_rms_mm']<=10 and b['xy_max_mm']<=20 and max(b['points_mm'][1],b['points_mm'][4])<=10
    return b

def recherche():
    results=[]
    for T,profil,g1,g2 in itertools.product((1.5,2.,2.5,3.),('cubique','quintique'),((12,2,4),(24,4,6),(40,6,8)),((8,1,2),(16,3,3),(24,4,4))):
        gains=(g1,g2); b=evaluer(sim(gains,T,.01,profil)); results.append(dict(T=T,profil=profil,gains=gains,**b))
    return sorted(results,key=lambda b:(not b['valide'],b['T'] if b['valide'] else b['xy_rms_mm'],b['xy_rms_mm']))

if __name__=='__main__':
    import json
    r=recherche(); print('valides',sum(x['valide'] for x in r)); print(r[:3]); print('baseline',evaluer(s.simuler_mission(creer_commande('combine')))); print('fin',evaluer(sim(r[0]['gains'],r[0]['T'],.0025,r[0]['profil']))); open('recherche.json','w').write(json.dumps(r,indent=2))
