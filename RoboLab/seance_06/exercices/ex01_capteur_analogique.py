"""EX01 — Convertir les codes en degrés ; refuser plage nulle et extrapolation."""
from support_serie import lire_csv
from support_simulation import simuler
from support_s5 import quintique
import math

def convertir_position(valeur_adc, adc_min, adc_max, angle_min, angle_max):
    # TODO : Convertir les codes en degrés ; refuser plage nulle et extrapolation.
    raise NotImplementedError

if __name__ == "__main__":
    mesures = lire_csv('etalonnage.csv')
    print("Données SYNTHÉTIQUES :", len(mesures), "lignes")
    print(mesures[0])
    # TODO : appeler les fonctions, vérifier les résultats et tracer les courbes.
