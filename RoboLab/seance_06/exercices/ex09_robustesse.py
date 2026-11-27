"""EX09 — Simuler charges relatives 1, 1.5, 2 avec gains identiques ; comparer RMS."""
from support_serie import lire_csv
from support_simulation import simuler
from support_s5 import quintique
import math

def comparer_charges(gains, charges):
    # TODO : Simuler charges relatives 1, 1.5, 2 avec gains identiques ; comparer RMS.
    raise NotImplementedError

if __name__ == "__main__":
    mesures = lire_csv('reponse_pid.csv')
    print("Données SYNTHÉTIQUES :", len(mesures), "lignes")
    print(mesures[0])
    # TODO : appeler les fonctions, vérifier les résultats et tracer les courbes.
