"""RoboLab S2 — ex08_selection_solution.py : compléter les TODO."""
from ex05_cinematique_inverse import cinematique_inverse

def ecart_angle(a,b):
    # TODO : déplacement signé minimal de a vers b.
    raise NotImplementedError

def cout(depart,arrivee):
    # TODO : somme des valeurs absolues des écarts.
    raise NotImplementedError

def choisir_solution(solutions,depart):
    # TODO : comparer les coûts, garder la première en cas d'égalité.
    raise NotImplementedError

if __name__ == '__main__':
    solutions=cinematique_inverse(40,30,40,30)
    print(ecart_angle(179,-179))
    for depart in [(0,80),(70,-80)]:
        print(choisir_solution(solutions,depart))
