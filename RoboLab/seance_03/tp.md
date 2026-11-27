# TP — Dimensionnement statique du R2

Durée 4 h, exercices 1–8 obligatoires, 9–10 bonus. Lire le cours avant chaque partie. Exécuter les fichiers depuis `exercices/` dans l'ordre. Toutes les longueurs sont en mètres, angles en degrés, couples en N·m. Compléter les TODO, conserver les signatures et les tests. Rendre les scripts et les graphiques, accompagnés de réponses aux questions d'interprétation.

## EX01 — Poids (10 min, 2 points)
Compléter `calculer_poids(masse,g=9.81)` : refuser masse négative, g non positif et valeurs non finies. Parcourir la liste de dictionnaires fournie, afficher les poids individuels et le total 26,487 N. Expliquer la différence entre kg et N.

## EX02 — Moment (15 min, 2 points)
Compléter `moment_force(x,y,Fx,Fy)` puis `moment_poids(masse,longueur,angle)` en réutilisant EX01. Tester une force horizontale appliquée en (0,2), Fx=3 N : moment -6 N·m. Pour 1 kg à 0,4 m, retrouver -3,924 ; -3,39828 environ ; -1,962 ; 0 ; +3,924 N·m aux angles 0,30,60,90,180°. Expliquer les signes.

## EX03 — Influence de l'angle (15 min, 2 points)
Échantillonner 0 à 360° inclus par pas de 5°, tracer le moment en fonction de l'angle avec axes et unités. Relever extrema et angles de moment nul (tolérance 1e-9). Expliquer pourquoi le poids ne change pas mais le moment varie.

## EX04 — Centres de gravité (10 min, 3 points)
Compléter `position_robot` (retour xA,yA,xP,yP) et `centres_gravite` (retour xG1,yG1,xG2,yG2). Pour (0°,0°), G1=(0,2;0), G2=(0,55;0). Pour (90°,-90°), G1=(0;0,2), G2=(0,15;0,4). Justifier la formule du milieu.

## EX05 — Couples moteurs (20 min, 4 points)
Compléter `calculer_couples(robot,theta1,theta2,charge)` en utilisant les positions et les moments. Retourner les deux couples signés de compensation. Refuser les charges négatives ou non finies. À (0°,0°), charge 0,5 kg : C1=11,4777 et C2=3,2373. Compléter `sollicitations` (retour u1,u2 sous forme de fractions) et `admissible` (booléen). Pourquoi C2 ne contient-il pas le poids du segment 1 ?

## EX06 — Validation (15 min, 2 points)
Automatiser les cinq cas fournis avec `math.isclose` (tolérance absolue 1e-9, relative nulle). Ajouter un test de périodicité et un test de charge négative. Afficher le nombre de tests réussis. Expliquer pourquoi les couples peuvent être nuls à la verticale.

## EX07 — Cartographie (25 min, 2 points)
Construire deux matrices de 72 lignes × 72 colonnes avec θ1 en ligne, θ2 en colonne, angles -180 à 175° par pas de 5°. Calculer les taux u1,u2 pour une charge de 1 kg. Compter les configurations satisfaisant simultanément les deux limites. Tracer deux cartes `imshow` avec origine basse, axes en degrés et barres de couleur. Relever les maxima et les comparer au cas horizontal. Refaire pour 0,5 kg : toutes les configurations doivent être admissibles. Ne pas confondre taux d'admissibilité de la grille et surface cartésienne.

## EX08 — Charge maximale (20 min, 3 points)
Calculer les deux bornes analytiques à l'horizontale, puis leur minimum. Si une borne est négative, signaler que le robot est déjà non admissible à vide. Rechercher numériquement la dernière masse admissible de 0 à 5 kg par pas de 0,001 kg (signaler si la borne de recherche est atteinte). Résultats : 0,770224746 kg et 1,212209763 kg ; recherche : 0,770 kg. Justifier la garantie globale avec les bornes des cosinus.

## EX09 — Mission Pick & Place (15 min, bonus 1)
Le module `support_s2.py` fournit la mission et ses 141 configurations `(theta1,theta2,etat)`. Compléter `analyser_mission` : retourner une liste de dictionnaires contenant indice, charge, C1, C2, u1, u2. La pièce de 0,5 kg est portée aux indices 40–99 ; contrôler également l'indice 100 juste avant dépose. Tracer les couples signés et les limites ±Cnom/S ; identifier le maximum absolu de chaque moteur et vérifier tous les taux. Refaire avec 1 kg. Ne pas conclure à la faisabilité dynamique.

## EX10 — Optimisation (15 min, bonus 1)
Pour une cible en mètres, obtenir les solutions de `cinematique_inverse` du module fourni. Calculer J=max(u1,u2) pour chaque solution et sélectionner celle de J minimal (première en cas d'égalité). Retourner la posture et son coût ; signaler si J>1. Tester (0,4;0,3), charge 0,5 kg, puis une cible inaccessible (0,8;0). Comparer avec le critère angulaire de S2. Pourquoi ce choix local ne suffit-il pas à planifier une mission ?

## Bilan (10 min)
Barème : 20 points + 2 bonus. Présenter les deux cartes, la charge maximale et les limites du modèle. Aucun matériel réel n'est commandé.
