import time
from Entites.Joueur import Joueur
from Entites.Ennemi import Ennemi
from Entites.Spawn import spawnEnnemi
from Entites.Loot import recompense

nomJoueur = input("Quel est votre nom ? ")
joueur = Joueur(nomJoueur)
ennemiActuel = spawnEnnemi(joueur.niveau)

def game(delta, joueur, ennemiActuel):
    if ennemiActuel.hp == 0:
        print(f"    Le {ennemiActuel.nom} est mort !")
        recompense(joueur, ennemiActuel)
        time.sleep(2)
        ennemiActuel = spawnEnnemi(joueur.niveau)
    hpTemp = ennemiActuel.hp
    joueur.attaquer(ennemiActuel)
    print(f"Le joueur {nomJoueur} a attaque un {ennemiActuel.nom} ! ({ennemiActuel.hp} / {hpTemp}) ")
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