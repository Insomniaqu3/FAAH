import time
from Entites.Joueur import Joueur 
from Entites.Spawn import spawnEnnemi
from Entites.Combat import Combat

nomJoueur = input("Quel est votre nom ? ")
joueur = Joueur(nomJoueur)  
partie = Combat(joueur)
partie.gameLoop()
