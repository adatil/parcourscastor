# Aide sur les fonctions fournies

Ce document explique les fonctions déjà implémentées dans les fichiers de travail.

---

## Fichier `jeucastortravail.py`

### Variables globales

```python
chemin = []           # Liste qui stocke le parcours du joueur
casedep = [5, 4]      # Case de départ (en bas à droite)
casearriv = [0, 0]    # Case d'arrivée (en haut à gauche)
grille_1 = [...]      # Grille exemple 5x6
grillecourante = ...  # Grille actuellement utilisée
```

### Fonctions fournies

#### `cheminContinu(parcours)`
Vérifie que toutes les cases du parcours sont adjacentes consécutivement.

```python
def cheminContinu(parcours):
    for i in range(len(parcours)-1):
        if not sontVoisines(parcours[i], parcours[i+1]):
            return False
    return True  # ATTENTION : ce return est EN DEHORS de la boucle !
```

**Important** : Le `return True` doit être en dehors de la boucle `for`, sinon la fonction retourne `True` dès la première paire de cases voisines testée.

---

#### `casesVoisinesPossibles(grille, cheminParcouru, caseActuelle)`
Retourne la liste des cases voisines non encore visitées.

**Paramètres** :
- `grille` : la grille de jeu
- `cheminParcouru` : les cases déjà visitées
- `caseActuelle` : position actuelle `[ligne, colonne]`

**Retourne** : liste des positions possibles `[[l1,c1], [l2,c2], ...]`

**Exemple** :
```python
>>> casesVoisinesPossibles(grille_1, [[4,5]], [4,5])
[[3, 5], [4, 4]]  # Cases au-dessus et à gauche
```

---

#### `chercheChemin(grille)`
Recherche un chemin valide avec la méthode du **backtracking** (retour en arrière).

**Principe** :
1. Partir de la case de départ
2. Choisir une case voisine valide
3. Si bloqué (cul-de-sac), revenir en arrière et essayer une autre direction
4. Mémoriser les chemins déjà testés pour ne pas les réessayer

**Retourne** : le chemin trouvé ou une liste vide si pas de solution

---

#### `rechercheCasesVoisinesPossibles(grille, cheminParcouru, caseActuelle)`
Comme `casesVoisinesPossibles`, mais filtre aussi selon la règle d'alternance des cases.

**Utilisation** : Cette fonction est utilisée par `chercheChemin` pour ne proposer que des cases qui respectent la règle du joker.

---

## Fichier `interfacecastortravail.py`

### Variables importantes

```python
SCRIPT_DIR = ...      # Chemin du dossier du script (pour les images)
tableauBoutons = ...  # Tableau 2D des boutons de la grille
reponse = StringVar() # Variable pour afficher "Bravo" ou "Perdu"
```

### Fonctions fournies

#### `initialise(grilleinit)`
Crée l'affichage initial de la grille avec les boutons cliquables.

---

#### `clic(g, btn, ligne, colon, typecase)`
Gère le clic sur une case : désactive le bouton et ajoute la case au chemin.

---

#### `lanceAide(grille)`
Appelle `chercheChemin` et affiche le résultat sur la grille.

```python
def lanceAide(grille):
    parcours = chercheChemin(grille)
    if parcours and parcours[-1] == [0, 0]:
        # Afficher le chemin trouvé
        for case in parcours:
            tableauBoutons[case[0]][case[1]].configure(state=DISABLED)
        verification(parcours, grille)
    else:
        reponse.set("Pas de solution trouvée !")
```

---

## Fonctions à compléter

### Partie I - Validation du parcours

| Fonction | Description |
|----------|-------------|
| `sontVoisines(case1, case2)` | Vérifie si deux cases sont adjacentes |
| `ordreDesCases(parcours, grille)` | Vérifie la règle d'alternance (1 joker) |
| `departArrivee(parcours, grille)` | Vérifie départ et arrivée |
| `verification(chemin, grille)` | Affiche "Bravo" ou "Perdu" |

### Partie II - Chemins aléatoires

| Fonction | Description |
|----------|-------------|
| `randomGrille(L, C)` | Génère une grille aléatoire |
| `cheminAleatoire1(grille)` | Chemin vers haut/gauche uniquement |
| `cheminAleatoire2(grille)` | Chemin aléatoire parmi voisins disponibles |
| `initialisenew(grilleinit)` | Réinitialise l'affichage |
| `lanceCheminAleatoire1(grille)` | Lance et affiche chemin aléatoire 1 |
| `lanceCheminAleatoire2(grille)` | Lance et affiche chemin aléatoire 2 |

---

## Conseils

1. **Testez vos fonctions** dans `jeucastortravail.py` avant de les utiliser avec l'interface.

2. **Pour `sontVoisines`** : deux cases `[l1,c1]` et `[l2,c2]` sont voisines si :
   ```python
   (l1-l2)**2 + (c1-c2)**2 == 1
   ```

3. **Pour `ordreDesCases`** : construisez le mot correspondant au parcours, puis comptez les lettres consécutives identiques.

4. **Pour les chemins aléatoires** : utilisez `choice()` de la bibliothèque `random` pour choisir parmi plusieurs options.

5. **Pour `initialisenew`** : n'oubliez pas d'effacer les anciens boutons avec `button.destroy()`.
