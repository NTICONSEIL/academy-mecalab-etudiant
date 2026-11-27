"""RoboLab S3 — Étudiant : ex01_poids.py"""
import math

def calculer_poids(masse, g=9.81):
    # TODO : contrôler les entrées et calculer le poids
    raise NotImplementedError

if __name__ == '__main__':
    composants = [{'nom':'segment 1','masse':1.2}, {'nom':'segment 2','masse':0.8}, {'nom':'pince','masse':0.2}, {'nom':'pièce','masse':0.5}]
    # TODO : afficher chaque poids et cumuler le total
    assert math.isclose(calculer_poids(2.7),26.487,abs_tol=1e-9)
