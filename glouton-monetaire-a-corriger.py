# Algorithme glouton de résolution de monnaie à rendre
# A CORRIGER
# NF.NSI

# montant de la monnaie a rendre
#montant = 1.65
# valeur des pieces disponibles en euro trié dans l'ordre croissant
#pieces = [ 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 ]

## exemple de cas non optimal
montant = 21
pieces = [ 18, 7, 1 ]

def giveBack_nonoptimised(giveBack,moneySystem) :
    solution=[0 for x in moneySystem]
    for k in range(len(moneySystem)) :
    	solution[k]=giveBack//moneySystem[k]
    	giveBack = round(giveBack%moneySystem[k], 2)
    return giveBack,solution

def giveBack_optimised(giveBack, moneySystem):
    giveBack = giveBack
    solution=[]
    for money in moneySystem:
        if money <= giveBack:
            solution.append(money)
            giveBack -= money

    return round(giveBack, 2), solution

print(giveBack_nonoptimised(montant, pieces))
print(giveBack_optimised(montant, pieces))
