# Documentation des fonctions fournies

## Fichier `interfacecastortravail.py`

### Variables globales

| Variable | Type | Description |
|----------|------|-------------|
| `SCRIPT_DIR` | str | Chemin absolu du dossier contenant le script |
| `fenetre` | Tk | Fenêtre principale de l'application |
| `maPolice1` | Font | Police Arial 18 gras pour les boutons |
| `photoF`, `photoB`, `photoP` | PhotoImage | Images des cases (feuille, bois, pierre) |
| `tableauBoutons` | list | Tableau 2D contenant tous les boutons de la grille |
| `reponse` | StringVar | Variable Tkinter pour afficher "Bravo" ou "Perdu" |
| `commentaire` | Label | Label qui affiche le contenu de `reponse` |
| `validationSaisie` | Button | Bouton "Parcours terminé" |

---

### Fonctions fournies

#### `initialise(grilleinit=grille_1)`

**But** : Crée l'affichage initial de la grille avec les boutons cliquables.

**Paramètre** : `grilleinit` (list) - grille à afficher (par défaut `grille_1`)

**Fonctionnement** :
1. Calcule les dimensions L×C de la grille
2. Crée un tableau 2D `tableauBoutons`
3. Pour chaque case, crée un bouton avec l'image correspondante (P, B ou F)
4. Configure chaque bouton pour appeler `clic()` lors du clic
5. Place chaque bouton sur la grille avec `.grid(row=x, column=y)`

---

#### `clic(g, btn, ligne, colon, typecase)`

**But** : Gère le clic sur une case de la grille.

**Paramètres** :
- `g` (list) : la grille (non utilisé dans la version de base)
- `btn` (Button) : le bouton cliqué
- `ligne` (int) : numéro de ligne du bouton
- `colon` (int) : numéro de colonne du bouton
- `typecase` (str) : type de la case ("P", "B" ou "F")

**Fonctionnement** :
1. Désactive le bouton (`btn["state"] = DISABLED`)
2. Ajoute les coordonnées `[ligne, colon]` à la liste globale `chemin`

---

#### `lanceAide(grille)`

**But** : Lance la recherche automatique d'un chemin valide et l'affiche.

**Paramètre** : `grille` (list) - la grille courante

**Fonctionnement** :
1. Appelle `chercheChemin(grille)` pour trouver un chemin
2. Si un chemin est trouvé (se termine en `[0, 0]`) :
   - Désactive tous les boutons du chemin
   - Appelle `verification()` pour afficher le résultat
3. Sinon : affiche "Pas de solution trouvée !"

---

## Fichier `jeucastortravail.py`

### Variables globales

| Variable | Type | Description |
|----------|------|-------------|
| `chemin` | list | Liste des cases cliquées `[[l1,c1], [l2,c2], ...]` |
| `casedep` | list | Case de départ `[5, 4]` (bas-droite pour grille 5×6) |
| `casearriv` | list | Case d'arrivée `[0, 0]` (haut-gauche) |
| `grille_1` | list | Grille exemple 5×6 |
| `grillecourante` | list | Grille actuellement utilisée |

---

### Fonctions fournies

#### `cheminContinu(parcours)`

**But** : Vérifie que toutes les cases du parcours sont adjacentes consécutivement.

**Paramètre** : `parcours` (list) - liste de cases

**Retour** : `True` si toutes les cases sont voisines, `False` sinon

**Fonctionnement** :
```python
for i in range(len(parcours)-1):
    if not sontVoisines(parcours[i], parcours[i+1]):
        return False
return True  # EN DEHORS de la boucle !
```

**Note importante** : Le `return True` est en dehors de la boucle pour ne retourner `True` que si TOUTES les paires ont été vérifiées.

---

#### `casesVoisinesPossibles(grille, cheminParcouru, caseActuelle)`

**But** : Retourne les cases voisines non encore visitées.

**Paramètres** :
- `grille` (list) : la grille de jeu
- `cheminParcouru` (list) : cases déjà visitées
- `caseActuelle` (list) : position actuelle `[ligne, colonne]`

**Retour** : Liste des positions possibles `[[l1,c1], [l2,c2], ...]`

**Fonctionnement** :
1. Génère les 4 positions voisines (haut, bas, gauche, droite)
2. Filtre celles qui sont dans la grille
3. Filtre celles qui ne sont pas déjà dans `cheminParcouru`

---

#### `chercheChemin(grille)`

**But** : Recherche un chemin valide avec la méthode du backtracking.

**Paramètre** : `grille` (list)

**Retour** : Le chemin trouvé ou liste vide si pas de solution

**Fonctionnement** :
1. Part de la case de départ
2. Choisit une case voisine valide
3. Si bloqué (cul-de-sac) → revient en arrière
4. Mémorise les chemins testés dans `culDeSac`
5. Continue jusqu'à atteindre `[0, 0]` ou épuiser les possibilités

---

#### `rechercheCasesVoisinesPossibles(grille, cheminParcouru, caseActuelle)`

**But** : Comme `casesVoisinesPossibles` mais filtre aussi selon la règle d'alternance.

**Paramètres** : Identiques à `casesVoisinesPossibles`

**Retour** : Liste des cases valides (voisines + règle du joker respectée)

**Fonctionnement** :
1. Appelle `casesVoisinesPossibles()`
2. Pour chaque case possible, teste si `ordreDesCases()` est respecté
3. Ne garde que les cases qui respectent la règle
