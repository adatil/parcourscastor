from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from random import *
from jeucastortravail import *
from time import *
import os

# Chemin du dossier contenant le script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# construction de la fenêtre #########################################################################

fenetre = Tk()  # création de la fenetre
maPolice1 = font.Font(family='Arial', size=18, weight='bold')
fenetre.geometry("700x700")  # taille de la fenêtre

# Chargement des images avec chemins absolus
photoF = PhotoImage(file=os.path.join(SCRIPT_DIR, "feuille.png"))
photoB = PhotoImage(file=os.path.join(SCRIPT_DIR, "bois.png"))
photoP = PhotoImage(file=os.path.join(SCRIPT_DIR, "pierre.png"))

# Mise en place des boutons #########################################################################
# nouvelleGrille = Button(...)  À compléter plus tard !
# nouvelleGrille.grid(...)
# nouvelleGrille.configure()

validationSaisie = Button(fenetre, text="Parcours terminé", font=maPolice1, relief='raised', borderwidth=5)
validationSaisie.grid(row=20, columnspan=20)
validationSaisie.configure(command=lambda: verification(chemin, grillecourante))

# cheminaleatoire1 = Button()
# cheminaleatoire1.grid()
# cheminaleatoire1.configure()
# cheminaleatoire2 = Button()
# cheminaleatoire2.grid()
# cheminaleatoire2.configure()
#
# cherchechemin = Button()
# cherchechemin.grid()
# cherchechemin.configure()


reponse = StringVar()
reponse.set("")
commentaire = Label(fenetre, font=maPolice1, textvariable=reponse)  # label qui contient le commentaire Gagné ou Perdu
commentaire.grid(row=14, column=1, columnspan=70)


def initialise(grilleinit=grille_1):
    """ fonction qui initialise le jeu : mise en place de la grille graphique et activation des boutons associés.
    Par défaut c'est la grille_1. Chaque image est affichée à sa place sur la grille.
    La grille est une liste de liste comprenant des "P", "F", "B"
    paramètre : grilleinit (list).

    """
    L = len(grillecourante)
    C = len(grillecourante[0])
    global tableauBoutons
    tableauBoutons = [[0 for i in range(C)] for j in range(L)]

    for x in range(L):
        for y in range(C):
            if grilleinit[x][y] == "P":
                bouton = Button(image=photoP, width=60, height=60)
                bouton.configure(command=lambda b=bouton, absc=x, ordon=y: clic(grillecourante, b, absc, ordon, "P"))

            elif grilleinit[x][y] == "B":
                bouton = Button(image=photoB, width=60, height=60)
                bouton.configure(command=lambda b=bouton, absc=x, ordon=y: clic(grillecourante, b, absc, ordon, "B"))

            elif grilleinit[x][y] == "F":
                bouton = Button(image=photoF, width=60, height=60)
                bouton.configure(command=lambda b=bouton, absc=x, ordon=y: clic(grillecourante, b, absc, ordon, "F"))

            tableauBoutons[x][y] = bouton
            tableauBoutons[x][y].grid(row=x, column=y)


def clic(g, btn, ligne, colon, typecase):
    """ fonction qui gère le clic sur un bouton
    paramètres grille (list)
                btn (bouton) le bouton concerné par le clic
                ligne (int)  ligne du bouton
                colon (int) colonne du bouton
                typecase (str) type de la case ("F", "B", ou "P")
    """

    btn["state"] = DISABLED  # on désactive le bouton
    global chemin  # on modifie ici la variable globale chemin
    chemin.append([ligne, colon])  # on ajoute  la case au chemin


#####################################################################################################################

def initialisenew(grilleinit=grille_1):
    """ fonction qui réinitialise le jeu : mise en place de la grille graphique et activation des boutons associés.
    Par défaut c'est la grille_1. Chaque image est affichée à sa place sur la grille.
    Ne pas oublier d'effacer une éventuelle grille précédente
    La grille est une liste de liste comprenant des "P", "F", "B"
    paramètre : grilleinit (list).

    """
    # À COMPLÉTER :
    # 1. Réinitialiser la variable globale chemin à []
    # 2. Réinitialiser la variable globale grillecourante avec grilleinit
    # 3. Effacer les anciens boutons de la grille :
    #    - Parcourir tous les boutons avec fenetre.grid_slaves()
    #    - Détruire ceux qui sont dans les limites de la grille avec button.destroy()
    # 4. Réinitialiser le message reponse.set("")
    # 5. Recréer la grille comme dans initialise()
    pass


def lanceCheminAleatoire1(grille):
    """ fonction qui répond au bouton chemin aléatoire1
    elle appelle la fonction cheminAleatoire1
    elle appelle ensuite la fonction de validation de chemin
    paramètre : grille (list).

    """
    # À COMPLÉTER :
    # 1. Appeler cheminAleatoire1(grille) et stocker le résultat dans parcours
    # 2. Pour chaque case du parcours, désactiver le bouton correspondant
    #    tableauBoutons[case[0]][case[1]].configure(state=DISABLED)
    # 3. Appeler verification(parcours, grille)
    pass


def lanceCheminAleatoire2(grille):
    """ fonction qui répond au bouton chemin aléatoire2
    elle appelle la fonction cheminAleatoire2
    elle appelle ensuite la fonction de validation de chemin
    paramètre : grille (list).

    """
    # À COMPLÉTER : même chose que lanceCheminAleatoire1 mais avec cheminAleatoire2
    pass


def lanceAide(grille):
    """Lance la recherche de chemin et l'affiche sur la grille."""
    # À COMPLÉTER : Fonction qui utilise chercheChemin pour aider le joueur
    # 1. Appeler chercheChemin(grille) et stocker le résultat dans parcours
    # 2. Vérifier si un chemin a été trouvé (parcours non vide et se termine en [0,0])
    # 3. Si oui :
    #    - Pour chaque case du parcours, désactiver le bouton correspondant
    #    - Appeler verification(parcours, grille)
    # 4. Sinon : afficher "Pas de solution trouvée !" avec reponse.set()
    pass


def verification(chemin, grille):
    """
    Fonction qui permet de vérifier la validité d'un chemin.
    paramètre : chemin (liste)
                grille (liste)
    affichera le message "Bravo" ou "Perdu" sur la grille
    """
    # À COMPLÉTER :
    # 1. Réinitialiser le message : reponse.set("")
    # 2. Vérifier les 3 conditions avec les fonctions de jeucastortravail.py :
    #    - cheminContinu(chemin)
    #    - ordreDesCases(chemin, grille)
    #    - departArrivee(chemin, grille)
    # 3. Si toutes les conditions sont vraies : reponse.set("Bravo")
    # 4. Sinon : reponse.set("Perdu")
    pass


initialise()  # on initialise une première fois !

fenetre.mainloop()
