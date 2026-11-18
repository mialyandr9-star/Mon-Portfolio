class Module:
    def __init__(self, titre, duree):
        self.titre = titre 
        self.duree = duree
        
class Formation:
    def __init__(self, intitule):
        self.intitule = intitule
        self.modules = []
        
    def ajouter_module(self, module):
        self.modules.append(module)
        
class Apprenant:
    def __init__(self, nom):
        self.nom = nom
        self.formations = []
        
    def s_inscrire(self, formation):
        self.formations.append(formation)
        
    def afficher_parcours(self):
        print(f"Apprenant", self.nom)
        for formation in self.formations:
          print(f"Formation, formation.intitule")
        for module in formation.modules:
          print(module.titre, module.duree, "heures")
          
          
# Creation des formations
formation1 = Formation("Web")
formation2 = Formation("Informatique")

# Creation des modules
module1 = Module("HTML", 15)
module2 = Module("CSS", 20)
module3 = Module("JavaScript", 25)
module4 = Module("Bureautique", 10)
module5 = Module("Python", 20)
module6 = Module("Reseaux", 8)

# Ajout des modules aux formations
formation1.ajouter_module(module1)
formation1.ajouter_module(module2)
formation1.ajouter_module(module3)


formation2.ajouter_module(module4)
formation2.ajouter_module(module5)
formation2.ajouter_module(module6)

# Creation des apprenants
apprenant1 = Apprenant("Bila")
apprenant2 = Apprenant("Gonna")

# Inscription
apprenant1.s_inscrire(formation1)
apprenant1.s_inscrire(formation2)
apprenant2.s_inscrire(formation2)

# Affichage des parcours des apprenants
apprenant1.afficher_parcours()
apprenant2.afficher_parcours()
        
          