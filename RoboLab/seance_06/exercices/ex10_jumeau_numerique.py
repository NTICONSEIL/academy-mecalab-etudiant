"""EX10 — Comparer séries synchronisées, RMS suivi et RMS modèle ; utiliser quintique et simulation."""
from support_serie import lire_csv
from support_simulation import simuler
from support_s5 import quintique
import math

def comparer_trajectoires(reference, simulation, mesures):
    # TODO : Comparer séries synchronisées, RMS suivi et RMS modèle ; utiliser quintique et simulation.
    raise NotImplementedError

if __name__ == "__main__":
    mesures = lire_csv('reponse_pid.csv')
    print("Données SYNTHÉTIQUES :", len(mesures), "lignes")
    print(mesures[0])
    # TODO : appeler les fonctions, vérifier les résultats et tracer les courbes.
