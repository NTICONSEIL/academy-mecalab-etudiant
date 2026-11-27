"""EX07 — Estimer K et tau par grille puis valider sur PWM 150 ; commande normalisée."""
from support_serie import lire_csv
from support_simulation import simuler
from support_s5 import quintique
import math

def modele_premier_ordre(t, K, tau, commande):
    # TODO : Estimer K et tau par grille puis valider sur PWM 150 ; commande normalisée.
    raise NotImplementedError

def identifier_parametres(temps, vitesses, commande):
    # TODO : Estimer K et tau par grille puis valider sur PWM 150 ; commande normalisée.
    raise NotImplementedError

if __name__ == "__main__":
    mesures = lire_csv('reponse_pwm_100.csv')
    print("Données SYNTHÉTIQUES :", len(mesures), "lignes")
    print(mesures[0])
    # TODO : appeler les fonctions, vérifier les résultats et tracer les courbes.
