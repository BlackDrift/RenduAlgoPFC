import random
tableElements = ["Pierre", "Feuille", "Ciseau"]
cercleCombat={"Pierre" : "Ciseau", "Feuille" : "Pierre", "Ciseau" : "Feuille"}

def pierreFeuilleCiseau():
    choixJoueur = tableElements[int(input("Choisissez un nombre entre 0 et 2 : "))]
    choixAdversaire = tableElements[random.randint(0,2)]
    if choixJoueur==choixAdversaire :
        return "Draw !"
    else :
        if choixAdversaire == cercleCombat[choixJoueur]:
            return "Win !"
        else :
            return "Lost... !"


print(pierreFeuilleCiseau())