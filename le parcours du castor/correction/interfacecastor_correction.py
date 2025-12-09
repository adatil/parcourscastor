"""
CORRECTION - Le parcours du castor (Partie interface graphique)
================================================================

Ce fichier contient les corrections complètes et commentées de toutes les fonctions
d'interface que les élèves doivent implémenter dans interfacecastortravail.py

Projet NSI - Décembre 2022
Technologies: Python, Tkinter, PIL
"""

from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from random import *
from time import *
import os
import sys

# ===== CONFIGURATION DU CHEMIN DES IMAGES ET MODULES =====
# Permet de charger les images et modules même si le script n'est pas lancé depuis son dossier
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Ajouter le répertoire du script au path Python pour l'import
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

# Importer le module de jeu depuis le même dossier
from jeucastor_correction import *

# ===== CONSTRUCTION DE LA FENÊTRE PRINCIPALE =====

fenetre = Tk()
maPolice1 = font.Font(family='Arial', size=18, weight='bold')
fenetre.geometry("700x700")

# ===== CHARGEMENT DES IMAGES =====
# Images normales (cases non cliquées)
photoF = PhotoImage(file=os.path.join(SCRIPT_DIR, "feuille.png"))
photoB = PhotoImage(file=os.path.join(SCRIPT_DIR, "bois.png"))
photoP = PhotoImage(file=os.path.join(SCRIPT_DIR, "pierre.png"))

# Images avec le castor (cases cliquées)
photoFC = PhotoImage(file=os.path.join(SCRIPT_DIR, "feuillecastor.png"))
photoPC = PhotoImage(file=os.path.join(SCRIPT_DIR, "pierrecastor.png"))
photoBC = PhotoImage(file=os.path.join(SCRIPT_DIR, "boiscastor.png"))

# Listes parallèles pour faciliter l'itération
types_cases = ["P", "B", "F"]
photos = [photoP, photoB, photoF]
photos_castor = [photoPC, photoBC, photoFC]


# =========================================
# MISE EN PLACE DES BOUTONS DE CONTRÔLE
# =========================================

# Bouton pour générer une nouvelle grille aléatoire
nouvelleGrille = Button(fenetre, text="Nouvelle grille", font=maPolice1,
                        relief='raised', borderwidth=5)
nouvelleGrille.grid(row=15, columnspan=20)
nouvelleGrille.configure(command=lambda: initialisenew(
    randomGrille(nombrelignes.get(), nombrecolonnes.get())))

# Bouton de validation du parcours manuel
validationSaisie = Button(fenetre, text="Parcours terminé", font=maPolice1,
                         relief='raised', borderwidth=5)
validationSaisie.grid(columnspan=20)
validationSaisie.configure(command=lambda: verification(chemin, grillecourante))

# Bouton chemin aléatoire 1 (progression directe)
cheminaleatoire1 = Button(fenetre, text="J'ai de la chance 1 !", font=maPolice1,
                         relief='raised', borderwidth=5)
cheminaleatoire1.grid(columnspan=20)
cheminaleatoire1.configure(command=lambda: lanceCheminAleatoire1(grillecourante))

# Bouton chemin aléatoire 2 (exploration libre)
cheminaleatoire2 = Button(fenetre, text="J'ai de la chance 2 !", font=maPolice1,
                         relief='raised', borderwidth=5)
cheminaleatoire2.grid(columnspan=20)
cheminaleatoire2.configure(command=lambda: lanceCheminAleatoire2(grillecourante))

# Bouton d'aide (backtracking)
cherchechemin = Button(fenetre, text="Aide !", font=maPolice1,
                      relief='raised', borderwidth=5)
cherchechemin.grid(columnspan=20)
cherchechemin.configure(command=lambda: lanceAide(grillecourante))

# Curseurs pour choisir la taille de la grille
nombrelignes = Scale(orient='horizontal', from_=0, to=10, resolution=1,
                     tickinterval=5, length=150, label='Nombre de lignes')
nombrelignes.grid(row=14, column=30, columnspan=20)

nombrecolonnes = Scale(orient='horizontal', from_=0, to=10, resolution=1,
                      tickinterval=5, length=150, label='Nombre de colonnes')
nombrecolonnes.grid(row=15, column=30, columnspan=20)

# Valeurs par défaut
nombrelignes.set(5)
nombrecolonnes.set(6)

# Label pour afficher le résultat (Bravo/Perdu)
reponse = StringVar()
reponse.set("")
commentaire = Label(fenetre, font=maPolice1, textvariable=reponse)
commentaire.grid(row=14, column=1, columnspan=70)


# =========================================
# FONCTIONS D'INTERFACE À COMPLÉTER
# =========================================

def initialise(grilleinit=grille_1):
    """
    Initialise le jeu avec une grille donnée (fonction fournie aux élèves).

    Cette fonction crée l'affichage graphique initial de la grille avec tous
    les boutons cliquables.

    Paramètres:
        grilleinit (list): Grille à afficher (par défaut grille_1)

    Technique Tkinter:
        - Création d'un tableau 2D de boutons avec Button()
        - Placement avec .grid(row=x, column=y)
        - Configuration du clic avec lambda pour passer les paramètres
    """
    L = len(grillecourante)
    C = len(grillecourante[0])
    global tableauBoutons
    tableauBoutons = [[0 for i in range(C)] for j in range(L)]

    for x in range(L):
        for y in range(C):
            # Trouver l'indice du type de case dans la liste
            for i in range(len(types_cases)):
                if grilleinit[x][y] == types_cases[i]:
                    bouton = Button(image=photos[i], width=60, height=60)
                    # Lambda pour capturer les valeurs de x, y, typecase au moment de la création
                    bouton.configure(command=lambda b=bouton, absc=x, ordon=y,
                                   t=types_cases[i]: clic(grillecourante, b, absc, ordon, t))
                    break
            tableauBoutons[x][y] = bouton
            tableauBoutons[x][y].grid(row=x, column=y)


def clic(g, btn, ligne, colon, typecase):
    """
    Gère le clic sur une case de la grille (fonction fournie aux élèves).

    Actions effectuées:
        1. Désactive le bouton (pour éviter de cliquer deux fois)
        2. Change l'image pour afficher le castor
        3. Ajoute la case au chemin global

    Paramètres:
        g (list): Grille de jeu
        btn (Button): Bouton concerné par le clic
        ligne (int): Ligne du bouton
        colon (int): Colonne du bouton
        typecase (str): Type de la case ("F", "B", ou "P")
    """
    # Trouver l'indice du type de case et appliquer l'image castor correspondante
    for i in range(len(types_cases)):
        if grillecourante[ligne][colon] == types_cases[i]:
            btn.configure(state=DISABLED, image=photos_castor[i])
            break

    global chemin
    chemin.append([ligne, colon])


def initialisenew(grilleinit=grille_1):
    """
    Réinitialise le jeu avec une nouvelle grille.

    Cette fonction est similaire à initialise() mais elle doit:
        1. Réinitialiser les variables globales (chemin, grillecourante)
        2. Effacer les anciens boutons de la grille précédente
        3. Effacer le message de résultat
        4. Créer la nouvelle grille

    Paramètres:
        grilleinit (list): Nouvelle grille à afficher

    Différences avec initialise():
        - Réinitialisation de chemin à []
        - Destruction des anciens boutons avec .destroy()
        - Mise à jour de grillecourante

    Astuce Tkinter:
        fenetre.grid_slaves() retourne tous les widgets placés avec grid()
        On filtre ceux qui sont dans la zone de la grille et on les détruit
    """
    global tableauBoutons
    global chemin
    chemin = []  # Réinitialiser le chemin
    global grillecourante
    global L
    global C

    # Effacer les anciens boutons de la grille
    for button in fenetre.grid_slaves():
        # Vérifier que le bouton est dans la zone de la grille
        if (int(button.grid_info()["row"]) <= len(grillecourante) and
            int(button.grid_info()["column"]) <= len(grillecourante[0])):
            button.destroy()

    # Effacer le message de résultat
    reponse.set("")

    # Mettre à jour la grille courante
    grillecourante = grilleinit.copy()

    # Créer la nouvelle grille
    L = len(grillecourante)
    C = len(grillecourante[0])
    tableauBoutons = [[0 for i in range(C)] for j in range(L)]

    casedep = [L - 1, C - 1]
    for x in range(L):
        for y in range(C):
            # Trouver l'indice du type de case dans la liste
            for i in range(len(types_cases)):
                if grilleinit[x][y] == types_cases[i]:
                    bouton = Button(image=photos[i], width=60, height=60)
                    bouton.configure(command=lambda b=bouton, absc=x, ordon=y,
                                   t=types_cases[i]: clic(grillecourante, b, absc, ordon, t))
                    break
            tableauBoutons[x][y] = bouton
            tableauBoutons[x][y].grid(row=x, column=y)


def verification(chemin, grille):
    """
    Vérifie si le parcours du joueur est valide et affiche le résultat.

    Critères de validation:
        1. cheminContinu(chemin) → toutes les cases sont voisines consécutivement
        2. ordreDesCases(chemin, grille) → respect de la règle d'alternance
        3. departArrivee(chemin, grille) → bon départ et bonne arrivée

    Paramètres:
        chemin (list): Parcours du joueur
        grille (list): Grille de jeu

    Affichage:
        - "Aucun parcours !" si le chemin est vide
        - "Bravo" si les 3 conditions sont remplies
        - "Pas arrivé à destination !" si la dernière case n'est pas [0, 0]
        - "Perdu" dans les autres cas
    """
    reponse.set("")  # Effacer l'ancien message

    # Vérifier d'abord que le chemin n'est pas vide
    if len(chemin) == 0:
        reponse.set("Aucun parcours !")
        return

    # Vérifier les 3 conditions
    if cheminContinu(chemin) and ordreDesCases(chemin, grille) and departArrivee(chemin, grille):
        reponse.set("Bravo")
    elif chemin[-1] != casearriv:
        reponse.set("Pas arrivé à destination !")
    else:
        reponse.set("Perdu")


def lanceCheminAleatoire1(grille):
    """
    Lance le chemin aléatoire de type 1 et l'affiche sur la grille.

    Algorithme:
        1. Appeler cheminAleatoire1(grille) pour générer le parcours
        2. Pour chaque case du parcours, désactiver le bouton correspondant
        3. Appeler verification() pour vérifier si le parcours est valide

    Paramètres:
        grille (list): Grille de jeu

    Note:
        Cette fonction sert de "pont" entre la logique (jeucastor.py)
        et l'interface graphique (interfacecastor.py)
    """
    parcours = cheminAleatoire1(grille)

    # Désactiver visuellement tous les boutons du parcours
    for case in parcours:
        tableauBoutons[case[0]][case[1]].configure(state=DISABLED)

    # Vérifier si le parcours est valide
    verification(parcours, grille)


def lanceCheminAleatoire2(grille):
    """
    Lance le chemin aléatoire de type 2 et l'affiche sur la grille.

    Même principe que lanceCheminAleatoire1() mais utilise cheminAleatoire2().

    Paramètres:
        grille (list): Grille de jeu

    Différence avec type 1:
        Le parcours peut être incomplet si le castor se retrouve coincé
        dans un cul-de-sac.
    """
    parcours = cheminAleatoire2(grille)

    # Désactiver visuellement tous les boutons du parcours
    for case in parcours:
        tableauBoutons[case[0]][case[1]].configure(state=DISABLED)

    # Vérifier si le parcours est valide
    verification(parcours, grille)


def lanceAide(grille):
    """
    Lance la recherche de chemin avec backtracking et affiche le résultat.

    Cette fonction utilise l'algorithme le plus complexe du projet:
    chercheChemin() qui trouve un chemin valide en explorant toutes les
    possibilités avec retour en arrière.

    Algorithme:
        1. Appeler chercheChemin(grille)
        2. Vérifier si un chemin a été trouvé (non vide et se termine en [0,0])
        3. Si oui:
           - Désactiver tous les boutons du parcours
           - Appeler verification()
        4. Sinon:
           - Afficher "Pas de solution trouvée !"

    Paramètres:
        grille (list): Grille de jeu

    Cas d'échec:
        Il existe des grilles sans solution (exemple: grille 2x2 avec "PPPP"
        ou "BBBB" partout, impossible de respecter la règle d'alternance)
    """
    parcours = chercheChemin(grille)

    # Vérifier si un chemin valide a été trouvé
    if parcours and parcours[-1] == [0, 0]:
        # Afficher le chemin trouvé sur la grille
        for case in parcours:
            tableauBoutons[case[0]][case[1]].configure(state=DISABLED)
        verification(parcours, grille)
    else:
        reponse.set("Pas de solution trouvée !")


# ===== INITIALISATION ET LANCEMENT =====
initialise()  # Créer l'affichage initial avec grille_1
mainloop()  # Lancer la boucle d'événements Tkinter
