import random
from Entites.Ennemi import Ennemi

def spawnEnnemi(niveauJoueur):
    if niveauJoueur <= 3:
        nom = random.choice(["Goblin" , "Rat géant" , "Bandit"])
        tier = 1
    elif niveauJoueur <= 6:
        nom = random.choice(["Orc", "Zombie", "Troll"])
        tier = 2
    elif niveauJoueur <= 9:
        nom = random.choice(["Golem", "Revenant", "Basilic", "Minotaure", "Démon", "Nécromant"])
        tier = 3
    else:
        nom = random.choice(["Liche", "Draconide", "Chimère","Possédé", "Manticore", "Hydre"])
        tier = 4
    return Ennemi(nom, niveauJoueur, tier)