"""EX05 — Filtres causaux, initialisation par première mesure, comparer dispersion et retard."""
from support_serie import lire_csv
from support_simulation import simuler
from support_s5 import quintique
import math

def moyenne_glissante(valeurs, taille_fenetre):
    # TODO : Filtres causaux, initialisation par première mesure, comparer dispersion et retard.
    raise NotImplementedError

def filtre_exponentiel(valeurs, alpha):
    # TODO : Filtres causaux, initialisation par première mesure, comparer dispersion et retard.
    raise NotImplementedError

if __name__ == "__main__":
    mesures = lire_csv('bruit_capteur.csv')
    print("Données SYNTHÉTIQUES :", len(mesures), "lignes")
    print(mesures[0])
    # TODO : appeler les fonctions, vérifier les résultats et tracer les courbes.
