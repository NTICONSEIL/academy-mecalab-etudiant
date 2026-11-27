def quintique(q0,qf,T,t):
    if T <= 0: raise ValueError('T positif requis')
    u=max(0.,min(1.,t/T)); d=qf-q0
    return q0+d*(10*u**3-15*u**4+6*u**5), d/T*(30*u**2-60*u**3+30*u**4), d/T**2*(60*u-180*u**2+120*u**3)
