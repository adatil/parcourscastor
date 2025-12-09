from tkinter import*
from tkinter import font
from PIL import Image, ImageTk
from random import *
from jeucastortravail import *
from time import *
#
# construction de la fenêtre #########################################################################



fenetre= Tk() #création de la fenetre
maPolice1=font.Font(family='Arial', size=18, weight='bold')
fenetre.geometry("700x700") #taille de la fenêtre
photoF=PhotoImage(file="feuille.png")
photoB=PhotoImage(file="bois.png")
photoP=PhotoImage(file="pierre.png")

# Mise en place des boutons #########################################################################
#nouvelleGrille = Button(...)  A compléter plus tard !
#nouvelleGrille.grid(...)
#nouvelleGrille.configure()

validationSaisie = Button(fenetre, text ="Parcours terminé",font=maPolice1,relief='raised', borderwidth=5)
validationSaisie.grid(row=20,columnspan=20)
validationSaisie.configure(command=lambda :verification(chemin,grillecourante))

#cheminaleatoire1 = Button()
#cheminaleatoire1.grid()
#cheminaleatoire1.configure()
#cheminaleatoire2 = Button()
#cheminaleatoire2.grid()
#cheminaleatoire2.configure()
#
#cherchechemin = Button()
#cherchechemin.grid()
#cherchechemin.configure()


reponse=StringVar()
reponse.set("")
commentaire= Label(fenetre,font=maPolice1, textvariable=reponse) # label qui contient le commentaire Gagné ou Perdu
commentaire.grid(row=14,column=1,columnspan=70)


  
   
def initialise(grilleinit=grille_1):
    """ fonction qui initialise le jeu : mise en place de la grille graphique et activation des boutons asscociés.
    Par défaut c'est la grille_1. Chaque image est affichée à sa place sur la grille.
    La grille est une liste de liste comprenant des "P", "F", "B"
    paramètre : grilleinit (list).

    """
    L=len(grillecourante)
    C=len(grillecourante[0])
    global tableauBoutons
    tableauBoutons=[[0 for i in range(C)] for j in range(L)] 
  
    for x in range(L):
        for y in range(C):
            if grilleinit[x][y]=="P":
                bouton = Button(image=photoP,width=60,height=60)
                bouton.configure(command= lambda b=bouton,absc=x, ordon=y : clic(grillecourante,b,absc,ordon,"P"))
                
            if grilleinit[x][y]=="B":
                bouton = Button(image=photoB,width=60,height=60)
                bouton.configure(command= lambda b=bouton,absc=x, ordon=y : clic(grillecourante,b,absc,ordon,"B"))
                
            if grilleinit[x][y]=="F":
                bouton = Button(image=photoF,width=60,height=60)
                bouton.configure(command= lambda b=bouton,absc=x, ordon=y : clic(grillecourante,b,absc,ordon,"F"))
            tableauBoutons[x][y]=bouton          
            tableauBoutons[x][y].grid(row=x, column=y)


def clic (g,btn,ligne,colon,typecase):
    """ fonction qui gére le clic sur un bouton
    paramètres grille (list)
                btn (bouton) le bouton concerné par le clic
                ligne (int)  ligne du boton
                colon (int) colonne du bouton
                typecase (str) type de la case ("F", "B", ou "P")
    """
    
    btn["state"]=DISABLED  # on désactive le bouton
    global chemin # on modifie ici la variable globale chemin
    chemin.append([ligne,colon])  #on ajoute  la case au chemin

#####################################################################################################################

def initialisenew(grilleinit=grille_1):
    """ fonction qui réinitialise le jeu : mise en place de la grille graphique et activation des boutons asscociés.
    Par défaut c'est la grille_1. Chaque image est affichée à sa place sur la grille.
    Ne pas oublier d'effacer une éventuelle grille précédente
    La grille est une liste de liste comprenant des "P", "F", "B"
    paramètre : grilleinit (list).

    """
    

def lanceCheminAleatoire1(grille):
    
    """ fonction qui répond au bouton chemin aléatoire1
    elle appelle la fonction cheminAléatoire1
    elle appelle ensuite la fonction de validation de chemin
    paramètre : grille (list).

    """
    



def lanceCheminAleatoire2(grille):
     """ fonction qui répond au bouton chemin aléatoire2
    elle appelle la fonction cheminAléatoire2
    elle appelle ensuite la fonction de validation de chemin
    paramètre : grille (list).

    """
    



def verification(chemin,grille):
     
    """
    Fonction qui permet de vérfier la validité d'un chemin.
    paramètre : chemin (liste)
                grille (liste)
    affichera le message "Bravo" ou "Perdu" sur la grille
    """
  

initialise() # on initilialise une première fois !

fenetre.mainloop()
    
    
    
    
    

        
     