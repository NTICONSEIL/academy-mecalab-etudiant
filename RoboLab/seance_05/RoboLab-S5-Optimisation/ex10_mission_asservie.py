"""RoboLab S5 — EX10 — corrigé enseignant."""
import math
from support_s4 import grille, simuler_articulation, simuler_mission, couples, ROBOT

def creer_commande(mode, Kp=12., Ki=2., Kd=4.):
    if mode not in ('anticipation','pid','combine'): raise ValueError('Mode inconnu')
    I=[0.,0.]
    def loi(ref,etat,dt):
        ff=couples(ROBOT,ref['q'],ref['w'],ref['a'],ref['charge']) if mode!='pid' else (0.,0.)
        if mode=='anticipation': return ff
        c=[]
        for i,lim in enumerate((20,8)):
            e=ref['q'][i]-etat['q'][i]; de=ref['w'][i]-etat['w'][i]
            trial=I[i]+dt*e; raw=ff[i]+Kp*e+Ki*trial+Kd*de
            if not ((raw>lim and e>0) or (raw< -lim and e<0)): I[i]=trial
            c.append(ff[i]+Kp*e+Ki*I[i]+Kd*de)
        return tuple(c)
    return loi

def bilan(data):
    def integ(v): return sum((x+y)/2*(b['t']-a['t']) for x,y,a,b in zip(v,v[1:],data,data[1:]))
    T=data[-1]['t']-data[0]['t']
    e=[[math.degrees(r['q'][i]-r['mesure'][i]) for r in data] for i in range(2)]
    xy=[1000*math.dist(r['xy'],r['xy_ref']) for r in data]
    maxima={k:[max(abs(r[k][i]) for r in data) for i in range(2)] for k in ('c','vitesse','acceleration','p')}
    return dict(erreur_max_deg=[max(map(abs,v)) for v in e],erreur_rms_deg=[math.sqrt(integ([x*x for x in v])/T) for v in e],xy_max_mm=max(xy),xy_rms_mm=math.sqrt(integ([x*x for x in xy])/T),maxima=maxima,admissible=all(x<=l for k,lims in zip(maxima,((20/1.5,8/1.5),(2,3),(5,8),(40,24))) for x,l in zip(maxima[k],lims)),saturation_s=sum(b['t']-a['t'] for a,b in zip(data,data[1:]) if a['sature']),travail_positif=[integ([max(0,r['p'][i]) for r in data]) for i in range(2)],travail_negatif=[integ([min(0,r['p'][i]) for r in data]) for i in range(2)])

if __name__ == "__main__":
    loi=creer_commande('anticipation')
    ref=dict(q=(0,0),w=(0,0),a=(0,0),charge=.5)
    assert all(math.isclose(x,y) for x,y in zip(loi(ref,dict(q=(0,0),w=(0,0)),.005),(11.4777,3.2373)))
    print("Tests de base réussis")
