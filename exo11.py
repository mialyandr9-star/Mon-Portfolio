class Employe:
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base
        
    def calcule_salaire(self):
        return self.salaire_base
    
class Developpeur(Employe):
    def __init__(self, nom, salaire_base, prime_technique):
        super().__init__(nom, salaire_base)
        self.prime_technique = prime_technique
        
        
class Commercial(Employe):
    def __init__(self, nom, salaire_base, commission):
        super().__init__(nom, salaire_base)
        self.commission = commission
        
    def calculer_salaire(self):
        return self.salaire_base + self.commission
    
# Creation des 2 developpeur
dev1 = Developpeur("Soa", 1200000, 300000)
dev2 = Developpeur("Fara", 1500000, 300000 )


# Creation de 2 com
com1 = Commercial("Kate", 10000000, 250000)
com2 = Commercial("Bine", 20000000, 400000)

# Regroupement des employes
employes = [dev1, dev2, com1, com2]

for employe in employes:
    print("Employe:", employe.nom)
    print("Salaire:", employe.calculer_salaire(), "Ar")
    print()