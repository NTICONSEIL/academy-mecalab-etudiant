# TP S4 — Dimensionnement dynamique de R2
Durée 4 h. Lire le cours par blocs. Exécuter chaque script après avoir complété les TODO ; conserver les signatures et les tests. Rendre les scripts, les figures et une courte analyse des résultats. Les angles sont en radians sauf dans les supports S2/S3.

| Temps | Activité |
|---|---|
| 0–15 min | Rappel S3 |
| 15–45 | Cours 1–3 |
| 45–85 | EX01–03 |
| 85–95 | Pause |
| 95–120 | Cours 4–6 |
| 120–165 | EX04–06 |
| 165–175 | Pause |
| 175–210 | EX07–08 |
| 210–230 | Bonus EX09–10 |
| 230–240 | Bilan |

## EX01 — Différences finies (10 min)
Calculer les vitesses entre les positions [0,0.04,0.16,0.36,0.64,1] espacées de 0,2 s, puis les accélérations. Rejeter dt non positif. Attendu : [0.2,0.6,1,1.4,1.8] rad/s et quatre accélérations de 2 rad/s². Expliquer le décalage temporel.

## EX02 — Profil cubique (15 min)
Implémenter les trois équations du cours. Valider T>0 et 0≤t≤T. Tester départ, milieu, arrivée, déplacement inverse et déplacement nul. Pour 90° en 2 s : milieu 45°, vitesse 1,178097 rad/s, accélération nulle ; accélérations extrêmes ±2,356194 rad/s².

## EX03 — Comparaison graphique (15 min)
Construire N+1 points pour T=1,2,4 s. Tracer position en degrés, vitesse et accélération en SI sur trois axes, en temps normalisé. Ajouter légendes et limites de l'épaule. Comparer les maxima et expliquer les facteurs 2 et 4. Exporter la figure.

## EX04 — Inerties élémentaires (10 min)
Implémenter les trois fonctions. Vérifier les valeurs du cours et rejeter masses, distances, inerties négatives. Expliquer pourquoi doubler la distance quadruple J.

## EX05 — Inertie équivalente (15 min)
Calculer J2 et J1(b) avec les distances au carré du cours. Tester b=0, pi/2, pi et charge nulle. Tracer J1 selon b en bonus. Expliquer pourquoi J2 est constant. Attendus nominaux : 0,087 ; 0,655 ; 0,391 ; 0,127 kg·m² respectivement pour J2 et J1 aux trois angles.

## EX06 — Couples dynamiques (20 min)
Simuler le mouvement de l'épaule 0→90° en 2 s, coude bloqué à 0. Utiliser N+1 instants et le support S3 (conversion en degrés). Calculer c1=G1+J1*a et c2=G2+M21*a. Afficher les maxima absolus et tracer les deux couples et les limites ±Cnom/1,5. Attendu initial : c1≈13,0210 N·m ; c2≈3,7533 N·m. Le coude immobile exerce un couple mais ne fournit pas de puissance mécanique.

## EX07 — Puissance et énergie (15 min)
Calculer P=c1*w ; P2=0. Intégrer P, max(P,0), min(P,0) par trapèzes. Tracer P et le travail cumulé (départ 0). Comparer le travail net à 11,4777 J pour N=200 puis 1000. Expliquer l'écart numérique et le signe de la puissance en fin de mouvement.

## EX08 — Durée admissible (20 min)
Contrôler les quatre limites de chaque axe sur tous les échantillons. Explorer les durées 0,50 à 5,00 s par pas de 0,01 s ; retourner None si aucune ne convient. Vérifier T=1 et T=2, puis la durée minimale sur la grille et celle juste avant. Refaire avec N=1000, puis une charge de 1 kg. Expliquer pourquoi ralentir ne suffit pas toujours. Le résultat n'est pas une certification continue.

## EX09 — Dynamique couplée (10 min, bonus)
Les coefficients, la matrice et les termes h,G sont fournis. Implémenter le produit matrice-vecteur et l'addition. Tester le retour à la statique, la symétrie de M et le cas d'une accélération de l'épaule seule. Comparer EX06. En approfondissement, tester une posture non alignée et des vitesses non nulles.

## EX10 — Mission (10 min pour démarrer, prolongement conseillé)
Les fonctions postures et mouvement sont fournies. Construire le bilan des sept déplacements. Utiliser la charge nulle avant la saisie, la charge nominale après saisie jusqu'à la dépose incluse, puis zéro. À chaque saisie/dépose contrôler G avant et après, à vitesse et accélération nulles. Pour chaque déplacement, contrôler aussi les deux extrémités du profil cubique avec leur accélération propre. Calculer les maxima par axe de |c|,|w|,|a|,|p|, les travaux positifs/négatifs par axe, la durée totale 7*T et un booléen admissible. Ne pas intégrer entre deux segments ou à travers un changement de masse. Comparer T=1,2,4 s pour 500 g et 1 kg. Expliquer la différence avec la trajectoire cartésienne S2 et les limites du modèle. Le bonus complet peut être terminé hors séance.

## Barème /20
EX01 3 ; EX02 3 ; EX03 2 ; EX04–05 3 ; EX06 4 ; EX07 2 ; EX08 3. Bonus EX09–10 +2. Évaluer aussi la justification physique et les tests, pas seulement les chiffres.
