import math, random
from support_s5 import quintique

def simuler(mode='OPEN', pwm=60, gains=(1.,0.,0.), K=8., tau=.25, dt=.01, duree=4., charge=1., trajectoire=False, seed=6):
    if min(K,tau,dt,duree,charge)<=0 or dt>=2*tau*charge: raise ValueError('paramètres invalides')
    rng=random.Random(seed); q=w=integ=wf=0.; ancien=0.; rows=[]
    for k in range(round(duree/dt)+1):
        t=k*dt; ref=quintique(0,.5,2,t)[0] if trajectoire else .5
        n=round((q+rng.gauss(0,.0005))*2400/(2*math.pi)); qm=n*2*math.pi/2400
        wm=(qm-ancien)/dt if k else 0.; ancien=qm; wf=.2*wm+.8*wf
        e=ref-qm; kp,ki,kd=gains; cand=integ+e*dt
        raw=kp*e+ki*cand-kd*wf
        if not ((raw>.35 and e>0) or (raw<-.35 and e<0)): integ=cand
        u=pwm/255 if mode=='OPEN' else max(-.35,min(.35,kp*e+ki*integ-kd*wf))
        u=round(255*u)/255
        rows.append(dict(time_us=round(t*1e6),count=n,theta_rad=qm,omega_rad_s=wf,setpoint_rad=ref if mode!='OPEN' else 0.,pwm=round(u*255),error_rad=e if mode!='OPEN' else -qm))
        q,w=q+dt*w,w+dt*(K*u-w)/(tau*charge)
    return rows
