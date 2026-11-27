"""EX04 — Dérivée arrière (N−1 points), temps strictement croissants ; moyenne et écart-type échantillon."""
from support_serie import lire_csv
from support_simulation import simuler
from support_s5 import quintique
import math

def calculer_vitesse(positions, temps):
    # TODO : Dérivée arrière (N−1 points), temps strictement croissants ; moyenne et écart-type échantillon.
    raise NotImplementedError

def statistiques_mesures(valeurs):
    # TODO : Dérivée arrière (N−1 points), temps strictement croissants ; moyenne et écart-type échantillon.
    raise NotImplementedError

if __name__ == "__main__":
    mesures = lire_csv('bruit_capteur.csv')
    print("Données SYNTHÉTIQUES :", len(mesures), "lignes")
    print(mesures[0])
    # TODO : appeler les fonctions, vérifier les résultats et tracer les courbes.
