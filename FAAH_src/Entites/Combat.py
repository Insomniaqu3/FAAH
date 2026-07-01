from Entites.Spawn import spawnEnnemi
from Entites.Loot import recompense
import time


class Combat:
    def __init__(self, joueur):
        self.joueur = joueur
        self.ennemiActuel = spawnEnnemi(joueur.niveau)
        
    def choisirAction(self):
        while True:
            print("Que voulez vous faire ?")
            print("1 : Attaquer")
            print("2 : Utiliser un objet")
            print("3 : Quitter le jeu")
            try:
                choix = int(input("> "))
                if choix in (1, 2, 3):
                    return choix
                else:
                    print("Choix invalide")
            except ValueError:
                print("Entrez un nombre entier")
    
    def tour(self):
        if self.ennemiActuel.hp == 0:
            print(f"    Le {self.ennemiActuel.nom} est mort !")
            recompense(self.joueur, self.ennemiActuel)
            time.sleep(2)
            self.ennemiActuel = spawnEnnemi(self.joueur.niveau)
        choix = self.choisirAction()
        if choix == 1:
            self.joueur.attaquer(self.ennemiActuel)
        elif choix == 2:
            pass # Objet non implemeter
        elif choix == 3:
            return False
        else:
            print("Choix invalide")
        time.sleep(2)
        self.ennemiActuel.attaquer(self.joueur)

    def gameLoop(self):
        # Boucle de jeu principale
        while True:
            tourActuel = self.tour()
            if tourActuel is False:
                break
            if self.joueur.hp == 0:
                print("Game Over !")
                break    