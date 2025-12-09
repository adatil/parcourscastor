# Aide sur les fonctions fournies

Ce document explique les fonctions déjà implémentées dans les fichiers de travail et donne des pistes pour les autres.

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

**Cette fonction vous est fournie comme exemple** pour vous montrer comment utiliser `sontVoisines()`.

```python
def cheminContinu(parcours):
    for i in range(len(parcours)-1):
        if not sontVoisines(parcours[i], parcours[i+1]):
            return False
    return True  # ATTENTION : ce return est EN DEHORS de la boucle !
```

**Note importante** : Le `return True` doit être en dehors de la boucle `for`, sinon la fonction retournerait `True` dès la première paire de cases voisines testée.

---

#### `casesVoisinesPossibles(grille, cheminParcouru, caseActuelle)`
Retourne la liste des cases voisines non encore visitées.

**Paramètres** :
- `grille` : la grille de jeu
- `cheminParcouru` : les cases déjà visitées
- `caseActuelle` : position actuelle `[ligne, colonne]`

**Retourne** : liste des positions possibles `[[l1,c1], [l2,c2], ...]`

**Cette fonction est fournie** car elle sera utile pour les chemins aléatoires.

---

---

## Partie III - Recherche de chemin (DIFFICILE)

#### `chercheChemin(grille)` et `rechercheCasesVoisinesPossibles(...)`
**À COMPLÉTER** - Recherche un chemin valide avec la méthode du **backtracking** (retour en arrière).

**⚠️ Partie difficile du projet !**

**Principe du backtracking** :
1. Partir de la case de départ
2. Choisir une case voisine valide
3. Si bloqué (cul-de-sac), revenir en arrière et essayer une autre direction
4. Continuer jusqu'à atteindre l'arrivée ou épuiser les possibilités

**Aide** : Lisez la documentation technique pour comprendre l'algorithme en détail.

---

## Fichier `interfacecastortravail.py`

### Fonctions fournies

#### `initialise(grilleinit)`
Crée l'affichage initial de la grille avec les boutons cliquables.
**Fonction fournie** - vous pouvez vous en inspirer pour `initialisenew()`.

#### `clic(g, btn, ligne, colon, typecase)`
Gère le clic sur une case : désactive le bouton et ajoute la case au chemin.
**Fonction fournie**.

#### `lanceAide(grille)`
**À COMPLÉTER** - Appelle `chercheChemin` et affiche le résultat sur la grille.
Vous pourrez vous en inspirer pour `lanceCheminAleatoire1/2()`.

---

## Fonctions à compléter

### Partie I - Validation du parcours

#### `sontVoisines(case1, case2)`
**But** : Vérifie si deux cases sont adjacentes (horizontalement ou verticalement).

**Indice** : Deux cases `[l1,c1]` et `[l2,c2]` sont voisines si la somme des carrés des différences vaut 1.

**Formule** : `(l1-l2)² + (c1-c2)² == 1`

**Exemple** :
- `[0,0]` et `[0,1]` → voisines (distance = 1)
- `[0,0]` et `[1,1]` → non voisines (distance diagonale)

---

#### `ordreDesCases(parcours, grille)`
**But** : Vérifie la règle d'alternance (pas deux cases identiques consécutives, sauf 1 joker).

**Étapes suggérées** :
1. Construire le mot correspondant au parcours (P, B, F, ...)
2. Compter combien de fois on a deux lettres consécutives identiques
3. Retourner `True` si ≤ 1 joker utilisé

**Exemple** :
- Parcours : P → B → F → B → P → OK (aucun joker)
- Parcours : P → P → B → F → OK (1 joker utilisé entre les deux P)
- Parcours : P → P → B → B → KO (2 jokers utilisés)

---

#### `departArrivee(parcours, grille)`
**But** : Vérifie que le parcours commence en bas-droite et finit en haut-gauche.

**Indices** :
- La case de départ est `[len(grille)-1, len(grille[0])-1]`
- La case d'arrivée est `[0, 0]`
- Utilisez `parcours[0]` pour la première case et `parcours[-1]` pour la dernière

---

#### `verification(chemin, grille)`
**But** : Affiche "Bravo" si le parcours est valide, "Perdu" sinon.

**Indices** :
- Utilisez les 3 fonctions de validation : `cheminContinu()`, `ordreDesCases()`, `departArrivee()`
- Si les 3 retournent `True` : `reponse.set("Bravo")`
- Sinon : `reponse.set("Perdu")`

---

### Partie II - Chemins aléatoires

#### `randomGrille(L, C)`
**But** : Génère une grille aléatoire de taille L×C.

**Indices** :
- Utilisez `choice(("P", "B", "F"))` pour choisir aléatoirement
- Utilisez une liste en compréhension à deux niveaux
- N'oubliez pas `global grillecourante`

---

#### `cheminAleatoire1(grille)`
**But** : Génère un chemin aléatoire en allant toujours vers le haut ou la gauche.

**Algorithme suggéré** :
1. Partir de la case de départ
2. Tant qu'on n'est pas arrivé à `[0,0]` :
   - Si on est sur la ligne 0 : aller à gauche
   - Si on est sur la colonne 0 : aller en haut
   - Sinon : choisir aléatoirement avec `randint(0,1)`
3. Retourner le chemin

---

#### `cheminAleatoire2(grille)`
**But** : Génère un chemin aléatoire en choisissant parmi les cases voisines disponibles.

**Indices** :
- Utilisez `casesVoisinesPossibles()` pour connaître les cases disponibles
- Utilisez `choice()` pour choisir une case au hasard
- Si l'arrivée est dans les cases possibles, y aller directement
- Attention : le castor peut se retrouver coincé !

---

#### `initialisenew(grilleinit)`
**But** : Réinitialise le jeu avec une nouvelle grille.

**Étapes** :
1. Réinitialiser `chemin` et `grillecourante`
2. Effacer les anciens boutons (`.destroy()`)
3. Recréer la grille (comme dans `initialise()`)

**Astuce** : Regardez comment `initialise()` fonctionne et adaptez.

---

#### `lanceCheminAleatoire1(grille)` et `lanceCheminAleatoire2(grille)`
**But** : Lance le chemin aléatoire et l'affiche sur la grille.

**Étapes** :
1. Appeler `cheminAleatoire1()` ou `cheminAleatoire2()`
2. Pour chaque case du parcours, désactiver le bouton
3. Appeler `verification()`

**Astuce** : Regardez comment `lanceAide()` fonctionne et adaptez.

---

## Conseils pratiques

### Comment tester vos fonctions ?

Vous pouvez tester vos fonctions directement dans Python sans lancer l'interface :

```python
# Ouvrir un terminal Python dans le dossier
from jeucastortravail import *

# Test sontVoisines
print(sontVoisines([0, 0], [0, 1]))  # Doit afficher True
print(sontVoisines([0, 0], [1, 1]))  # Doit afficher False

# Test parcours simple
parcours = [[4, 5], [3, 5], [2, 5], [1, 5], [0, 5], [0, 4], [0, 3], [0, 2], [0, 1], [0, 0]]
print(cheminContinu(parcours))       # True si toutes cases voisines
print(departArrivee(parcours))       # True si bon départ/arrivée
```

### Erreurs courantes

1. **Oublier `global`** : Les variables globales doivent être déclarées avec `global` avant modification
2. **`return` dans la boucle** : Attention à ne pas mettre le `return True` DANS la boucle for
3. **Indices inversés** : C'est `[ligne, colonne]` et pas `[colonne, ligne]`
4. **Oublier le `casearriv`** : Dans `cheminAleatoire1`, la condition d'arrêt est `case != [0, 0]`

### Ordre de travail suggéré

**Partie I** (dans l'ordre) :
1. `sontVoisines()` - facile, formule donnée
2. `departArrivee()` - facile, juste une comparaison
3. `ordreDesCases()` - moyen, construction de mot
4. `verification()` - facile, appel des 3 fonctions

**Partie II** (dans l'ordre) :
5. `randomGrille()` - facile, liste en compréhension
6. `cheminAleatoire1()` - moyen, while + conditions
7. `lanceCheminAleatoire1()` - facile, inspiré de `lanceAide()`
8. `lanceCheminAleatoire2()` - facile, idem
9. `cheminAleatoire2()` - moyen/difficile, gestion du hasard
10. `initialisenew()` - difficile, gestion de l'interface

**Partie III** (DIFFICILE - Backtracking) :
11. `rechercheCasesVoisinesPossibles()` - filtrage avec règle d'alternance
12. `chercheChemin()` - algorithme de backtracking complet
13. `lanceAide()` - affichage du résultat

---

## Ressources

- Documentation Tkinter : https://docs.python.org/fr/3/library/tkinter.html
- Module random : https://docs.python.org/fr/3/library/random.html
  - `choice(liste)` : choisit un élément au hasard
  - `randint(a, b)` : nombre aléatoire entre a et b
