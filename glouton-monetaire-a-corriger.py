# Algorithme glouton de résolution de monnaie à rendre
# A CORRIGER
# NF.NSI

# montant de la monnaie a rendre
montant = 1.65
# valeur des pieces disponibles en euro trié dans l'ordre croissant
pieces = [ 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 ]

## exemple de cas non optimal
## montant = 21
## pieces = [ 18, 7, 1 ]

def Monnaie(somme,ListeMontants) :
    ListeNbPieces=[0 for x in ListeMontants]
    for k in range(len(ListeMontants)) :
    	ListeNbPieces[k]=somme//ListeMontants[k]
    	somme%=ListeMontants[k]
    return somme,ListeNbPieces

print(Monnaie(montant, pieces))
