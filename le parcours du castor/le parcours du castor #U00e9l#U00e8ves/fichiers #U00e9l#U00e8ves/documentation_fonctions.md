# Documentation technique du projet

## Architecture du projet

Le projet est divisé en deux fichiers Python :

1. **`jeucastortravail.py`** : Logique du jeu (fonctions de validation, chemins, etc.)
2. **`interfacecastortravail.py`** : Interface graphique Tkinter

Cette séparation permet de tester les fonctions de logique indépendamment de l'interface.

---

## Fichier `interfacecastortravail.py`

### Variables globales

| Variable | Type | Description |
|----------|------|-------------|
| `SCRIPT_DIR` | str | Chemin absolu du dossier contenant le script (pour charger les images) |
| `fenetre` | Tk | Fenêtre principale de l'application |
| `maPolice1` | Font | Police Arial 18 gras pour les boutons |
| `photoF`, `photoB`, `photoP` | PhotoImage | Images des cases (feuille, bois, pierre) |
| `tableauBoutons` | list | Tableau 2D contenant tous les boutons de la grille |
| `reponse` | StringVar | Variable Tkinter pour afficher "Bravo" ou "Perdu" |
| `commentaire` | Label | Label qui affiche le contenu de `reponse` |
| `validationSaisie` | Button | Bouton "Parcours terminé" |

### Gestion des chemins d'images

Pour éviter les problèmes de chemins relatifs, on utilise :

```python
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
photoF = PhotoImage(file=os.path.join(SCRIPT_DIR, "feuille.png"))
```

Cela garantit que les images seront trouvées quelle que soit la façon dont le script est lancé.

---

### Fonctions fournies

#### `initialise(grilleinit=grille_1)`

**But** : Crée l'affichage initial de la grille avec les boutons cliquables.

**Fonctionnement** :
1. Calcule les dimensions L×C de la grille
2. Crée un tableau 2D `tableauBoutons` rempli de 0
3. Pour chaque case `[x, y]` de la grille :
   - Lit le type de case dans `grilleinit[x][y]` (P, B ou F)
   - Crée un `Button` avec l'image correspondante
   - Configure le bouton pour appeler `clic()` avec les bons paramètres
   - Stocke le bouton dans `tableauBoutons[x][y]`
   - Place le bouton sur la grille avec `.grid(row=x, column=y)`

**Note sur les lambda** :
```python
lambda b=bouton, absc=x, ordon=y: clic(grillecourante, b, absc, ordon, "P")
```
Les paramètres `b=bouton`, `absc=x`, `ordon=y` sont nécessaires pour "capturer" les valeurs au moment de la création du bouton. Sans ça, tous les boutons auraient les mêmes valeurs finales de `x` et `y`.

---

#### `clic(g, btn, ligne, colon, typecase)`

**But** : Gère le clic sur une case de la grille.

**Fonctionnement** :
1. Désactive le bouton cliqué : `btn["state"] = DISABLED`
2. Ajoute les coordonnées à la liste globale `chemin` : `chemin.append([ligne, colon])`

**Paramètres** :
- `g` : la grille (non utilisé ici)
- `btn` : le bouton Tkinter qui a été cliqué
- `ligne`, `colon` : coordonnées de la case
- `typecase` : type de la case ("P", "B" ou "F")

---

#### `lanceAide(grille)`

**But** : Lance la recherche automatique d'un chemin valide et l'affiche.

**Fonctionnement** :
1. Appelle `chercheChemin(grille)` pour trouver un chemin
2. Vérifie si un chemin a été trouvé (non vide et se termine en `[0,0]`)
3. Si oui :
   - Désactive tous les boutons du chemin
   - Appelle `verification()` pour afficher le résultat
4. Sinon : affiche "Pas de solution trouvée !"

**Utilité** : Cette fonction vous montre comment utiliser le résultat d'une fonction de recherche de chemin pour l'afficher sur l'interface.

---

## Fichier `jeucastortravail.py`

### Variables globales

| Variable | Type | Description |
|----------|------|-------------|
| `chemin` | list | Liste des cases cliquées `[[l1,c1], [l2,c2], ...]` |
| `casedep` | list | Case de départ `[5, 4]` (pour la grille 5×6 par défaut) |
| `casearriv` | list | Case d'arrivée `[0, 0]` (haut-gauche) |
| `grille_1` | list | Grille exemple 5×6 |
| `grillecourante` | list | Grille actuellement utilisée |

**Note** : Les variables `casedep` et `casearriv` sont souvent recalculées dynamiquement dans les fonctions pour s'adapter à la taille de la grille.

---

### Représentation de la grille

Une grille est une liste de listes (tableau 2D) :

```python
grille_1 = [
    ["P","B","P","F","P","P"],  # Ligne 0 (haut)
    ["F","P","P","P","B","B"],  # Ligne 1
    ["P","P","F","P","B","P"],  # Ligne 2
    ["P","B","F","F","F","B"],  # Ligne 3
    ["P","B","P","F","B","F"]   # Ligne 4 (bas)
]
```

- **P** = Pierre
- **B** = Bois
- **F** = Feuille

**Coordonnées** : `grille[ligne][colonne]`
- Ligne 0 = haut, Ligne 4 = bas
- Colonne 0 = gauche, Colonne 5 = droite
- Case `[0, 0]` = haut-gauche (arrivée)
- Case `[4, 5]` = bas-droite (départ)

---

### Fonctions fournies

#### `cheminContinu(parcours)`

**But** : Vérifie que toutes les cases du parcours sont adjacentes consécutivement.

**Algorithme** :
- Parcourir toutes les paires de cases consécutives
- Pour chaque paire, vérifier qu'elles sont voisines
- Si une paire n'est pas voisine : retourner `False`
- Si toutes les paires sont voisines : retourner `True`

**Piège à éviter** : Le `return True` doit être **en dehors** de la boucle `for`. Si on le met dans la boucle, la fonction retournera `True` dès la première paire voisine testée.

---

#### `casesVoisinesPossibles(grille, cheminParcouru, caseActuelle)`

**But** : Retourne les cases voisines non encore visitées.

**Algorithme** :
1. Calculer les dimensions de la grille (L lignes, C colonnes)
2. Générer la liste de toutes les cases de la grille
3. À partir de la case actuelle `[x, y]`, calculer les 4 positions voisines :
   - `[x-1, y]` : au-dessus
   - `[x+1, y]` : en-dessous
   - `[x, y-1]` : à gauche
   - `[x, y+1]` : à droite
4. Filtrer les positions pour ne garder que celles qui :
   - Sont dans la grille (existent dans `cases_grille`)
   - Ne sont pas déjà dans `cheminParcouru`
5. Retourner la liste filtrée

**Utilité** : Cette fonction est utilisée pour générer les chemins aléatoires.

---

#### `chercheChemin(grille)` - Algorithme de backtracking

**But** : Recherche un chemin valide avec l'algorithme de backtracking (retour en arrière).

**Principe du backtracking** :

Le backtracking est une technique de recherche exhaustive qui explore toutes les possibilités en :
1. Essayant une solution
2. Si ça fonctionne, on continue
3. Si on est bloqué, on **revient en arrière** et on essaie autre chose

**Variables utilisées** :
- `casecourante` : position actuelle du castor
- `chemin` : liste des cases parcourues jusqu'ici
- `culDeSac` : liste des chemins testés qui ne mènent nulle part
- `nextmove` : liste des cases voisines possibles depuis la position actuelle

**Déroulement** :
1. On démarre de la case de départ
2. On cherche les cases voisines valides (qui respectent les règles)
3. On essaie la première case disponible
4. Si le chemin actuel est déjà dans `culDeSac` : on l'ignore
5. Si toutes les cases ont été testées (on est bloqué) :
   - On mémorise ce chemin dans `culDeSac`
   - On retire la dernière case (**backtrack**)
   - On revient à la case précédente
6. On continue jusqu'à atteindre `[0,0]` ou épuiser toutes les possibilités

**Exemple visuel** :
```
Départ [4,5]
├─ Essai 1 : [4,5] → [3,5] → [2,5] → Bloqué !
│  └─ Backtrack à [3,5]
└─ Essai 2 : [4,5] → [3,5] → [3,4] → ... → [0,0] ✓
```

---

#### `rechercheCasesVoisinesPossibles(grille, cheminParcouru, caseActuelle)`

**But** : Comme `casesVoisinesPossibles` mais avec filtrage selon la règle d'alternance.

**Différence clé** :
- `casesVoisinesPossibles` : retourne toutes les cases voisines non visitées
- `rechercheCasesVoisinesPossibles` : retourne uniquement celles qui respectent aussi la règle du joker

**Fonctionnement** :
1. Appelle `casesVoisinesPossibles()` pour avoir la liste de base
2. Pour chaque case de cette liste :
   - Ajoute temporairement la case au chemin
   - Teste si `ordreDesCases()` est toujours respecté
   - Si oui, garde la case ; sinon, l'élimine
   - Retire la case du chemin (test temporaire)
3. Retourne uniquement les cases valides

**Utilité** : Permet au backtracking de ne tester que les chemins qui ont une chance de réussir.

---

## À compléter : Spécifications techniques

### Partie I - Fonctions de validation

#### `sontVoisines(case1, case2)`

**Spécification** :
- **Entrée** : Deux cases `[ligne, colonne]`
- **Sortie** : `True` si adjacentes, `False` sinon
- **Règle** : Adjacence horizontale ou verticale uniquement (pas diagonale)

**Indice mathématique** : Distance de Manhattan au carré = 1

---

#### `ordreDesCases(parcours, grilleATester)`

**Spécification** :
- **Entrée** : Un parcours (liste de cases) et une grille
- **Sortie** : `True` si la règle d'alternance est respectée avec au plus 1 joker
- **Règle** : Pas deux cases du même type consécutives, sauf 1 fois maximum

**Algorithme suggéré** :
1. Construire le mot (chaîne de caractères) correspondant au parcours
2. Compter les paires de lettres identiques consécutives
3. Vérifier que ce compteur ≤ 1

**Exemple de mot** :
- Parcours `[[0,0], [0,1], [1,1]]` sur grille où `[0,0]="P"`, `[0,1]="B"`, `[1,1]="B"`
- Mot : `"PBB"` → 1 paire identique consécutive → OK (1 joker)

---

#### `departArrivee(parcours, grille)`

**Spécification** :
- **Entrée** : Un parcours et une grille
- **Sortie** : `True` si départ = bas-droite ET arrivée = haut-gauche
- **Calcul dynamique** :
  - Départ = `[len(grille)-1, len(grille[0])-1]`
  - Arrivée = `[0, 0]`

**Astuce** : Accès au premier élément avec `parcours[0]`, au dernier avec `parcours[-1]`

---

#### `verification(chemin, grille)`

**Spécification** :
- **Entrée** : Un chemin et une grille
- **Sortie** : Aucune (modification de la variable d'interface `reponse`)
- **Règle** : Les 3 conditions doivent être vraies simultanément

**Structure suggérée** :
```python
if (condition1 and condition2 and condition3):
    reponse.set("Bravo")
else:
    reponse.set("Perdu")
```

---

### Partie II - Fonctions aléatoires

#### `randomGrille(L, C)`

**Spécification** :
- **Entrée** : Nombre de lignes L, nombre de colonnes C
- **Sortie** : Une grille L×C avec cases aléatoires
- **Effet de bord** : Modifie `grillecourante` (variable globale)

**Structure** : Liste de listes (liste en compréhension à deux niveaux)

---

#### `cheminAleatoire1(grille)`

**Spécification** :
- **Entrée** : Une grille
- **Sortie** : Un chemin de la case de départ à `[0,0]`
- **Contrainte** : Ne se déplace que vers le haut ou la gauche

**Cas particuliers** :
- Si `ligne == 0` : ne peut aller qu'à gauche
- Si `colonne == 0` : ne peut aller qu'en haut
- Sinon : choix aléatoire entre les deux

---

#### `cheminAleatoire2(grille)`

**Spécification** :
- **Entrée** : Une grille
- **Sortie** : Un chemin (qui peut ne pas atteindre l'arrivée si coincé)
- **Contrainte** : Choisit aléatoirement parmi les cases voisines disponibles

**Optimisation** : Si l'arrivée est dans les cases disponibles, y aller directement.

**Gestion du blocage** : La boucle s'arrête si `nextmove == []` (aucune case disponible).

---

#### `initialisenew(grilleinit)`

**Spécification** :
- **Entrée** : Une nouvelle grille
- **Sortie** : Aucune (modification de l'interface)
- **Actions** :
  1. Réinitialiser `chemin` et `grillecourante`
  2. Supprimer les anciens boutons de la grille
  3. Recréer la grille (comme `initialise()`)

**Astuce pour supprimer les boutons** :
```python
for button in fenetre.grid_slaves():
    if (conditions pour vérifier que c'est un bouton de la grille):
        button.destroy()
```

---

#### `lanceCheminAleatoire1(grille)` et `lanceCheminAleatoire2(grille)`

**Spécification** :
- **Entrée** : Une grille
- **Sortie** : Aucune (modification de l'interface)
- **Actions** :
  1. Générer un chemin aléatoire
  2. Désactiver visuellement les boutons du chemin
  3. Vérifier si le chemin est valide

**Pattern à suivre** : Regarder `lanceAide()` qui fait la même chose avec `chercheChemin()`.

---

## Conseils de débogage

### Tests unitaires

Testez chaque fonction individuellement avant de passer à la suivante :

```python
from jeucastortravail import *

# Test 1 : Voisinage
assert sontVoisines([0,0], [0,1]) == True
assert sontVoisines([0,0], [1,1]) == False

# Test 2 : Départ/Arrivée
assert departArrivee([[4,5], [0,0]], grille_1) == True
assert departArrivee([[0,0], [4,5]], grille_1) == False

# Test 3 : Chemin continu
assert cheminContinu([[4,5], [3,5], [2,5]]) == True
assert cheminContinu([[4,5], [2,5]]) == False
```

### Erreurs courantes

| Erreur | Cause | Solution |
|--------|-------|----------|
| `return True` trop tôt | `return` dans la boucle | Mettre `return True` en dehors |
| Variable non modifiée | Oublier `global` | Ajouter `global nom_variable` |
| Indices inversés | `[colonne, ligne]` | Toujours `[ligne, colonne]` |
| Image non trouvée | Chemin relatif | Utiliser `os.path.join(SCRIPT_DIR, ...)` |
| Bouton ne répond pas | Lambda mal configurée | Vérifier capture des variables |

### Affichage de débogage

Ajoutez des `print()` pour comprendre ce qui se passe :

```python
def ordreDesCases(parcours, grille):
    mot = ''
    for case in parcours:
        mot = mot + grille[case[0]][case[1]]
    print(f"Mot construit : {mot}")  # Débogage
    # ... suite du code
```

---

## Ressources

- **Tkinter** : https://docs.python.org/fr/3/library/tkinter.html
- **Module random** : https://docs.python.org/fr/3/library/random.html
- **Listes en compréhension** : https://docs.python.org/fr/3/tutorial/datastructures.html#list-comprehensions
- **Backtracking** : https://fr.wikipedia.org/wiki/Retour_sur_trace
