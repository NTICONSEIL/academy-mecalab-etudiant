# RoboLab — Python appliqué à la robotique

**MecaLab · Cycle préparatoire · Première année**

RoboLab est un parcours pédagogique consacré à la modélisation, à la simulation et à la commande d'un bras robotique. Il prolonge les acquis de Python du projet BatiCalc en mobilisant les mathématiques, la mécanique et les sciences de l'ingénieur.

## 1. Contexte industriel

Le bureau d'études fictif **RoboTech Industries** développe le robot R2 pour déplacer des pièces entre deux postes de production (mission Pick & Place). Les étudiants construisent progressivement un simulateur permettant de répondre à quatre questions : où se trouve le bras, comment atteindre une cible, quelle charge peut-il supporter et à quelle vitesse peut-il la déplacer ?

## 2. Progression pédagogique

Quatre séances de 4 h sont préparées, soit **16 heures, 40 exercices (32 obligatoires et 8 approfondissements)**. Deux séances supplémentaires constituent la feuille de route.

| Séance | Thématique | Problématique | État des supports |
|---|---|---|---|
| S1 | Cinématique directe | Où se trouve l'extrémité du bras ? | Prêts |
| S2 | Cinématique inverse | Quels angles permettent d'atteindre une cible ? | Prêts |
| S3 | Statique et dimensionnement | Les moteurs peuvent-ils supporter la charge ? | Prêts |
| S4 | Dynamique et puissance | À quelle vitesse déplacer la pièce ? | Prêts |
| S5 | Commande et asservissement | Comment corriger les erreurs de suivi ? | Prévu |
| S6 | Expérimentation physique | Comment piloter un système réel ? | Prévu |

### Séance 1 — Cinématique directe (4 h)

Trigonométrie, conversion degrés/radians, coordonnées des articulations, espace de travail, visualisation et animation du bras. Validation des résultats par des cas géométriques simples.

[Présentation](seance_01/README.md) · [Cours](seance_01/cours.md) · [TP](seance_01/tp.md) · [Exercices](seance_01/exercices/) · [Ressources](seance_01/ressources/)

### Séance 2 — Cinématique inverse (4 h)

Accessibilité des cibles, calcul des solutions articulaires, choix de posture, planification et simulation d'une mission Pick & Place. Vérification par cinématique directe.

[Présentation](seance_02/README.md) · [Cours](seance_02/cours.md) · [TP](seance_02/tp.md) · [Exercices](seance_02/exercices/)

### Séance 3 — Statique et dimensionnement (4 h)

Forces, poids, moments signés, isolement des systèmes, centres de gravité, couples de maintien, coefficient de sécurité, cartographie des contraintes, charge utile maximale et validation statique de la mission.

[Présentation](seance_03/README.md) · [Cours](seance_03/cours.md) · [TP](seance_03/tp.md) · [Exercices](seance_03/exercices/) · [Schémas](seance_03/ressources/)

### Séance 4 — Dynamique et puissance (4 h)

Différences finies, lois de mouvement cubique et quintique, vitesse, accélération, moments d'inertie, théorème de Huygens-Steiner, couples dynamiques, puissance et travail mécanique, intégration par trapèzes et optimisation sous contraintes. En approfondissement : modèle dynamique couplé et simulation de la mission complète.

[Présentation](seance_04/README.md) · [Cours](seance_04/cours.md) · [TP](seance_04/tp.md) · [Exercices](seance_04/exercices/) · [Schémas](seance_04/ressources/)

### Perspectives

- S5 : boucle ouverte et fermée, équations différentielles, méthode d'Euler, correcteurs P, PI et PID, stabilité et suivi de consigne.
- S6 : expérimentation Python-Arduino, sous réserve de matériel et d'un encadrement adapté.

## 3. Robot de référence R2

Bras plan à deux articulations rotatives (épaule et coude). Le second angle est relatif au premier segment. Les paramètres suivants sont des hypothèses pédagogiques, non des spécifications constructeur.

| Paramètre | Valeur |
|---|---:|
| Longueurs L1 / L2 | 0,40 / 0,30 m |
| Masses des segments | 1,20 / 0,80 kg |
| Masse de la pince | 0,20 kg |
| Charge nominale étudiée | 0,50 kg |
| Pesanteur | 9,81 m/s² |
| Couples nominaux épaule / coude | 20 / 8 N·m |
| Coefficient de sécurité sur les couples | 1,5 |
| Vitesses maximales | 2 / 3 rad/s |
| Accélérations maximales | 5 / 8 rad/s² |
| Puissances mécaniques maximales | 40 / 24 W |

Les premières séances utilisent notamment les centimètres et les degrés. Les calculs mécaniques utilisent les unités SI ; en S4, les vitesses et accélérations angulaires sont exprimées en radians. Respecter les conventions des modules de support, qui utilisent des degrés pour certaines fonctions.

## 4. Compétences développées

| Domaine | Compétences |
|---|---|
| Python | Variables, conditions, boucles, listes, fonctions, modules, assertions |
| Mathématiques | Trigonométrie, vecteurs, dérivation, intégration numérique, matrices |
| Mécanique | Cinématique, équilibre, moments, inertie, dynamique, énergie |
| Simulation | Séries temporelles, visualisation Matplotlib, cartographie |
| Ingénierie | Validation analytique, dimensionnement, optimisation et analyse des limites |

## 5. Organisation du dépôt

```text
MecaLab-CESI-Python/
├── README.md
├── requirements.txt
└── RoboLab/
    ├── README.md
    ├── seance_01/
    ├── seance_02/
    ├── seance_03/
    └── seance_04/
```

Chaque séance contient un README, un cours, un TP et dix scripts de départ dans `exercices/`. Des ressources graphiques et des modules de support fonctionnels complètent les séances selon les besoins. Les corrigés Python et notebooks Jupyter sont réservés à l'enseignant et conservés séparément.

## 6. Installation et mise à jour

Python 3.10 ou supérieur recommandé, Git, VS Code avec extension Python et Matplotlib.

```bash
git clone URL_DU_DEPOT
cd MecaLab-CESI-Python
git switch robolab
python -m pip install -r requirements.txt
code .
```

Remplacer `URL_DU_DEPOT` par l'adresse communiquée par l'enseignant. Sous Windows, `py` peut remplacer `python`. Si la commande `code` n'est pas disponible, ouvrir le dossier dans VS Code manuellement.

Pour récupérer les nouveaux supports :

```bash
git switch robolab
git pull
```

## 7. Méthode de travail

1. Lire le cours puis le TP de la séance.
2. Copier le dossier `exercices` complet dans `mon_travail/seance_XX` pour préserver les imports locaux.
3. Compléter les TODO dans l'ordre ; conserver les signatures et les assertions.
4. Exécuter les scripts depuis leur dossier. Exemple en S4 : `python ex01_vitesse_acceleration.py`.
5. Comparer les résultats aux références du TP et expliquer les écarts.
6. Conserver les programmes, graphiques et conclusions demandés.

Les exercices 1 à 8 forment le socle obligatoire ; les exercices 9 et 10 sont des approfondissements. Les scripts de départ sont volontairement incomplets. Les modules de support fournis ne nécessitent pas de correction.

## 8. Démarche scientifique et limites

Un programme qui s'exécute n'est pas nécessairement un modèle valide. Chaque résultat doit être contrôlé par les unités, des cas particuliers, des tests numériques et, lorsque possible, un calcul analytique indépendant.

Les modèles supposent notamment des segments rigides, des articulations idéales et l'absence de frottements. La validation dynamique repose sur un échantillonnage temporel et des limites pédagogiques indépendantes de couple, vitesse et puissance. Elle ne tient pas compte des collisions, des contraintes thermiques ni des courbes constructeur. L'interpolation articulaire ne garantit pas une trajectoire cartésienne rectiligne. Le travail mécanique n'est pas la consommation électrique. Les résultats ne constituent pas une certification ni une autorisation de commande d'un robot réel.

---

**RoboLab — Comprendre, modéliser, programmer, simuler et vérifier.**
