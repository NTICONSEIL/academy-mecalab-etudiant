# MecaLab — Python appliqué aux sciences de l’ingénieur

**Cycle préparatoire · Première année**

MecaLab est un projet pédagogique consacré à l’application de la programmation Python à la mécanique, à la robotique et à la mécatronique. Il place les étudiants face à des problèmes de modélisation, de simulation et de commande de systèmes physiques.

Le projet s’articule autour de deux parcours complémentaires : **RoboLab**, consacré aux bras robotiques, et **DroneLab**, consacré à la dynamique et au pilotage simulé de drones quadricoptères.

## Objectifs pédagogiques

- Traduire un problème physique en modèle mathématique puis en algorithme.
- Consolider les fondamentaux Python : variables, conditions, boucles, listes et fonctions.
- Manipuler les unités, les coordonnées, les vecteurs et les angles.
- Représenter graphiquement des systèmes mécaniques et leurs trajectoires.
- Vérifier les résultats numériques à l’aide de calculs analytiques et de tests.
- Découvrir progressivement la simulation temporelle, la commande et l’asservissement.
- Identifier les hypothèses et les limites d’un modèle physique.

## Les deux parcours

### RoboLab — Robotique et manipulation

Le bureau d’études fictif RoboTech Industries souhaite modéliser un bras robotique destiné au déplacement de pièces entre deux postes de production. Les étudiants développent progressivement un simulateur permettant de déterminer les positions accessibles et de préparer les mouvements du bras.

Le premier système étudié, **RoboLab R2**, est un bras plan à deux articulations rotatives, constitué de segments de 40 cm et 30 cm.

| Étape | Thématique | État |
|---|---|---|
| 1 | Trigonométrie, cinématique directe, validation et visualisation | Disponible |
| 2 | Cinématique inverse et choix des configurations articulaires | Prévu |
| 3 | Forces, moments et couples moteurs | Prévu |
| 4 | Vitesses, accélérations et génération de trajectoires | Prévu |
| 5 | Commande, contraintes et mission Pick & Place simulée | Prévu |

**[Accéder à RoboLab — séance 1 (4 h)](RoboLab/seance_01/README.md)** · [Cours](RoboLab/seance_01/cours.md) · [TP](RoboLab/seance_01/tp.md) · [Scripts de départ](RoboLab/seance_01/exercices/)

### DroneLab — Dynamique et pilotage

DroneLab propose d’étudier le comportement d’un drone quadricoptère par la programmation et la simulation. Le parcours commencera par un modèle vertical simplifié, avant d’introduire les déplacements, l’orientation et la régulation.

| Étape | Thématique | État |
|---|---|---|
| 1 | Masse, poids, poussée et équilibre | Prévu |
| 2 | Décollage et dynamique verticale | Prévu |
| 3 | Simulation temporelle et intégration numérique | Prévu |
| 4 | Énergie, puissance et autonomie | Prévu |
| 5 | Déplacements, orientation et trajectoires | Prévu |
| 6 | Régulation d’altitude et mission autonome simulée | Prévu |

**[Accéder à DroneLab](DroneLab/README.md)** — parcours en préparation.

## Une démarche scientifique commune

Pour chaque exercice :

1. Comprendre le problème et identifier les grandeurs physiques.
2. Définir le modèle, les hypothèses et les unités.
3. Établir les relations mathématiques.
4. Implémenter l’algorithme en Python.
5. Tester les résultats et les comparer aux valeurs de référence.
6. Interpréter les résultats et discuter les limites du modèle.

La réussite d’un exercice ne se limite pas à obtenir un programme qui s’exécute : les résultats doivent être justifiés, vérifiés et interprétés.

## Organisation du dépôt

```text
MecaLab-CESI-Python/
├── README.md
├── requirements.txt
├── .gitignore
├── RoboLab/
│   └── seance_01/
│       ├── README.md
│       ├── cours.md
│       ├── tp.md
│       ├── exercices/
│       └── ressources/
└── DroneLab/
    └── README.md
```

Les parcours sont organisés en répertoires dans le dépôt. Chaque séance contient un cours, un TP et, selon les besoins, des scripts de départ et des ressources. Les corrigés enseignants sont conservés séparément.

## Prérequis et installation

- Python 3.10 ou supérieur recommandé.
- Visual Studio Code avec l’extension Python.
- Git pour récupérer les supports.
- Notions élémentaires d’algorithmique et de trigonométrie.

Cloner le dépôt en remplaçant `URL_DU_DEPOT` par l’adresse communiquée par l’enseignant :

```bash
git clone URL_DU_DEPOT
cd MecaLab-CESI-Python
python --version
python -m pip install -r requirements.txt
code .
```

Sous Windows, `py` peut remplacer `python`. Sélectionner dans VS Code le même interpréteur que celui utilisé pour installer les dépendances. La commande `code .` suppose que VS Code est accessible depuis le terminal ; sinon, ouvrir le dossier depuis son interface.

La seule bibliothèque externe requise pour la première séance est **Matplotlib**. Le module `math` appartient à la bibliothèque standard de Python. NumPy pourra être introduit ultérieurement.

## Méthode de travail étudiant

1. Lire le cours et les consignes du TP.
2. Copier le dossier `exercices` de la séance dans un dossier personnel `mon_travail` à la racine du dépôt, en conservant les scripts ensemble.
3. Compléter les sections `TODO` et exécuter les scripts depuis le dossier de travail.
4. Vérifier les résultats à partir des cas de test proposés.
5. Conserver les programmes et les conclusions demandées par l’enseignant.

Le dossier `mon_travail` est ignoré par Git. Pour récupérer les nouveaux supports, exécuter depuis la racine du dépôt :

```bash
git pull
```

## État et périmètre du projet

RoboLab — séance 1 est disponible : dix exercices progressifs, dont huit obligatoires et deux facultatifs, pour une séance de quatre heures. Les autres étapes de RoboLab et le parcours DroneLab constituent la feuille de route pédagogique ; leurs supports seront ajoutés progressivement.

Les modèles proposés sont des simulations pédagogiques simplifiées. Ils ne constituent ni des logiciels de commande validés pour des équipements réels, ni des outils de certification ou de dimensionnement industriel. Une éventuelle expérimentation matérielle nécessitera un encadrement et des dispositifs de sécurité adaptés.

---

**MecaLab — Comprendre la physique, modéliser les systèmes, programmer et vérifier.**
