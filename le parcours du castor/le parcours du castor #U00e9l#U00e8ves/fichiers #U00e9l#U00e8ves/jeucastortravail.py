from random import choice, randint

chemin = []  # chemin est la variable qui recueille le chemin au fur et à mesure des clics dans la grille
casedep = [5, 4]
casearriv = [0, 0]
grille_1 = [["P","B","P","F","P","P"],["F","P","P","P","B","B"],["P","P","F","P","B","P"],["P","B","F","F","F","B"],["P","B","P","F","B","F"]]
grillecourante = grille_1.copy()


def randomGrille(L=6, C=5):
    """
    Création d'une grille aléatoire.
    Cette fonction modifie au passage la grille courante
    cette variable est donc déclarée globale.

    paramètres L (int) nombre de lignes
               C (int) nombre de colonnes

    renvoie grillecourante (liste)
    """
    global grillecourante
    # À COMPLÉTER : créer une grille aléatoire avec choice(("P", "B", "F"))
    # Utiliser une liste en compréhension : [[choice(...) for j in range(C)] for i in range(L)]
    pass


def sontVoisines(case1, case2):
    """
    Vérifie si deux cases sont adjacentes (horizontalement ou verticalement).

    paramètres case1 (liste) case 1
               case2 (liste) case 2

    renvoie un booléen qui vaut True ou False selon le résultat
    """
    # À COMPLÉTER : calculer la distance entre les deux cases
    # Deux cases sont voisines si la somme des carrés des différences vaut 1
    # Formule : (ligne1-ligne2)**2 + (colonne1-colonne2)**2 == 1
    pass


def ordreDesCases(parcours, grilleATester):
    """
    Vérifie si l'ordre des cases est respecté (alternance des cases avec un joker permis).

    paramètres parcours (liste)
               grilleATester (liste)

    renvoie True ou False selon le résultat
    """
    # À COMPLÉTER : construire le mot à partir du parcours
    # 1. Créer une variable mot = '' vide
    # 2. Pour chaque case du parcours, ajouter la lettre correspondante au mot
    # 3. Compter combien de fois on a deux lettres consécutives identiques
    # 4. Renvoyer True si au plus 1 joker utilisé (<=1), False sinon
    pass


def cheminContinu(parcours):
    """
    Vérifie si toutes les cases sont adjacentes consécutivement.

    paramètres parcours (liste)

    renvoie True ou False selon le résultat
    """
    # À COMPLÉTER : vérifier que chaque case est voisine de la suivante
    # ATTENTION : le return True doit être EN DEHORS de la boucle for
    for i in range(len(parcours)-1):
        if not sontVoisines(parcours[i], parcours[i+1]):
            return False
    return True


def departArrivee(parcours, grille=grillecourante):
    """
    Vérifie si les cases de départ et d'arrivée sont correctes.

    paramètres parcours (liste)
               grille (par défaut la grillecourante) (liste)

    renvoie True ou False selon le résultat
    """
    casedep = [len(grille)-1, len(grille[0])-1]
    casearriv = [0, 0]
    # À COMPLÉTER : vérifier que parcours[0] == casedep et parcours[-1] == casearriv
    pass


def casesVoisinesPossibles(grille, cheminParcouru, caseActuelle):
    """
    Propose des cases possibles pour un parcours aléatoire.
    Cette fonction se contente de proposer des cases voisines qui sont dans la grille.

    paramètres  grille (liste)
                cheminParcouru (liste)
                caseActuelle (liste)

    renvoie la liste des positions suivantes possibles sous forme d'une liste
    """
    L = len(grille)
    C = len(grille[0])
    cases_grille = [[i, j] for i in range(L) for j in range(C)]

    x, y = caseActuelle[0], caseActuelle[1]
    positionssuivantespossibles = [[x - 1, y], [x, y - 1], [x, y + 1], [x + 1, y]]
    positionssuivantesvalides = []

    # À COMPLÉTER : filtrer les positions qui sont dans la grille et pas déjà parcourues
    for p in positionssuivantespossibles:
        if (p in cases_grille) and not (p in cheminParcouru):
            positionssuivantesvalides.append(p)

    return positionssuivantesvalides


def cheminAleatoire1(grille):
    """
    Propose un chemin aléatoire progressant vers l'arrivée (déplacement vers le haut ou la gauche uniquement).

    paramètres grille (liste)

    renvoie le chemin proposé
    """
    casedep = [len(grille)-1, len(grille[0])-1]
    chemin = [casedep]
    case = casedep

    # À COMPLÉTER : avancer vers [0,0] en allant vers le haut ou la gauche
    # 1. Boucle while case != casearriv:
    # 2. Si on est sur la ligne 0 : aller à gauche
    # 3. Si on est sur la colonne 0 : aller en haut
    # 4. Sinon : choisir aléatoirement avec randint(0,1)
    # 5. Ajouter la nouvelle case au chemin
    # 6. Retourner le chemin
    pass


def cheminAleatoire2(grille):
    """
    Propose un chemin aléatoire progressant aléatoirement.

    paramètres grille (liste)

    renvoie le chemin proposé
    """
    casedep = [len(grille)-1, len(grille[0])-1]
    casearriv = [0, 0]
    chemin = [casedep]
    case = casedep
    nextmove = None

    # À COMPLÉTER : utiliser casesVoisinesPossibles et choice pour avancer
    # 1. Boucle while case != casearriv et nextmove != []:
    # 2. Appeler casesVoisinesPossibles pour avoir les cases possibles
    # 3. Si casearriv est dans les cases possibles, y aller directement
    # 4. Sinon, choisir une case au hasard avec choice()
    # 5. Ajouter la case au chemin
    # 6. Retourner le chemin
    pass


def chercheChemin(grille):
    """
    Cherche un chemin valide pour le castor avec backtracking (retour en arrière).

    paramètres grille (liste)

    renvoie le chemin proposé
    """
    # À COMPLÉTER : Algorithme de backtracking (DIFFICILE - Partie III)
    # Principe :
    # 1. Partir de la case de départ
    # 2. Chercher les cases voisines possibles (avec rechercheCasesVoisinesPossibles)
    # 3. Essayer la première case disponible
    # 4. Si on est bloqué (cul-de-sac) :
    #    - Mémoriser ce chemin comme cul-de-sac
    #    - Retirer la dernière case du chemin (backtrack)
    #    - Revenir à la case précédente
    # 5. Continuer jusqu'à atteindre [0,0] ou épuiser les possibilités
    #
    # Variables utiles :
    # - casecourante : position actuelle
    # - chemin : liste des cases parcourues
    # - culDeSac : liste des chemins déjà testés qui ne marchent pas
    # - nextmove : cases voisines possibles
    pass


def rechercheCasesVoisinesPossibles(grille, cheminParcouru, caseActuelle):
    """
    Recherche les cases voisines possibles en vérifiant la règle des lettres.

    paramètres grille (liste)
               cheminParcouru (liste) : le chemin déjà parcouru
               caseActuelle (liste) : case sur laquelle se trouve le castor

    renvoie la liste des cases valides
    """
    # À COMPLÉTER : Filtrer les cases voisines selon la règle d'alternance
    # 1. Appeler casesVoisinesPossibles() pour avoir les cases voisines de base
    # 2. Pour chaque case possible :
    #    - Ajouter temporairement la case au chemin
    #    - Tester si ordreDesCases() est respecté
    #    - Si oui, garder la case dans la liste des cases valides
    #    - Retirer la case du chemin (c'était juste un test)
    # 3. Retourner la liste des cases valides
    pass
