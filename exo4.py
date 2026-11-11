class Formation:
    def __init__(self, intitule, duree):
        self.intitule = intitule
        self.duree = duree
        
class Etudiant:
    def __init__(self, nom, age, formation):
        self.nom = nom 
        self.age = age
        self.formation = formation
        
    def afficher_information(self):
        print(f"nom :{self.nom}")
        print(f"age :{self.age}")
        print(f"formation :{self.formation}")
    
        

# Creation d'un objet
formation1 = Formation("hotellerie", 24)

# Creation formation
etudiant1 = Etudiant("Pounie", 25, "formation1")
etudiant2 = Etudiant("Aicha", 22, "formation1")

# Afficher chaque information des etudiants:
print("Etudiant1")
etudiant1.afficher_information()
print("Etudiant2")
etudiant2.afficher_information()




        
        