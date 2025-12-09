from random import *
chemin=[] #chemin est la variable qui recueille le chemin au fur et à mesure des clics dans la grille
casedep=[5,4]
casearriv=[0,0]
grille_1= [["P","B","P","F","P","P"],["F","P","P","P","B","B"],["P","P","F","P","B","P"],["P","B","F","F","F","B"],["P","B","P","F","B","F"]]
grillecourante=grille_1.copy()



def randomGrille(L=6,C=5):
    """
    créeation d'une grille aléatoire.
    cette fonction modfie au passage la grille courante
    cette variable est donc déclarrée globale.
    
    paramètres L (int) nombre de lignes
               C (int) nombre de colonnes
    
    renvoie grille courante (liste)
    

    """
    global grillecourante
   
    
    
def sontVoisines(case1, case2):
    """
    vérifie si deux cases sont adjacentes
    
       
    paramètres case1 (liste) case 1
               case2 (liste) case 2
    
    renvoie un booléen qui vaut True ou False selon le résultat
    

    """
    



def ordreDesCases(parcours,grilleATester):
    """
    vérifie si l'odre des cases est respécté (alternance des cases avec un joker permis)
    
       
    paramètres parcours (liste) 
               grilleATester (liste) 
    
    renvoie True ou False selon le résultat    
    """
    
   
            


def cheminContinu(parcours):
    """
    vérifie si toutes cases sont adjacentes (
    
       
    paramètres parcours (liste) 
               
    
    renvoie True ou False selon le résultat    
    """
    
    
    
   
    

def departArrivee(parcours,grille=grillecourante):
    """
    vérifie si les cases de départ et d'arrivée sont correctes.
    
       
    paramètres parcours (liste) 
               grille (par défaut la grillecourante (liste) 
    
    renvoie True ou False selon le résultat    
    """
    
   

    
def casesVoisinesPossibles(grille,cheminParcouru,caseActuelle):
    """
    propose des cases possibles pour un parcours aléatoire.
    Cette fonction se contente de proposer des cases voisines qui sont dans la grille
    
      
    paramètres  grille (liste
                cheminParcouru (liste) 
                caseActuelle (liste) 
    
    renvoie la liste des positions suivantes possibles sous forme d'une liste
    """
    
    



def cheminAleatoire1(grille):
    """
    propose un chemin aléatoire progressant vers l'arrivée (déplacement vers le haut ou la gauche uniquement)
    
       
    paramètres grille (liste) 
    
    renvoie le chemin proposé  
    """
    

    





def cheminAleatoire2(grille):
    """
    propose un chemin aléatoire progressant aléatoirement .
    
       
    paramètres grille (liste) 
               
    
    renvoie le chemin proposé  
    """
    
    
    

    


def chercheChemin(grille):
   """
    cherche un chemin valide pour le castor
    
       
    paramètres grille(liste)
    
    renvoie le chemin proposé  
    """
   
        

         
                    
                    
        
        
       

def rechercheCasesVoisinesPossibles(grille,cheminParcouru,caseActuelle):
    """
    cherche les cases possibles au cours du mouvement
    
       
    paramètres grille (liste) 
               cheminParcouru (liste) : le chemin déjà parcouru
               caseActuelle (liste) : case sur laquelle se trouve le castor
    
    renvoie le chemin proposé  
    """
    
    pass

 
    
    
    
    
    
