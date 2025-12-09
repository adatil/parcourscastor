from random import choice, randint

chemin = []  # chemin est la variable qui recueille le chemin au fur et à mesure des clics dans la grille
casedep = [5, 4]
casearriv = [0, 0]
grille_1 = [["P","B","P","F","P","P"],["F","P","P","P","B","B"],["P","P","F","P","B","P"],["P","B","F","F","F","B"],["P","B","P","F","B","F"]]
grillecourante = grille_1.copy()


def randomGrille(L=6, C=5):
    """Génère une grille aléatoire de dimensions L x C."""
    global grillecourante
    grillecourante = [[choice(("P", "B", "F")) for i in range(C)] for j in range(L)]
    return grillecourante


def sontVoisines(case1, case2):
    """Vérifie si deux cases sont voisines (adjacentes horizontalement ou verticalement)."""
    ligne1, colonne1 = case1
    ligne2, colonne2 = case2
    d = (ligne1-ligne2)**2 + (colonne1-colonne2)**2
    return d == 1


def ordreDesCases(parcours, grilleATester):
    """Vérifie que le parcours respecte la règle : pas plus d'une lettre consécutive identique."""
    mot = ''
    jokerutilise = 0

    for case in parcours:
        mot = mot + grilleATester[case[0]][case[1]]

    nbrLettres = len(mot)
    for indice in range(nbrLettres-1):
        if mot[indice] == mot[indice+1]:
            jokerutilise += 1

    return jokerutilise <= 1


def cheminContinu(parcours):
    """Vérifie que toutes les cases du parcours sont voisines consécutivement."""
    for i in range(len(parcours)-1):
        if not sontVoisines(parcours[i], parcours[i+1]):
            return False
    return True


def departArrivee(parcours, grille=grillecourante):
    """Vérifie que le parcours part du bon départ et arrive à la bonne destination."""
    casedep = [len(grille)-1, len(grille[0])-1]
    casearriv = [0, 0]
    return parcours[0] == casedep and parcours[-1] == casearriv


def casesVoisinesPossibles(grille, cheminParcouru, caseActuelle):
    """Retourne la liste des cases voisines non encore visitées."""
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


def cheminAleatoire1(grille):
    """Génère un chemin aléatoire en allant toujours vers le haut ou la gauche."""
    casedep = [len(grille)-1, len(grille[0])-1]
    chemin = [casedep]
    case = casedep

    while case != casearriv:
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


def cheminAleatoire2(grille):
    """Génère un chemin aléatoire en explorant les cases voisines possibles."""
    casedep = [len(grille)-1, len(grille[0])-1]
    casearriv = [0, 0]
    chemin = [casedep]
    case = casedep
    nextmove = None

    while case != casearriv and nextmove != []:
        nextmove = casesVoisinesPossibles(grille, chemin, case)
        if nextmove == []:
            pass  # Coincé, ne rien faire
        else:
            if casearriv in nextmove:
                case = casearriv
            else:
                case = choice(nextmove)
            chemin.append(case)

    return chemin


def chercheChemin(grille):
    """Recherche un chemin valide avec backtracking."""
    casecourante = [len(grille)-1, len(grille[0])-1]
    casearriv = [0, 0]
    chemin = [casecourante]
    culDeSac = []

    while casecourante != casearriv and chemin != []:
        nextmove = rechercheCasesVoisinesPossibles(grille, chemin, casecourante)
        caseDisponible = False
        while nextmove != [] and caseDisponible == False:
            caseEnvisagee = nextmove[0]
            chemin.append(caseEnvisagee)

            if chemin in culDeSac:
                nextmove = nextmove[1:]
                chemin.pop()
            else:
                casecourante = caseEnvisagee
                caseDisponible = True

        if nextmove == []:
            chem = chemin.copy()
            culDeSac.append(chem)
            chemin.pop()
            if chemin != []:
                casecourante = chemin[-1]

    return chemin


def rechercheCasesVoisinesPossibles(grille, cheminParcouru, caseActuelle):
    """Recherche les cases voisines possibles en vérifiant la règle des lettres."""
    # Utilise casesVoisinesPossibles puis filtre selon la règle
    positionssuivantesvalides = casesVoisinesPossibles(grille, cheminParcouru, caseActuelle)

    # Filtrer les cases qui ne respectent pas la règle des lettres
    casesValides = []
    for case in positionssuivantesvalides:
        cheminParcouru.append(case)
        if ordreDesCases(cheminParcouru, grille):
            casesValides.append(case)
        cheminParcouru.remove(case)

    return casesValides
