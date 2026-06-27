from .Entite import Entite

class Ennemi(Entite):
    def __init__(self, nom, niveauJoueur, tier):
        hp = niveauJoueur * 12
        degats = niveauJoueur * 1.5
        armure = niveauJoueur * 0.5
        super().__init__(nom, hp=hp, degats=degats,armure=armure)
        self.tier = tier # tier de l'ennemi (permet de determiner le loot donner)
        self.xp = tier * 50
        