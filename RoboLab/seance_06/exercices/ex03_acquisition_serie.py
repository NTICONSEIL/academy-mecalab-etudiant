"""EX03 — Valider 7 champs, nombres finis, PWM et timestamps ; écrire CSV."""
from support_serie import lire_csv
from support_simulation import simuler
from support_s5 import quintique
import math

def decoder_trame(ligne):
    # TODO : Valider 7 champs, nombres finis, PWM et timestamps ; écrire CSV.
    raise NotImplementedError

def enregistrer_mesures(mesures, fichier):
    # TODO : Valider 7 champs, nombres finis, PWM et timestamps ; écrire CSV.
    raise NotImplementedError

if __name__ == "__main__":
    mesures = lire_csv('reponse_pwm_60.csv')
    print("Données SYNTHÉTIQUES :", len(mesures), "lignes")
    print(mesures[0])
    # TODO : appeler les fonctions, vérifier les résultats et tracer les courbes.
