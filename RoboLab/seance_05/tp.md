# TP S5 — Asservissement du robot R2 (4 h)

## Organisation
15 min introduction, 25 min modèle, 40 min EX01–03, 10 min pause, 20 min P et performances, 45 min EX04–06, 10 min pause, 15 min PID, 35 min EX07–08, 20 min bonus/démonstration, 5 min bilan. Compléter les TODO sans modifier les tests. Pour chaque exercice fournir code, graphique si demandé, résultats et interprétation. Exécuter depuis `exercices/` avec `python ex01_premier_ordre.py` puis les suivants. Les supports sont fournis et ne doivent pas être modifiés.

## EX01 — Premier ordre (10 min)
Implémenter la solution exacte depuis le repos, refuser J ou b non positifs et t négatif. Tracer sur 0–6 s, U=1 N·m, J=.655, b=.8. Calculer tau, vitesse finale, vitesse à tau et temps à 5 %. Références : .81875 s, 1.25 rad/s, .79015 rad/s, environ 2.453 s. Expliquer la signification physique de b.

## EX02 — Euler (15 min)
Utiliser `grille(duree,dt)` et la récurrence du cours. Retourner deux listes de même longueur, état initial inclus. Sur 10 s, comparer les pas .01, .1, .5 et 2 s à la solution exacte aux mêmes instants. Calculer le maximum de l'erreur absolue. Tracer et expliquer pourquoi le dernier pas est instable. Vérifier la convergence en divisant le pas .1 par deux.

## EX03 — Boucle ouverte (15 min)
Retourner trois listes temps, position, vitesse. Euler explicite, conditions initiales fournies. Pour un départ au repos et U=1, tracer les deux états sur 10 s, comparer à la solution analytique de position. Refaire avec U=0 et une vitesse initiale non nulle. Pourquoi une commande constante ne maintient-elle pas une position cible ?

## EX04 — P (15 min)
Compléter la loi proportionnelle puis utiliser `simuler_articulation(loi, duree, dt, perturbation)` ; loi reçoit t,q,w,g,dt et retourne le couple correctif. Chaque ligne du résultat contient t,q,w,a,c,p,sature. Consigne pi/4, gains 2,5,10,20, horizon 15 s, pas .01. Tracer positions en degrés et couples en N·m. Comparer dépassement et rapidité. Modèle compensé idéal sans saturation pour EX04–07.

## EX05 — Performances (15 min)
Implémenter les trois fonctions du script pour un échelon positif depuis zéro. Vérifier consigne positive, listes non vides et longueurs compatibles. Temps de réponse : None si le dernier point est hors bande ; sinon retourner le premier instant suivant le dernier point hors bande (ou le premier instant si tous sont dedans). Appliquer aux quatre essais EX04. Comparer le dépassement mesuré à la formule théorique ; expliquer les différences dues au pas et à l'horizon.

## EX06 — Perturbation (15 min)
Implémenter d(t)=0 avant 5 s, -1 ensuite. Simuler les quatre gains pendant 30 s, dt=.01. Comparer erreur finale et erreur théorique 1/Kp (rad), convertir en degrés. Tracer une courbe avant/après perturbation. Pourquoi augmenter Kp n'est-il pas suffisant ?

## EX07 — PI (15 min)
Implémenter l'intégrale candidate puis la commande. Utiliser une fonction loi avec mémoire (closure `nonlocal` ou objet) pour appeler le support. Comparer P (Kp=5) et PI (Kp=5, Ki=2) sur 40 s avec perturbation EX06. Vérifier Routh avant simulation. Tracer erreur et intégrale. Expliquer pourquoi une intégrale trop forte peut déstabiliser le système.

## EX08 — PID et saturation (20 min)
Implémenter PID avec dérivée sur mesure, puis `creer_loi`. Chaque appel à creer_loi crée une intégrale indépendante. Le support passe g, compensation de gravité ; la loi retourne uniquement u. Anti-windup : tester g+u candidat contre ±20, bloquer l'intégration si l'erreur aggrave la saturation. Comparer P, PI, PD, PID avec Kp=8, Ki=2 (si actif), Kd=3 (si actif), consigne 45°, 20 s, dt=.005, perturbation EX06, `gravite=True, saturation=True`. Comparer avec/sans anti-windup pour Kp=30, Ki=10, Kd=3. Tracer position, erreur et couple total. Contrôler 1.5*max|c| <=20, max|w|<=2, max|a|<=5, max|p|<=40. Un correcteur stable peut violer ces contraintes.

## EX09 — Optimisation (bonus 15 min)
`evaluer` retourne au minimum `iae`, `admissible`, `maxima` (clés c,w,a,p). IAE par trapèzes, maxima absolus, limites EX08. Tester Kp dans (1,2,3,4), Ki dans (.1,.3,.5), Kd dans (1,2,3), consigne pi/4, durée 30 s, dt=.01, perturbation -0.2 N·m dès 5 s, gravité et saturation actives. Filtrer par Routh puis contraintes. Retenir le minimum IAE, départager par ordre lexicographique des gains ; retourner None si aucun candidat. Comparer au réglage (2,.3,2) et vérifier le gagnant à dt=.005. Ne pas présenter le minimum sur grille comme optimum global.

## EX10 — Mission asservie (bonus 20 min)
Utiliser `simuler_mission(loi,T=2,dt=.005,charge=.5,charge_reelle=.6)`. Les références sont en radians et les états réels ne sont pas réinitialisés. La loi reçoit ref (q,w,a,charge,segment,t), etat (q,w), dt. Pour anticipation, retourner `couples(ROBOT,ref['q'],ref['w'],ref['a'],ref['charge'])`. Pour PID, correction par axe avec erreur de position et vitesse de référence moins vitesse réelle ; pour combine, ajouter l'anticipation. Intégration conditionnelle par axe sur ±20 et ±8. Le support appelle aussi la loi aux fins de segment avec dt=0 pour contrôler les deux côtés des transitions. Comparer les trois modes, gains initiaux 12,2,4 pour les deux axes. Les gains ne sont pas garantis admissibles.

Le bilan utilise les lignes t,q,w,a (référence), mesure,vitesse,acceleration (réel), c,p,sature,xy,xy_ref. Calculer erreurs articulaires max et RMS par axe (degrés), erreur cartésienne max et RMS (mm), maxima absolus des couples/vitesses/accélérations/puissances, temps saturé et travaux positif/négatif par axe. Pour RMS temporel et énergie, intégrer par trapèzes sur chaque segment ; les instants dupliqués aux frontières ont un intervalle nul. Temps saturé : somme des intervalles dont le point gauche est saturé. Contrôler les limites S4 et comparer à dt=.0025. Tracer trajectoires XY et erreurs temporelles. Si le suivi est mauvais, expliquer pourquoi ; les actions de saisie/dépose sont programmées et ne prouvent pas la réussite physique. Proposer une amélioration.

## Évaluation /20
EX01–03 : modèle et Euler 8 points ; EX04–06 : P, performances et perturbations 8 points ; EX07–08 : PI/PID 4 points. Bonus EX09 +1, EX10 +2. Les tests fournis sont des tests de base, pas une preuve exhaustive. Les graphiques doivent porter unités, légende et titre.
