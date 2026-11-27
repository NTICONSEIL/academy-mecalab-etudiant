"""EX08 — Calculer erreur finale, dépassement, temps à 5 %, RMS et IAE ; comparer P PI PID."""
from support_serie import lire_csv
from support_simulation import simuler
from support_s5 import quintique
import math

def calculer_performances(temps, positions, consigne):
    # TODO : Calculer erreur finale, dépassement, temps à 5 %, RMS et IAE ; comparer P PI PID.
    raise NotImplementedError

if __name__ == "__main__":
    mesures = lire_csv('reponse_pid.csv')
    print("Données SYNTHÉTIQUES :", len(mesures), "lignes")
    print(mesures[0])
    # TODO : appeler les fonctions, vérifier les résultats et tracer les courbes.
