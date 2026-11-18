class Apprenant:
    def __init__(self, nom, identifiant):
        self.nom = nom
        self.identifiant = identifiant
        self.modules = []
        
    def inscrire(self, module):
        self.modules.append(module)
        
        
    def afficher_module(self):
        print(f"Nom:", self.nom)
        print(f"Identifiant:", self.identifiant)
        print(f"Module suivis :")
        for module in self.modules:
            print(module.titre, module.nombre_heures, "heures")
        
             
class Module:
    def __init__(self, titre, nombre_heures):
        self.titre = titre 
        self.nombre_heures = nombre_heures
        
    def afficher_modules():
        for apprenant in self.apprenant:
            apprenant.afficher_details()
            
# Creation des apprenants et des modules
apprenant1 = Apprenant("Stela", "A1")
apprenant2 = Apprenant("Sonia", "A2")


module1 = Module("Couture", 20)
module2 = Module("Informatique", 15)
module3 = Module("coiffure", 10)

# Inscrire de chaque  apprenants 
apprenant1.inscrire(module1)
apprenant1.inscrire(module2)

apprenant2.inscrire(module1)
apprenant2.inscrire(module3)

# Afficher les inscriptions 
print("Apprenant1")
apprenant1.afficher_module()
print("Apprenant2")
apprenant2.afficher_module()
       