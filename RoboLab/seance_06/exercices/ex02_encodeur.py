"""EX02 — Convertir le comptage signé en radians ; vérifier un tour."""
from support_serie import lire_csv
from support_simulation import simuler
from support_s5 import quintique
import math

def position_encodeur(comptage, comptages_par_tour):
    # TODO : Convertir le comptage signé en radians ; vérifier un tour.
    raise NotImplementedError

if __name__ == "__main__":
    mesures = lire_csv('bruit_capteur.csv')
    print("Données SYNTHÉTIQUES :", len(mesures), "lignes")
    print(mesures[0])
    # TODO : appeler les fonctions, vérifier les résultats et tracer les courbes.
