from .Entite import Entite

class Joueur(Entite): # Initialise le joueur, (niveau 1 avec 0 xp et 10 de degats)
    def __init__(self, nom):
        super().__init__(nom, hp=100, degats=10, armure= 0)
        self.niveau = 1
        self.xp = 0
    
    def monterNiveau(self): # Quand l'xp du joueur arrive a 100 fois son niveau, il monte de niveau, l'xp retourne a 0
        if self.xp >= self.niveau * 100:
            self.niveau += 1
            self.xp = 0
            print(f"Vous etes monter de niveau ! (Niveau actuel : {self.niveau})")