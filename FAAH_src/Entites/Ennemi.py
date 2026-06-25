from .Entite import Entite

class Ennemi(Entite):
    def __init__(self, nom, niveauJoueur):
        hp = niveauJoueur * 1.25
        degats = niveauJoueur * 1.5
        super().__init__(nom, hp=hp, degats=degats, armure=0)