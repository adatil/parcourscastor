from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from random import *
from jeucastor import *
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
photoFC = PhotoImage(file=os.path.join(SCRIPT_DIR, "feuillecastor.png"))
photoPC = PhotoImage(file=os.path.join(SCRIPT_DIR, "pierrecastor.png"))
photoBC = PhotoImage(file=os.path.join(SCRIPT_DIR, "boiscastor.png"))

# Listes parallèles pour les types de cases
types_cases = ["P", "B", "F"]
photos = [photoP, photoB, photoF]
photos_castor = [photoPC, photoBC, photoFC]



# Mise en place des boutons #########################################################################
nouvelleGrille = Button(fenetre, text ="Nouvelle grille",font=maPolice1,relief='raised', borderwidth=5)
nouvelleGrille.grid(row=15,columnspan=20)
nouvelleGrille.configure(command=lambda :initialisenew(randomGrille(nombrelignes.get(),nombrecolonnes.get())))

validationSaisie = Button(fenetre, text ="Parcours terminé",font=maPolice1,relief='raised', borderwidth=5)
validationSaisie.grid(columnspan=20)
validationSaisie.configure(command=lambda :verification(chemin,grillecourante))

cheminaleatoire1 = Button(fenetre, text ="J'ai de la chance 1 !",font=maPolice1,relief='raised', borderwidth=5)
cheminaleatoire1.grid(columnspan=20)
cheminaleatoire1.configure(command=lambda : lanceCheminAleatoire1(grillecourante))
cheminaleatoire2 = Button(fenetre, text ="J'ai de la chance 2 !",font=maPolice1,relief='raised', borderwidth=5)
cheminaleatoire2.grid(columnspan=20)
cheminaleatoire2.configure(command=lambda : lanceCheminAleatoire2(grillecourante))

cherchechemin = Button(fenetre, text ="Aide !",font=maPolice1,relief='raised', borderwidth=5)
cherchechemin.grid(columnspan=20)
cherchechemin.configure(command=lambda : lanceAide(grillecourante))

nombrelignes=Scale( orient='horizontal', from_=0, to=10, resolution=1, tickinterval=5, length=150,  label='Nombre de lignes')
nombrelignes.grid(row=14,column=30, columnspan=20)
nombrecolonnes=Scale( orient='horizontal', from_=0, to=10,  resolution=1, tickinterval=5, length=150,label='Nombre de colonnes')
nombrecolonnes.grid(row=15,column=30, columnspan=20)
nombrelignes.set(5)
nombrecolonnes.set(6)



reponse=StringVar()
reponse.set("")
commentaire= Label(fenetre,font=maPolice1, textvariable=reponse) # label qui contient le commentaire Gagné ou Perdu
commentaire.grid(row=14,column=1,columnspan=70)


def initialisenew(grilleinit=grille_1):
    """ fonction qui initialise le jeu : mise en place de la grille graphique et activation des boutons asscociés.
    Par défaut c'est la grille_1. Chaque image est affichée à sa place sur la grille.
    La grille est une liste de liste comprenant des "P", "F", "B"
    paramètre : grilleinit (list).

    """
    global tableauBoutons   
    global chemin
    chemin=[]
    global grillecourante #la grille par défaut est déclarée globale : elle sera modifiée ici.
    global L
    global C
    for button in fenetre.grid_slaves():
        if int(button.grid_info()["row"])<=len(grillecourante)  and int(button.grid_info()["column"])<=len(grillecourante[0]):
            button.destroy()
    
    reponse.set("")
    
    
    grillecourante=grilleinit.copy() #la grille courante est modifiée.     
    
    L=len(grillecourante)
    C=len(grillecourante[0])
    tableauBoutons=[[0 for i in range(C)] for j in range(L)]
   
    casedep = [L-1, C-1]
    for x in range(L):
        for y in range(C):
            # Trouver l'indice du type de case dans la liste
            for i in range(len(types_cases)):
                if grilleinit[x][y] == types_cases[i]:
                    bouton = Button(image=photos[i], width=60, height=60)
                    bouton.configure(command=lambda b=bouton, absc=x, ordon=y, t=types_cases[i]: clic(grillecourante, b, absc, ordon, t))
                    break
            tableauBoutons[x][y] = bouton
            tableauBoutons[x][y].grid(row=x, column=y)
   
   
def initialise(grilleinit=grille_1):
    """ fonction qui initialise le jeu : mise en place de la grille graphique et activation des boutons asscociés.
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
            # Trouver l'indice du type de case dans la liste
            for i in range(len(types_cases)):
                if grilleinit[x][y] == types_cases[i]:
                    bouton = Button(image=photos[i], width=60, height=60)
                    bouton.configure(command=lambda b=bouton, absc=x, ordon=y, t=types_cases[i]: clic(grillecourante, b, absc, ordon, t))
                    break
            tableauBoutons[x][y] = bouton
            tableauBoutons[x][y].grid(row=x, column=y)




def clic (g,btn,ligne,colon,typecase):
    """ fonction qui gére le clic sur un bouton
    paramètres grille (list)
                btn (bouton) le bouton concerné par le clic
                ligne (int)  ligne du boton
                colon (int) colonne du bouton
                typecase (str) type de la case ("F", "B", ou "P")
    """
    # Trouver l'indice du type de case et appliquer l'image castor correspondante
    for i in range(len(types_cases)):
        if grillecourante[ligne][colon] == types_cases[i]:
            btn.configure(state=DISABLED, image=photos_castor[i])
            break
        
    global chemin # on modifie ici la variable globale chemin
    chemin.append([ligne,colon])  #on ajoute  la case au chemin



def lanceCheminAleatoire1(grille):
    parcours = cheminAleatoire1(grille)
    for case in parcours:
        tableauBoutons[case[0]][case[1]].configure(state=DISABLED)
    verification(parcours, grille)


def lanceCheminAleatoire2(grille):
    parcours = cheminAleatoire2(grille)
    for case in parcours:
        tableauBoutons[case[0]][case[1]].configure(state=DISABLED)
    verification(parcours, grille)


def lanceAide(grille):
    """Lance la recherche de chemin et l'affiche sur la grille."""
    parcours = chercheChemin(grille)
    if parcours and parcours[-1] == [0, 0]:
        # Afficher le chemin trouvé
        for case in parcours:
            tableauBoutons[case[0]][case[1]].configure(state=DISABLED)
        verification(parcours, grille)
    else:
        reponse.set("Pas de solution trouvée !")



def verification(chemin, grille):
    """Vérifie si le chemin est valide et affiche le résultat."""
    reponse.set("")

    if cheminContinu(chemin) and ordreDesCases(chemin, grille) and departArrivee(chemin, grille):
        reponse.set("Bravo")
    elif chemin[-1] != casearriv:
        reponse.set("Pas arrivé à destination !")
    else:
        reponse.set("Perdu")


initialise()
mainloop()
