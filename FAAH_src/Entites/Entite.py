class Entite:
    def __init__(self, nom, hp, degats, armure):
        self.nom = nom
        self.hp = hp
        self.degats = degats
        self.armure = armure

    def attaquer(self, cible):
        return cible.prendreDegats(self.degats)

    def prendreDegats(self, montant):
        self.hp = max(0, self.hp - montant)
        return montant