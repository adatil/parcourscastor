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

**Code** :
```python
L = len(grillecourante)
C = len(grillecourante[0])
global tableauBoutons
tableauBoutons = [[0 for i in range(C)] for j in range(L)]

for x in range(L):
    for y in range(C):
        if grilleinit[x][y] == "P":
            bouton = Button(image=photoP, width=60, height=60)
            bouton.configure(command=lambda b=bouton, absc=x, ordon=y: clic(grillecourante, b, absc, ordon, "P"))
        # ... (similaire pour "B" et "F")
        tableauBoutons[x][y] = bouton
        tableauBoutons[x][y].grid(row=x, column=y)
```

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

**Code** :
```python
btn["state"] = DISABLED
global chemin
chemin.append([ligne, colon])
```

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

**Code** :
```python
parcours = chercheChemin(grille)
if parcours and parcours[-1] == [0, 0]:
    for case in parcours:
        tableauBoutons[case[0]][case[1]].configure(state=DISABLED)
    verification(parcours, grille)
else:
    reponse.set("Pas de solution trouvée !")
```

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

**Exemple** :
```python
>>> parcours1 = [[4,5], [3,5], [2,5]]
>>> cheminContinu(parcours1)
True  # Toutes les cases sont voisines

>>> parcours2 = [[4,5], [2,5]]
>>> cheminContinu(parcours2)
False  # [4,5] et [2,5] ne sont pas voisines
```

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

**Code** :
```python
L = len(grille)
C = len(grille[0])
cases_grille = [[i, j] for i in range(L) for j in range(C)]

x, y = caseActuelle[0], caseActuelle[1]
positionssuivantespossibles = [[x - 1, y], [x, y - 1], [x, y + 1], [x + 1, y]]
positionssuivantesvalides = []

for p in positionssuivantespossibles:
    if (p in cases_grille) and not (p in cheminParcouru):
        positionssuivantesvalides.append(p)

return positionssuivantesvalides
```

**Exemple** :
```python
>>> casesVoisinesPossibles(grille_1, [[4,5]], [4,5])
[[3, 5], [4, 4]]
# [3,5] est au-dessus, [4,4] est à gauche
# [5,5] n'existe pas (hors grille)
# [4,6] n'existe pas (hors grille)
```

---

#### `chercheChemin(grille)`

**But** : Recherche un chemin valide avec la méthode du backtracking.

**Paramètre** : `grille` (list)

**Retour** : Le chemin trouvé ou liste vide si pas de solution

**Algorithme - Backtracking** :

Le backtracking est une méthode de recherche exhaustive :
1. On essaie une solution
2. Si elle fonctionne, on continue
3. Si on est bloqué, on revient en arrière et on essaie une autre voie

**Fonctionnement détaillé** :
1. Part de la case de départ `[len(grille)-1, len(grille[0])-1]`
2. Cherche les cases voisines valides avec `rechercheCasesVoisinesPossibles()`
3. Choisit la première case disponible
4. Si le chemin actuel est un cul-de-sac déjà testé → essayer la case suivante
5. Si toutes les cases ont été testées (cul-de-sac) :
   - Mémoriser ce chemin dans `culDeSac`
   - Retirer la dernière case du chemin (backtrack)
   - Revenir à la case précédente
6. Continue jusqu'à atteindre `[0, 0]` ou épuiser les possibilités

**Variables utilisées** :
- `casecourante` : position actuelle du castor
- `chemin` : liste des cases parcourues
- `culDeSac` : liste des chemins déjà testés qui ne mènent nulle part
- `nextmove` : liste des cases voisines possibles
- `caseEnvisagee` : prochaine case à tester

**Exemple de déroulement** :
```
Départ : [4,5]
Essai 1 : [4,5] → [3,5] → [2,5] → ... → Bloqué !
Backtrack : retour à [3,5]
Essai 2 : [4,5] → [3,5] → [3,4] → ... → [0,0] ✓
```

---

#### `rechercheCasesVoisinesPossibles(grille, cheminParcouru, caseActuelle)`

**But** : Comme `casesVoisinesPossibles` mais filtre aussi selon la règle d'alternance.

**Paramètres** : Identiques à `casesVoisinesPossibles`

**Retour** : Liste des cases valides (voisines + règle du joker respectée)

**Fonctionnement** :
1. Appelle `casesVoisinesPossibles()` pour avoir les cases voisines non visitées
2. Pour chaque case possible :
   - Ajoute temporairement la case au chemin
   - Teste si `ordreDesCases()` est respecté
   - Si oui, garde la case ; sinon, l'élimine
   - Retire la case du chemin
3. Retourne uniquement les cases qui respectent toutes les règles

**Code** :
```python
positionssuivantesvalides = casesVoisinesPossibles(grille, cheminParcouru, caseActuelle)

casesValides = []
for case in positionssuivantesvalides:
    cheminParcouru.append(case)
    if ordreDesCases(cheminParcouru, grille):
        casesValides.append(case)
    cheminParcouru.remove(case)

return casesValides
```

**Différence avec `casesVoisinesPossibles`** :
- `casesVoisinesPossibles` : vérifie uniquement position et visite
- `rechercheCasesVoisinesPossibles` : vérifie aussi la règle d'alternance

---

## Conseils pour compléter les fonctions

### Partie I - Validation

#### `sontVoisines(case1, case2)`

**Astuce** : Deux cases sont voisines si la distance Manhattan vaut 1.

Formule : `(ligne1-ligne2)² + (colonne1-colonne2)² == 1`

```python
ligne1, colonne1 = case1
ligne2, colonne2 = case2
d = (ligne1-ligne2)**2 + (colonne1-colonne2)**2
return d == 1
```

#### `ordreDesCases(parcours, grilleATester)`

**Étapes** :
1. Construire le mot : `mot = ''`
2. Parcourir les cases et ajouter les lettres
3. Compter les paires de lettres identiques consécutives
4. Retourner `True` si ≤ 1 joker utilisé

```python
mot = ''
for case in parcours:
    mot = mot + grilleATester[case[0]][case[1]]

jokerutilise = 0
for indice in range(len(mot)-1):
    if mot[indice] == mot[indice+1]:
        jokerutilise += 1

return jokerutilise <= 1
```

#### `departArrivee(parcours, grille)`

```python
casedep = [len(grille)-1, len(grille[0])-1]
casearriv = [0, 0]
return parcours[0] == casedep and parcours[-1] == casearriv
```

### Partie II - Aléatoire

#### `randomGrille(L, C)`

```python
global grillecourante
grillecourante = [[choice(("P", "B", "F")) for j in range(C)] for i in range(L)]
return grillecourante
```

#### `cheminAleatoire1(grille)`

```python
casedep = [len(grille)-1, len(grille[0])-1]
chemin = [casedep]
case = casedep

while case != [0, 0]:
    if case[0] == 0:
        case = [0, case[1]-1]
    elif case[1] == 0:
        case = [case[0]-1, 0]
    else:
        a = randint(0, 1)
        if a == 1:
            case = [case[0]-1, case[1]]
        else:
            case = [case[0], case[1]-1]
    chemin.append(case)

return chemin
```

---

## Débogage

### Tester les fonctions séparément

```python
# Dans un terminal Python
from jeucastortravail import *

# Test 1 : sontVoisines
assert sontVoisines([0,0], [0,1]) == True
assert sontVoisines([0,0], [1,1]) == False

# Test 2 : cheminContinu
parcours = [[4,5], [3,5], [2,5]]
assert cheminContinu(parcours) == True

# Test 3 : chercheChemin
solution = chercheChemin(grille_1)
print(f"Chemin trouvé : {solution}")
print(f"Longueur : {len(solution)}")
```

### Erreurs courantes

1. **`return True` dans la boucle** → retour prématuré
2. **Oublier `global`** → variables non modifiées
3. **Indices inversés** → `[colonne, ligne]` au lieu de `[ligne, colonne]`
4. **Images non trouvées** → utiliser `SCRIPT_DIR` pour les chemins absolus

---

## Ressources

- Documentation Tkinter : https://docs.python.org/fr/3/library/tkinter.html
- Module random : https://docs.python.org/fr/3/library/random.html
- Backtracking : https://fr.wikipedia.org/wiki/Retour_sur_trace
