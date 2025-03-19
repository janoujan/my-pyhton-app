class Vehicule:
    # le constructeur avec ses attributs d'instance
    def __init__(self, marque, modele, vitesse):
        self.marque = marque
        self.modele = modele
        self.vitesse = vitesse

    # methode pour afficher une description du vehicule
    def description(self):
        return f"{self.marque} {self.modele}, vitesse: {self.vitesse} km/h"

    # methode pour accelerer
    def accelerer(self, increment):
        self.vitesse += increment
        return (f"La voiture accelere de {increment} km/h, "
                f"vitesse: {self.vitesse} km/h")
   
    # methode pour freiner
    def freiner(self, decrement):
        self.vitesse -= decrement
        return (f"La voiture freine de {decrement} km/h, "
                f"vitesse: {self.vitesse} km/h")


class Electrique(Vehicule):
    def __init__(self, marque, modele, vitesse, autonomie):
        super().__init__(marque, modele, vitesse)
        self.autonomie = autonomie


class Thermique(Vehicule):
    def __init__(self, marque, modele, vitesse, carburant):
        super().__init__(marque, modele, vitesse)
        self.carburant = carburant


class Voiture(Thermique):
    def __init__(self, marque, modele, vitesse, carburant, nbr_portes):
        super().__init__(marque, modele, vitesse, carburant)
        self.nbr_portes = nbr_portes


class Scooter_T(Thermique):
    def __init__(self, marque, modele, vitesse, carburant, nbr_roues):
        super().__init__(marque, modele, vitesse, carburant)
        self.nbr_roues = nbr_roues


class Voiture_E(Electrique):
    def __init__(self, marque, modele, vitesse, autonomie, nbr_portes):
        super().__init__(marque, modele, vitesse, autonomie)
        self.nbr_portes = nbr_portes


class Scooter(Electrique):
    def __init__(self, marque, modele, vitesse, autonomie, nbr_roues):
        super().__init__(marque, modele, vitesse, autonomie)
        self.nbr_roues = nbr_roues
