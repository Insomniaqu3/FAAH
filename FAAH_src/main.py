import time
from Entites.Joueur import Joueur
from Entites.Ennemi import Ennemi

nomJoueur = input("Quel est votre nom ? ")
joueur = Joueur(nomJoueur)

def game(delta, joueur):
    ennemi_1 = Ennemi("Goblin", joueur.niveau)
    joueur.attaquer(ennemi_1)
    print(f"Le joueur {nomJoueur} a attaquer un Goblin ! ")
    time.sleep(3)
    print(f"hp = {joueur.hp}, niveau = {joueur.niveau}, xp = {joueur.xp}")
    ennemi_1.attaquer(joueur)
    print(f"Le Goblin a attaquer {nomJoueur} ! ")
    time.sleep(3)
    print(f"hp = {joueur.hp}, niveau = {joueur.niveau}, xp = {joueur.xp}")

# Boucle de jeu principale
lastFrameTime = time.time()
while True:
    # Delta => temps entre chaque frame
    currentTime = time.time()
    delta = currentTime - lastFrameTime
    lastFrameTime = currentTime
    game(delta, joueur)  # On appelle la fonction de jeu principale avec le delta et joueur
    if joueur.hp <= 0:
        print("Game Over !")
        break