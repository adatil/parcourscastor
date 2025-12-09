"""
CORRECTION - Le parcours du castor (Partie logique)
====================================================

Ce fichier contient les corrections complètes et commentées de toutes les fonctions
que les élèves doivent implémenter dans jeucastortravail.py

Projet NSI - Décembre 2022
"""

from random import choice, randint

# ===== VARIABLES GLOBALES =====
chemin = []  # Liste qui stocke le parcours du joueur au fur et à mesure des clics
casedep = [5, 4]  # Case de départ (en bas à droite pour une grille 5x6)
casearriv = [0, 0]  # Case d'arrivée (en haut à gauche)

# Grille exemple 5 lignes x 6 colonnes
grille_1 = [
    ["P", "B", "P", "F", "P", "P"],
    ["F", "P", "P", "P", "B", "B"],
    ["P", "P", "F", "P", "B", "P"],
    ["P", "B", "F", "F", "F", "B"],
    ["P", "B", "P", "F", "B", "F"]
]
grillecourante = grille_1.copy()


# =========================================
# PARTIE I - VALIDATION DU PARCOURS
# =========================================

def sontVoisines(case1, case2):
    """
    Vérifie si deux cases sont adjacentes (horizontalement ou verticalement).

    Paramètres:
        case1 (list): Première case [ligne, colonne]
        case2 (list): Deuxième case [ligne, colonne]

    Renvoie:
        bool: True si les cases sont voisines, False sinon

    Explication de la formule:
        Pour que deux cases soient voisines, elles doivent être:
        - Sur la même ligne avec colonnes différentes d'une unité, OU
        - Sur la même colonne avec lignes différentes d'une unité

        La formule mathématique: (ligne1-ligne2)² + (colonne1-colonne2)² == 1
        fonctionne car:
        - Si horizontalement voisines: (0)² + (±1)² = 1 ✓
        - Si verticalement voisines: (±1)² + (0)² = 1 ✓
        - Si en diagonale: (±1)² + (±1)² = 2 ✗
        - Si plus éloignées: résultat > 1 ✗
    """
    ligne1, colonne1 = case1
    ligne2, colonne2 = case2
    distance = (ligne1 - ligne2)**2 + (colonne1 - colonne2)**2
    return distance == 1


def ordreDesCases(parcours, grilleATester):
    """
    Vérifie que le parcours respecte la règle d'alternance des lettres.

    Règle: Pas plus d'une répétition consécutive de la même lettre (1 joker autorisé).

    Paramètres:
        parcours (list): Liste des cases du parcours [[l1,c1], [l2,c2], ...]
        grilleATester (list): Grille de jeu contenant les lettres P, B, F

    Renvoie:
        bool: True si ≤ 1 joker utilisé, False sinon

    Algorithme:
        1. Construire le "mot" correspondant au parcours (ex: "PBFBP")
        2. Compter le nombre de répétitions consécutives (ex: "PPBF" = 1 répétition)
        3. Retourner True si ≤ 1 joker utilisé

    Gestion des cas particuliers:
        - Si le parcours est vide ou contient une seule case → True (pas de répétition)
    """
    # Un parcours vide ou d'une seule case respecte trivialement la règle
    if len(parcours) <= 1:
        return True

    mot = ''
    jokerutilise = 0

    # Construction du mot à partir du parcours
    for case in parcours:
        mot = mot + grilleATester[case[0]][case[1]]

    # Comptage des répétitions consécutives
    nbrLettres = len(mot)
    for indice in range(nbrLettres - 1):
        if mot[indice] == mot[indice + 1]:
            jokerutilise += 1

    return jokerutilise <= 1


def cheminContinu(parcours):
    """
    Vérifie que toutes les cases du parcours sont voisines consécutivement.

    Paramètres:
        parcours (list): Liste des cases du parcours

    Renvoie:
        bool: True si toutes les cases consécutives sont voisines, False sinon

    Note importante:
        Le return True doit être EN DEHORS de la boucle for, sinon la fonction
        retournerait True dès la première paire de cases voisines testée.

    Gestion des cas particuliers:
        - Si le parcours est vide ou contient une seule case → True (trivialement vrai)
    """
    # Un parcours vide ou d'une seule case est trivialement continu
    if len(parcours) <= 1:
        return True

    for i in range(len(parcours) - 1):
        if not sontVoisines(parcours[i], parcours[i + 1]):
            return False
    return True  # ATTENTION : ce return est EN DEHORS de la boucle !


def departArrivee(parcours, grille=grillecourante):
    """
    Vérifie que le parcours commence en bas-droite et se termine en haut-gauche.

    Paramètres:
        parcours (list): Liste des cases du parcours
        grille (list): Grille de jeu (par défaut grillecourante)

    Renvoie:
        bool: True si départ et arrivée sont corrects, False sinon

    Explications:
        - Case de départ = [dernière_ligne, dernière_colonne]
        - Case d'arrivée = [0, 0] (coin haut-gauche)
        - parcours[0] = première case du parcours
        - parcours[-1] = dernière case du parcours

    Gestion des cas particuliers:
        - Si le parcours est vide → False (pas de départ ni d'arrivée)
        - Si le parcours contient une seule case → vérifier si c'est à la fois départ ET arrivée
    """
    # Vérifier que le parcours n'est pas vide
    if len(parcours) == 0:
        return False

    casedep = [len(grille) - 1, len(grille[0]) - 1]
    casearriv = [0, 0]
    return parcours[0] == casedep and parcours[-1] == casearriv


# =========================================
# PARTIE II - GÉNÉRATION DE GRILLES ET CHEMINS ALÉATOIRES
# =========================================

def randomGrille(L=6, C=5):
    """
    Génère une grille aléatoire de dimensions L lignes × C colonnes.

    Paramètres:
        L (int): Nombre de lignes (par défaut 6)
        C (int): Nombre de colonnes (par défaut 5)

    Renvoie:
        list: Grille générée avec des lettres P, B, F choisies aléatoirement

    Technique utilisée:
        Liste en compréhension à deux niveaux:
        [[expression for j in range(C)] for i in range(L)]
        - Boucle externe (i): parcourt les lignes
        - Boucle interne (j): parcourt les colonnes
    """
    global grillecourante
    grillecourante = [[choice(("P", "B", "F")) for i in range(C)] for j in range(L)]
    return grillecourante


def casesVoisinesPossibles(grille, cheminParcouru, caseActuelle):
    """
    Retourne la liste des cases voisines valides (dans la grille et non visitées).

    Paramètres:
        grille (list): Grille de jeu
        cheminParcouru (list): Chemin déjà parcouru
        caseActuelle (list): Position actuelle [ligne, colonne]

    Renvoie:
        list: Liste des positions possibles [[l1,c1], [l2,c2], ...]

    Algorithme:
        1. Générer toutes les cases de la grille
        2. Calculer les 4 positions voisines (haut, bas, gauche, droite)
        3. Filtrer celles qui sont dans la grille ET non visitées
    """
    L = len(grille)
    C = len(grille[0])
    cases_grille = [[i, j] for i in range(L) for j in range(C)]

    x, y = caseActuelle[0], caseActuelle[1]
    # Les 4 cases voisines possibles (haut, gauche, droite, bas)
    positionssuivantespossibles = [[x - 1, y], [x, y - 1], [x, y + 1], [x + 1, y]]

    positionssuivantesvalides = []
    for p in positionssuivantespossibles:
        if (p in cases_grille) and not (p in cheminParcouru):
            positionssuivantesvalides.append(p)

    return positionssuivantesvalides


def cheminAleatoire1(grille):
    """
    Génère un chemin aléatoire en progressant toujours vers l'arrivée.

    Stratégie: Aller uniquement vers le haut ou la gauche (jamais en arrière).

    Paramètres:
        grille (list): Grille de jeu

    Renvoie:
        list: Chemin généré de la case de départ à [0, 0]

    Algorithme:
        1. Partir de la case de départ (bas-droite)
        2. Tant qu'on n'est pas arrivé à [0, 0]:
           - Si on est sur la ligne 0 → aller à gauche obligatoirement
           - Si on est sur la colonne 0 → aller en haut obligatoirement
           - Sinon → choisir aléatoirement entre haut et gauche
        3. Retourner le chemin complet
    """
    casedep = [len(grille) - 1, len(grille[0]) - 1]
    chemin = [casedep]
    case = casedep

    while case != casearriv:
        if case[0] == 0:
            # On est sur la ligne 0, on ne peut qu'aller à gauche
            case = [0, case[1] - 1]
        elif case[1] == 0:
            # On est sur la colonne 0, on ne peut qu'aller en haut
            case = [case[0] - 1, 0]
        else:
            # On peut aller soit en haut, soit à gauche
            a = randint(0, 1)
            if a == 1:
                case = [case[0] - 1, case[1]]  # Haut
            else:
                case = [case[0], case[1] - 1]  # Gauche
        chemin.append(case)

    return chemin


def cheminAleatoire2(grille):
    """
    Génère un chemin aléatoire en explorant librement les cases voisines.

    Différence avec cheminAleatoire1: Le castor peut aller dans n'importe quelle
    direction (haut, bas, gauche, droite), ce qui peut le conduire dans un cul-de-sac.

    Paramètres:
        grille (list): Grille de jeu

    Renvoie:
        list: Chemin généré (peut ne pas atteindre l'arrivée si coincé)

    Algorithme:
        1. Partir de la case de départ
        2. Tant qu'on n'est pas arrivé ET qu'il reste des cases possibles:
           - Obtenir les cases voisines possibles (non visitées)
           - Si l'arrivée est dans les cases possibles → y aller directement
           - Sinon → choisir une case au hasard parmi les possibles
        3. Retourner le chemin (même s'il est incomplet)
    """
    casedep = [len(grille) - 1, len(grille[0]) - 1]
    casearriv = [0, 0]
    chemin = [casedep]
    case = casedep
    nextmove = None

    while case != casearriv and nextmove != []:
        nextmove = casesVoisinesPossibles(grille, chemin, case)

        if nextmove == []:
            pass  # Coincé dans un cul-de-sac, arrêt de la progression
        else:
            if casearriv in nextmove:
                # Si l'arrivée est accessible, y aller directement
                case = casearriv
            else:
                # Sinon, choisir aléatoirement parmi les cases possibles
                case = choice(nextmove)
            chemin.append(case)

    return chemin


# =========================================
# PARTIE III - RECHERCHE DE CHEMIN AVEC BACKTRACKING (DIFFICILE)
# =========================================

def rechercheCasesVoisinesPossibles(grille, cheminParcouru, caseActuelle):
    """
    Recherche les cases voisines possibles en respectant la règle d'alternance.

    Cette fonction est plus intelligente que casesVoisinesPossibles() car elle
    filtre les cases selon la règle des lettres (pas deux lettres identiques
    consécutives, sauf 1 joker).

    Paramètres:
        grille (list): Grille de jeu
        cheminParcouru (list): Chemin déjà parcouru
        caseActuelle (list): Position actuelle

    Renvoie:
        list: Liste des cases voisines qui respectent la règle d'alternance

    Algorithme:
        1. Obtenir toutes les cases voisines possibles (dans la grille, non visitées)
        2. Pour chaque case voisine:
           a. L'ajouter temporairement au chemin
           b. Tester si ordreDesCases() est respecté
           c. Si oui: la garder dans la liste des cases valides
           d. La retirer du chemin (c'était juste un test)
        3. Retourner la liste des cases valides
    """
    # Étape 1: Obtenir les cases voisines de base
    positionssuivantesvalides = casesVoisinesPossibles(grille, cheminParcouru, caseActuelle)

    # Étape 2: Filtrer selon la règle des lettres
    casesValides = []
    for case in positionssuivantesvalides:
        # Test: ajouter temporairement la case
        cheminParcouru.append(case)

        # Vérifier si le chemin respecte toujours la règle d'alternance
        if ordreDesCases(cheminParcouru, grille):
            casesValides.append(case)

        # Retirer la case (c'était juste un test)
        cheminParcouru.remove(case)

    return casesValides


def chercheChemin(grille):
    """
    Recherche un chemin valide avec l'algorithme du backtracking (retour en arrière).

    C'est la partie la plus difficile du projet !

    Paramètres:
        grille (list): Grille de jeu

    Renvoie:
        list: Chemin valide trouvé, ou chemin incomplet si aucune solution

    Principe du backtracking:
        1. Essayer d'avancer en choisissant une case voisine valide
        2. Si on est bloqué (cul-de-sac):
           - Mémoriser ce chemin comme "cul-de-sac" (pour ne pas le retenter)
           - Retirer la dernière case du chemin (backtrack)
           - Revenir à la case précédente
           - Essayer une autre direction
        3. Continuer jusqu'à atteindre [0,0] ou épuiser toutes les possibilités

    Variables clés:
        - casecourante: position actuelle du castor
        - chemin: liste des cases parcourues
        - culDeSac: liste des chemins déjà testés qui ne mènent pas à une solution
        - nextmove: cases voisines possibles à partir de la position actuelle
    """
    casecourante = [len(grille) - 1, len(grille[0]) - 1]  # Départ
    casearriv = [0, 0]  # Arrivée
    chemin = [casecourante]
    culDeSac = []  # Mémorisation des chemins qui ne marchent pas

    # Boucle principale: tant qu'on n'est pas arrivé et qu'on a encore des cases
    while casecourante != casearriv and chemin != []:
        # Obtenir les cases voisines valides (respect de la règle d'alternance)
        nextmove = rechercheCasesVoisinesPossibles(grille, chemin, casecourante)

        caseDisponible = False

        # Essayer les cases voisines une par une
        while nextmove != [] and caseDisponible == False:
            caseEnvisagee = nextmove[0]  # Prendre la première case possible
            chemin.append(caseEnvisagee)

            # Vérifier si ce chemin n'a pas déjà été testé (cul-de-sac connu)
            if chemin in culDeSac:
                nextmove = nextmove[1:]  # Retirer cette case des possibilités
                chemin.pop()  # Retirer la case du chemin
            else:
                # Cette case est valide, on avance
                casecourante = caseEnvisagee
                caseDisponible = True

        # Si plus aucune case disponible → on est dans un cul-de-sac
        if nextmove == []:
            chem = chemin.copy()
            culDeSac.append(chem)  # Mémoriser ce cul-de-sac
            chemin.pop()  # Retirer la dernière case (backtrack)

            if chemin != []:
                casecourante = chemin[-1]  # Revenir à la case précédente

    return chemin
