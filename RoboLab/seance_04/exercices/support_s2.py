"""Support fourni : cinématique et mission S2. Interface en mètres, angles en degrés."""

import math

def est_accessible(L1, L2, x, y):
    if not all((math.isfinite(v) for v in (L1, L2, x, y))) or min(L1, L2) <= 0 or L1 == L2:
        raise ValueError('Longueurs positives distinctes et valeurs finies requises')
    d = math.hypot(x, y)
    return abs(L1 - L2) - 1e-10 <= d <= L1 + L2 + 1e-10

def angles_coude(L1, L2, x, y):
    if not est_accessible(L1, L2, x, y):
        raise ValueError('Cible inaccessible')
    c = (x * x + y * y - L1 * L1 - L2 * L2) / (2 * L1 * L2)
    c = max(-1.0, min(1.0, c))
    b = math.degrees(math.acos(c))
    return (b, -b)

def angle_epaule(L1, L2, x, y, theta2):
    b = math.radians(theta2)
    return math.degrees(math.atan2(y, x) - math.atan2(L2 * math.sin(b), L1 + L2 * math.cos(b)))

def normaliser(angle):
    return (angle + 180) % 360 - 180

def cinematique_inverse(L1, L2, x, y):
    solutions = []
    for b in angles_coude(L1, L2, x, y):
        a = angle_epaule(L1, L2, x, y, b)
        q = (normaliser(a), normaliser(b))
        if not any((all((abs(normaliser(v - w)) <= 1e-07 for v, w in zip(q, s))) for s in solutions)):
            solutions.append(q)
    return solutions

def ecart_angle(a, b):
    return (b - a + 180) % 360 - 180

def cout(depart, arrivee):
    return sum((abs(ecart_angle(a, b)) for a, b in zip(depart, arrivee)))

def choisir_solution(solutions, depart):
    if not solutions:
        raise ValueError('Aucune solution')
    return min(solutions, key=lambda q: cout(depart, q))

def segment_accessible(L1, L2, depart, arrivee):
    if not (est_accessible(L1, L2, *depart) and est_accessible(L1, L2, *arrivee)):
        return False
    x, y = depart
    u, v = (arrivee[0] - x, arrivee[1] - y)
    norme2 = u * u + v * v
    t = max(0, min(1, -(x * u + y * v) / norme2)) if norme2 else 0
    return math.hypot(x + t * u, y + t * v) >= abs(L1 - L2) - 1e-10

def points_segment(depart, arrivee, N):
    if type(N) is not int or N <= 0:
        raise ValueError('N entier positif requis')
    return [(depart[0] + k / N * (arrivee[0] - depart[0]), depart[1] + k / N * (arrivee[1] - depart[1])) for k in range(N + 1)]

def planifier(L1, L2, depart, arrivee, N, angles_depart):
    if not segment_accessible(L1, L2, depart, arrivee):
        raise ValueError('Segment inaccessible')
    precedent = angles_depart
    configurations = []
    for x, y in points_segment(depart, arrivee, N):
        q = choisir_solution(cinematique_inverse(L1, L2, x, y), precedent)
        precedent = tuple((a + ecart_angle(a, b) for a, b in zip(precedent, q)))
        configurations.append(precedent)
    return configurations

MISSION = [{'cible': (60, 0), 'action': 'attente'}, {'cible': (50, 20), 'action': 'approche'}, {'cible': (50, 10), 'action': 'saisie'}, {'cible': (50, 30), 'action': 'degagement'}, {'cible': (20, 50), 'action': 'transfert'}, {'cible': (20, 30), 'action': 'depose'}, {'cible': (20, 50), 'action': 'degagement'}, {'cible': (60, 0), 'action': 'attente'}]

def preparer_mission(L1, L2, mission, N=20):
    if not mission or type(N) is not int or N <= 0:
        raise ValueError('Mission ou N invalide')
    depart = mission[0]['cible']
    q = cinematique_inverse(L1, L2, *depart)[0]
    etat = 'ouverte'
    images = [(*q, etat)]
    for etape in mission[1:]:
        arrivee = etape['cible']
        trajet = planifier(L1, L2, depart, arrivee, N, q)
        for i, q in enumerate(trajet[1:], 1):
            if i == N:
                if etape['action'] == 'saisie':
                    etat = 'fermee'
                elif etape['action'] == 'depose':
                    etat = 'ouverte'
            images.append((*q, etat))
        depart = arrivee
    return images

_preparer_mission = preparer_mission
MISSION = [dict(e, cible=tuple(v/100 for v in e['cible'])) for e in MISSION]
def preparer_mission():
    return _preparer_mission(.4,.3,MISSION,20)
