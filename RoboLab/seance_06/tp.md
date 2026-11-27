# TP — Du capteur au modèle

Banc préassemblé et validé par enseignant. Mode synthétique par défaut. Ne jamais envoyer START sans validation matérielle.

Planning : introduction 20 min ; EX01–03 40 min ; cours 15 min ; EX04–05 30 min ; pause 10 min ; moteur 20 min ; EX06–07 40 min ; pause 10 min ; PID 15 min ; EX08 25 min ; démonstration 10 min ; bilan 5 min.

## EX01 — capteur analogique

Fichier : `exercices/ex01_capteur_analogique.py`. Données : `etalonnage.csv`.

Convertir les codes en degrés ; refuser plage nulle et extrapolation.

Contrôles : 100→0°, 900→180°, 500→90° avec cet étalonnage. En réel relever au moins cinq positions connues et discuter les résidus.

## EX02 — encodeur

Fichier : `exercices/ex02_encodeur.py`. Données : `bruit_capteur.csv`.

Convertir le comptage signé en radians ; vérifier un tour.

Contrôles : C=2400, n=600→π/2, n=−2400→−2π. En réel mesurer C sur plusieurs tours, vérifier le signe avant activation.

## EX03 — acquisition serie

Fichier : `exercices/ex03_acquisition_serie.py`. Données : `reponse_pwm_60.csv`.

Valider 7 champs, nombres finis, PWM et timestamps ; écrire CSV.

Contrôles : rejeter ligne tronquée, NaN et PWM 256 ; calculer médiane des intervalles, nombre de trous >1,5 fois la médiane. En réel utiliser les sketches 01/02 passifs ou acquisition supervisée 03/04.

## EX04 — vitesse bruit

Fichier : `exercices/ex04_vitesse_bruit.py`. Données : `bruit_capteur.csv`.

Dérivée arrière (N−1 points), temps strictement croissants ; moyenne et écart-type échantillon.

Contrôle : [0,0.1,0.3] rad aux temps [0,.1,.2] s donne [1,2] rad/s. Comparer écart-type de position et vitesse, unités distinctes.

## EX05 — filtrage

Fichier : `exercices/ex05_filtrage.py`. Données : `bruit_capteur.csv`.

Filtres causaux, initialisation par première mesure, comparer dispersion et retard.

Contrôle : [1,3,5], fenêtre 2 donne [1,2,4] ; alpha .5 donne [1,2,3.5]. Tester aussi un échelon synthétique pour le retard.

## EX06 — reponse indicielle

Fichier : `exercices/ex06_reponse_indicielle.py`. Données : `reponse_pwm_60.csv`.

Moyenne des derniers points ; tracer les trois échelons et vérifier le plateau.

Comparer PWM 60,100,150 (diviser par 255). En réel limiter les essais à la course et au plafond autorisés ; 150 est uniquement synthétique avec le firmware fourni. Si plateau inaccessible, ne pas identifier par cette méthode.

## EX07 — identification

Fichier : `exercices/ex07_identification.py`. Données : `reponse_pwm_100.csv`.

Estimer K et tau par grille puis valider sur PWM 150 ; commande normalisée.

Grille K=4..12 par .25, tau=.10.. .50 par .01 ; comparer RMSE et méthode 63,2 %. Identifier sur 60 et 100 séparément puis discuter leur cohérence ; valider sur 150 sans réajuster.

## EX08 — asservissement

Fichier : `exercices/ex08_asservissement.py`. Données : `reponse_pid.csv`.

Calculer erreur finale, dépassement, temps à 5 %, RMS et IAE ; comparer P PI PID.

Consigne .5 rad, départ 0. Bande ±.025 rad ; si jamais stabilisé retourner None. Comparer les trois CSV. En réel gains validés par enseignant, commencer P faible, puis D et I ; aucun gain synthétique à recopier directement.

## EX09 — robustesse

Fichier : `exercices/ex09_robustesse.py`. Données : `reponse_pid.csv`.

Simuler charges relatives 1, 1.5, 2 avec gains identiques ; comparer RMS.

Utiliser support_simulation.simuler(mode="PID", charge=...). En réel modifier la masse uniquement hors tension, vérifier fixation et limites. Discuter la différence entre inertie et couple résistant.

## EX10 — jumeau numerique

Fichier : `exercices/ex10_jumeau_numerique.py`. Données : `reponse_pid.csv`.

Comparer séries synchronisées, RMS suivi et RMS modèle ; utiliser quintique et simulation.

Générer deux simulations trajectoire=True, charge=1 et 1.5 ; la seconde est un substitut synthétique de mesure, jamais une mesure réelle. En réel le firmware fourni accepte uniquement des consignes fixes : suivi quintique physique hors périmètre, à développer après validation du banc.

## Évaluation /20
Capteurs 3, acquisition 3, échantillonnage 2, filtrage 3, identification 4, asservissement 3, interprétation 2. Bonus EX09 +1, EX10 +2.
