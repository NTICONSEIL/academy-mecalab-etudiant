# TP S2 — Commander le robot R2

Durée : 4 h. Lire [le cours](cours.md). Travailler dans une copie du dossier exercices. Exécuter chaque script avant de poursuivre. Toutes les longueurs sont en cm, les angles publics en degrés. Longueurs positives, distinctes ; entrées finies. Tolérance d'accessibilité 1e-10 cm, erreur de reconstruction < 1e-9 cm sur les références.

| Phase | Durée |
|---|---:|
| Réactivation S1 et cours | 45 min |
| EX01–03 | 40 min |
| Pause | 10 min |
| EX04–06 | 50 min |
| Pause | 10 min |
| EX07–08 | 40 min |
| EX09–10 (bonus) | 30 min |
| Bilan | 15 min |

## EX01 — Accessibilité (10 min)
Compléter `est_accessible`. Contrôler les longueurs et les valeurs finies ; lever ValueError si invalides. Utiliser hypot et les deux bornes inclusives avec tolérance. Tester (40,30), (70,0), (10,0), (80,0), (3,4), (0,0) : True, True, True, False, False, False. Tester une longueur nulle et NaN.

## EX02 — Trigonométrie inverse (15 min)
Compléter `orientation`. Afficher acos(0.5) en degrés. Comparer atan(y/x) et atan2(y,x) sur les quatre quadrants et axes ; traiter x=0 et refuser l'origine. Pour (1,1), (-1,1), (-1,-1), (1,-1), attendre 45,135,-135,-45°. Sur (0,1), attendre 90°.

## EX03 — Coude (15 min)
Compléter `angles_coude` en réutilisant EX01. Refuser les cibles inaccessibles, calculer c par Al-Kashi, borner c puis renvoyer les deux angles en degrés (positif puis négatif). Pour (40,30) : ±90° ; (70,0) : 0° ; (10,0) : ±180°. La déduplication sera faite en EX05.

## EX04 — Épaule (15 min)
Compléter `angle_epaule` avec la formule du cours. Convertir theta2 en radians. Pour (40,30), attendre 0° avec +90° et 73.739795° avec -90°. Réutiliser EX03 dans la démonstration.

## EX05 — Modèle inverse (20 min)
Assembler EX03 et EX04. Normaliser les angles dans [-180,180[. Retourner une liste de tuples ; éliminer les doublons aux frontières (comparaison angulaire avec tolérance 1e-7 degré). Pour (40,30), deux solutions ; (70,0) et (10,0), une seule ; (80,0), ValueError. Ne pas arrondir les angles calculés.

## EX06 — Validation (15 min)
Le modèle direct de S1 est fourni. Compléter `erreur_reconstruction` puis tester chaque solution pour les cibles du script. Vérifier l'erreur < 1e-9 cm et le nombre attendu de postures. Vérifier que les cibles impossibles lèvent ValueError. Expliquer pourquoi on ne compare pas les angles avec ==.

## EX07 — Visualisation (20 min)
Compléter `afficher_solutions`. Tracer les deux bras O,A,P pour (40,30), avec couleurs distinctes, cible, légende, grille et axes de même échelle. Ajouter les cercles de rayons 10 et 70. Tester aussi (70,0). Comparer avec le schéma du cours.

## EX08 — Sélection (20 min)
Compléter `ecart_angle`, `cout` et `choisir_solution`. Utiliser le modulo pour les écarts signés. Vérifier ecart_angle(179,-179)=2. Pour (40,30), depuis (0,80) choisir (0,90) ; depuis (70,-80) choisir environ (73.74,-90). En cas d'égalité garder la première solution. Expliquer la limite du coût.

## EX09 — Trajectoire cartésienne (15 min, bonus)
Compléter `segment_accessible`, `points_segment` et `planifier`. Utiliser la formule du minimum de distance du cours ; traiter le segment nul. Refuser tout segment inaccessible avant de calculer les angles. N entier strictement positif. Pour (70,0) vers (30,40), N=20 : 21 points, milieu (50,20). Sélectionner la posture la plus proche de la précédente, puis déplier les angles via les écarts minimaux. Vérifier les reconstructions. Refuser (-40,0) vers (40,0), même avec N=1. Tracer la trajectoire et comparer à S1.

## EX10 — Pick & Place (15 min, bonus)
Compléter `preparer_mission` et `animer`. Utiliser les huit étapes fournies. Initialiser à la première cible, pince ouverte ; planifier chaque segment avant toute animation. Ne pas dupliquer le point de jonction ; changer l'état de la pince seulement à l'arrivée aux étapes saisie et dépose. Retourner des images sous forme de tuples (theta1,theta2,etat). Animer avec plt.pause, afficher l'état et la position. Tester le retour à (60,0), pince ouverte. Refuser une mission contenant un segment impossible.

## Restitution
Remettre les scripts complétés et une courte conclusion : deux solutions, frontières, erreur numérique, intérêt de la commande cartésienne. Barème indicatif /20 : EX01–03 6 pts, EX04–05 5 pts, EX06 3 pts, EX07 3 pts, EX08 3 pts. EX09–10 bonus +2. Les deux derniers exercices peuvent nécessiter du temps supplémentaire selon le niveau du groupe.
