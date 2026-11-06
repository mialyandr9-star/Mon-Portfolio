class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
    def afficher_solde(self):
        print(f"titulaire : {self.titulaire}")
        print(f"solde : {self.solde} Ar")
        
        
class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde, taux_interet):
        super().__init__(titulaire, solde)
        self.taux_interet = taux_interet
    def afficher_solde(self):
        super().afficher_solde()
        print("Taux_interet :", self.taux_interet, "%")

        
# Creation un objet de la classe CompteEpargne avec les informations suivantes :
compte__miora = CompteEpargne("Miora", 500000, "5") 
 
# Appeler la methode afficher_solde()
compte__miora.afficher_solde()      