class Livre:
    def __init__(self, titre, auteur, annee ):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        
    def affiche_details(self):
        print(f"{self.titre} : {self.auteur} :{self.annee}")
        
        
class Bibliotheque:
    def __init__(self, titre):
        self.titre = titre
        
    def ajouter_livre(self):
        print(f"{self.titre.livre}")
        
    def afficher_catalogue(self):
        print(f" {self.titre.livre} : {self.auteur} : {self.annee} ")
        
# Creation des objets livres
print("afficher_catalogue complet")
livre = Livre = "Onjam_pilafila"
auteur = Auteur = "IPA"
annee = Annee = 2001


# Affiche le catalogue complet
print("titre: Onjam_pilafila")
print("auteur: IPA")
print("annee: 2001")
