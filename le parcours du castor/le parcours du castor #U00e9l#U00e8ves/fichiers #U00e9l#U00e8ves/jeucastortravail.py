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
    
    pass


def sontVoisines(case1, case2):
    """
    Vérifie si deux cases sont adjacentes (horizontalement ou verticalement).

    paramètres case1 (liste) case 1
               case2 (liste) case 2

    renvoie un booléen qui vaut True ou False selon le résultat
    """
    # À COMPLÉTER 
   
    pass


def ordreDesCases(parcours, grilleATester):
    """
    Vérifie si l'ordre des cases est respecté (alternance des cases avec un joker permis).

    paramètres parcours (liste)
               grilleATester (liste)

    renvoie True ou False selon le résultat
    """
    # À COMPLÉTER 
    pass


def cheminContinu(parcours):
    """
    Vérifie si toutes les cases sont adjacentes consécutivement.

    paramètres parcours (liste)

    renvoie True ou False selon le résultat
    """
    # À COMPLÉTER : vérifier que chaque case est voisine de la suivante
   


def departArrivee(parcours, grille=grillecourante):
    """
    Vérifie si les cases de départ et d'arrivée sont correctes.

    paramètres parcours (liste)
               grille (par défaut la grillecourante) (liste)

    renvoie True ou False selon le résultat
    """
  
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

    # À COMPLÉTER 
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

