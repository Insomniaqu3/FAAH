import time
from Entites.Joueur import Joueur
from Entites.Ennemi import Ennemi
from Entites.Spawn import spawnEnnemi
from Entites.Loot import recompense

nomJoueur = input("Quel est votre nom ? ")
joueur = Joueur(nomJoueur)
ennemiActuel = spawnEnnemi(joueur.niveau)

def choisirAction():
    while True:
        print("Que voulez vous faire ?")
        print("1 : Attaquer")
        print("2 : Utiliser un objet")
        try:
            choix = int(input("> "))
            if choix in (1, 2):
                return choix
            else:
                print("Choix invalide")
        except ValueError:
            print("Entrez un nombre entier")

def game(delta, joueur, ennemiActuel):
    if ennemiActuel.hp == 0:
        print(f"    Le {ennemiActuel.nom} est mort !")
        recompense(joueur, ennemiActuel)
        time.sleep(2)
        ennemiActuel = spawnEnnemi(joueur.niveau)

    choix = choisirAction()
    if choix == 1:
        joueur.attaquer(ennemiActuel)
    elif choix == 2:
        pass # Objet non implemeter
    else:
        print("Choix invalide")
    time.sleep(2)
    ennemiActuel.attaquer(joueur)
    return ennemiActuel

# Boucle de jeu principale
lastFrameTime = time.time()
while True:
    # Delta => temps entre chaque frame
    currentTime = time.time()
    delta = currentTime - lastFrameTime
    lastFrameTime = currentTime
    ennemiActuel = game(delta, joueur, ennemiActuel) # On appelle la fonction de jeu principale avec le delta et joueur
    if joueur.hp <= 0:
        print("Game Over !")
        break