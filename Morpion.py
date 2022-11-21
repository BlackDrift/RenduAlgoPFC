import random  #importation de la bibiliothèque random 
class TicTacToe (object):  #création de la class TicTacToe de type object 

    def __init__(self,secondPlayer=False): #surcharge de la méthode constructeur __init__
        if secondPlayer :  #s'il y a un second joueur
            self._iaMode = False   #Pas de présence d'une IA
        else : #sinon, il n'y a qu'un seul joueur
            self._iaMode = True #on indique la présence d'une IA
        #self._winningCombos = [[(0,0),(0,1),(0,2)],[(0,0),(1,0),(2,0)],[(0,0),(1,1),(2,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],[(0,2),(1,1),(2,0)]]   #Les combos gagnants
        self._gamePlate=[]
        self._pointOwner = "X"

    def affiche(self,content):  #affichage du tableau de jeu
        for i in range(len(content)):
            contentLine = ""
            for j in range(len(content)):
                contentLine += content[i][j]
                contentLine += (" | ")
            print(contentLine)  

    
    def ticTacToeStart(self):   #Création du tableau 
        for i in range(3):
            self._gamePlate.append([])
            for _ in range (3) :
                self._gamePlate[i].append("*") #caractère montrant la case n                                                                                                                     on choisi auparavant
        self.affiche(self._gamePlate) 
        
    
    def win(self,pointOwner): #annonces des vainqueurs
        if self._iaMode :
            if pointOwner == "X" :
                print("Player Wins !")  #retourner le joueur  a gagné
            else :
                print("AI wins !") #retourner l'IA a gagné
        else :
            if pointOwner == "X" :
                print("Player 1 wins !")  #retourner le joueur 1 a gagné
            else :
                print("Player 2 wins !") #retourner le joueur 2 a gagné

    def draw(self):
        print("That's a draw !")   

    def playerTurn(self):   #Les actions à faire du joueur 
        rowCoord=int(input("Please select a row number between 1 and 3 : "))-1
        assert rowCoord >= 0 and rowCoord <=2, "You're supposed to have chosen a number between 1 and 3..."
        colCoord=int(input("Please select a column number between 1 and 3 : "))-1
        assert colCoord >= 0 and colCoord <=2, "You're supposed to have chosen a number between 1 and 3..."
        return (rowCoord, colCoord) #retoune la ligne et la colonne du point

    def botTurn(self) :   #Les actions à faire du bot
        botRowCoord=random.randint(0,2)   #le robot choisi une coordonnée horizontale aléatoire
        botColCoord=random.randint(0,2)   #le robot choisi une coordonnée verticale aléatoire
        return (botRowCoord, botColCoord) #retourne la ligne et la colonne du point

    def playerWin(self, player):
        win = None
        length = len(self._gamePlate)
        # on vérifie les lignes
        for i in range(length):
            win = True
            for j in range(length):
                if self._gamePlate[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # on vérifie les colonnes
        for i in range(length):
            win = True
            for j in range(length):
                if self._gamePlate[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # on vérifie les diagonales
        win = True
        for i in range(length):
            if self._gamePlate[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(length):
            if self._gamePlate[i][length - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def swapTurn(self, player):
        return 'X' if player == 'O' else 'O'
    
    def filledGamePlate(self):
        filled = True
        for i in range (len(self._gamePlate)) :
            for j in range (len(self._gamePlate)) :
                if self._gamePlate[i][j] == "*" :
                    filled = False
                    break
        if filled:
            return filled
        return False
        

    def ticTacToeGame(self):    #Le jeu commence 
        takenCoords=[]   #on définit takenCoords qui enregistre les coordonées prises durant la partie 
        continuing=True   
        if self._iaMode :
            while continuing : #tant que personne ne gagne
                  
                self._playerCoords=self.playerTurn()
                if self._gamePlate[self._playerCoords[0]][self._playerCoords[1]] != "*" and self._playerCoords in takenCoords:
                    print("You cannot pick this used space... try again")
                    self._playerCoords=self.playerTurn()
                else :
                    takenCoords.append(self._playerCoords)
                
                self._gamePlate[self._playerCoords[0]].insert(self._playerCoords[1],"X")    
                self._gamePlate[self._playerCoords[0]].pop(self._playerCoords[1]+1)
                self.affiche(self._gamePlate)
                
                if self.playerWin(self._pointOwner) :
                        continuing = False
                        self.win(self._pointOwner)
                        break
                self._pointOwner = self.swapTurn(self._pointOwner)

                self._botCoords=self.botTurn()
                while self._gamePlate[self._botCoords[0]][self._botCoords[1]] != "*" :
                    self._botCoords=self.botTurn()
                takenCoords.append(self._botCoords)
                
                print("AI played ",(self._botCoords[0]+1,self._botCoords[1]+1))
                
                self._gamePlate[self._botCoords[0]].insert(self._botCoords[1],"O")
                self._gamePlate[self._botCoords[0]].pop(self._botCoords[1]+1)
                self.affiche(self._gamePlate)
                 
                if self.playerWin(self._pointOwner) :
                    continuing = False
                    self.win(self._pointOwner)
                    break
                self._pointOwner = self.swapTurn(self._pointOwner)
                
                assert len(takenCoords) <= 9, "An internal error occured..."
                if self.filledGamePlate() :                                  
                    continuing = False
                    self.draw()
                    break
                
        else :
            while continuing :
            
                self._firstPlayerCoords=self.playerTurn()
                if self._gamePlate[self._firstPlayerCoords[0]][self._firstPlayerCoords[1]] != "*" and self._firstPlayerCoords in takenCoords:
                    print("You cannot pick this used space... try again")
                    self._firstPlayerCoords=self.playerTurn()
                else :
                    takenCoords.append(self._firstPlayerCoords)

                self._gamePlate[self._firstPlayerCoords[0]].insert(self._firstPlayerCoords[1],self._pointOwner)    
                self._gamePlate[self._firstPlayerCoords[0]].pop(self._firstPlayerCoords[1]+1)
                self.affiche(self._gamePlate)
                
                if self.playerWin(self._pointOwner) :
                    continuing = False
                    self.win(self._pointOwner)
                    break
                
                if self.filledGamePlate() :                                  
                    continuing = False
                    self.draw()
                    break

                self._pointOwner=self.swapTurn(self._pointOwner)

                
                self._secondPlayerCoords=self.playerTurn()
                if self._gamePlate[self._secondPlayerCoords[0]][self._secondPlayerCoords[1]] != "*" and self._secondPlayerCoords in takenCoords:
                    print("You cannot pick this used space... try again")
                    self._secondPlayerCoords=self.playerTurn()
                else :
                    takenCoords.append(self._secondPlayerCoords)
            
                self._gamePlate[self._secondPlayerCoords[0]].insert(self._secondPlayerCoords[1],self._pointOwner)    
                self._gamePlate[self._secondPlayerCoords[0]].pop(self._secondPlayerCoords[1]+1)
                self.affiche(self._gamePlate)
                
                if self.playerWin(self._pointOwner) :
                    continuing = False
                    self.win(self._pointOwner)
                    break
                
                if self.filledGamePlate() :                                  
                    continuing = False
                    self.draw()
                    break

                self._pointOwner = self.swapTurn(self._pointOwner)
                
                








game=TicTacToe()
game.ticTacToeStart()
game.ticTacToeGame()