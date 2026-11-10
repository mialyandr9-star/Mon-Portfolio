class Moteur:
    def __init__(self, marque, puissance):
        self.marque = marque
        self.puissance = puissance
        
    def demarrer():
        print(f"Le moteur demarre")
        
        
class Voiture:
    def __init__(self, moteur):
        self.moteur = moteur
        
    def demarrer(self):
        print(f"La voiture demarre")
        
# Creer un objet
moteur = Moteur("Rolls" ,400) 
voiture = Voiture(moteur)
voiture.demarrer()