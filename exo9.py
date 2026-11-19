class Transport:
    def se_deplacer(self):
        print("La transport se deplace.")
        
class Voiture(Transport):
    def se_deplacer(self):
        print("La voiture roule sur la route.")
        
class Avion(Transport):
    def se_deplacer(self):
        print("L'avion vole dans les airs.")
        
        
class Bateau(Transport):
    def se_deplacer(self):
        print("Le bateau navigue sur l'eau.")
        
voiture1 = Voiture()
avion1 = Avion()
bateau1 = Bateau()

transports = [voiture1, avion1, bateau1]

for transport in transports:
    transport.se_deplacer()
    