"""RoboLab S4 — étudiant — ex01_vitesse_acceleration"""
def calculer_vitesses(positions, dt):
    # TODO : différences premières, valider dt > 0
    raise NotImplementedError

def calculer_accelerations(vitesses, dt):
    # TODO : différences premières des vitesses
    raise NotImplementedError

if __name__ == '__main__':
    v=calculer_vitesses([0,.04,.16,.36,.64,1],.2)
    a=calculer_accelerations(v,.2)
    print(v,a)
    assert len(v)==5 and len(a)==4
    assert all(abs(x-2)<1e-9 for x in a)
