"""RoboLab S4 — étudiant — ex08_optimisation_duree"""
from ex06_couples_dynamiques import simuler
from ex07_puissance_energie import puissance_mecanique
LIMITES=((20,2,5,40),(8,3,8,24))

def verifier(T,charge=.5,N=200):
    # TODO : contrôler les 4 contraintes pour chaque axe ; axe 2 immobile
    # Retour booléen ; sécurité 1.5 sur couple uniquement
    raise NotImplementedError

def rechercher_duree(charge=.5,N=200):
    # TODO : centièmes entiers 50..500 inclus ; None si impossible
    raise NotImplementedError

if __name__ == '__main__':
    assert not verifier(1) and verifier(2)
    T=rechercher_duree()
    print(T)
    assert T is not None and verifier(T)
    assert not verifier(round(T-.01,2))
