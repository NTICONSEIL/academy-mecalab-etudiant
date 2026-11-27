"""EX06 — Moyenne des derniers points ; tracer les trois échelons et vérifier le plateau."""
from support_serie import lire_csv
from support_simulation import simuler
from support_s5 import quintique
import math

def estimer_regime_permanent(vitesses, proportion=0.2):
    # TODO : Moyenne des derniers points ; tracer les trois échelons et vérifier le plateau.
    raise NotImplementedError

if __name__ == "__main__":
    mesures = lire_csv('reponse_pwm_60.csv')
    print("Données SYNTHÉTIQUES :", len(mesures), "lignes")
    print(mesures[0])
    # TODO : appeler les fonctions, vérifier les résultats et tracer les courbes.
