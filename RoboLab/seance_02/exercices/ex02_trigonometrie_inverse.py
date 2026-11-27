"""RoboLab S2 — ex02_trigonometrie_inverse.py : compléter les TODO."""
import math

def orientation(x,y):
    # TODO : refuser l'origine et retourner l'orientation en degrés.
    raise NotImplementedError

if __name__ == '__main__':
    # TODO : afficher acos(0.5), comparer atan et atan2 sans division par zéro.
    for x,y in [(1,1),(-1,1),(-1,-1),(1,-1),(0,1),(0,-1),(1,0),(-1,0)]:
        print(x,y,orientation(x,y))
