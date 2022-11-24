import random  #importation de la bibiliothèque random 
class TicTacToe (object):  #création de la class TicTacToe de type object 

    def __init__(self,secondPlayer=False): #surcharge de la méthode constructeur __init__
        self.gamePlate=[]
        if secondPlayer :  #s'il y a un second joueur
            self._iaMode = False   #Pas de présence d'une IA
        else : #sinon, il n'y a qu'un seul joueur
            self._iaMode = True #on indique la présence d'une IA
            self.AIExtreme = ExtremeIA(self) #activation du mode extrême (l'IA doit gagner strictement ou égaliser le match)      
        self._pointOwner = "X"
        self.takenCoords=[]   #on définit self.takenCoords qui enregistre les coordonées prises durant la partie 

    def affiche(self,content):  #affichage du tableau de jeu
        for i in range(len(content)):
            contentLine = ""
            for j in range(len(content)):
                contentLine += content[i][j]
                contentLine += (" | ")
            print(contentLine)  

    
    def ticTacToeStart(self):   #Création du tableau 
        for i in range(3):
            self.gamePlate.append([])
            for _ in range (3) :
                self.gamePlate[i].append("*") #caractère montrant la case n                                                                                                                     on choisi auparavant
        self.affiche(self.gamePlate) 
        
    
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

    #"""def botTurn(self) :   #Les actions à faire du bot
        botRowCoord=random.randint(0,2)   #le robot choisi une coordonnée horizontale aléatoire
        botColCoord=random.randint(0,2)   #le robot choisi une coordonnée verticale aléatoire
        return (botRowCoord, botColCoord) #retourne la ligne et la colonne du point"""

    def playerWin(self, player):
        win = None
        length = len(self.gamePlate)
        # on vérifie les lignes
        for i in range(length):
            win = True
            for j in range(length):
                if self.gamePlate[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # on vérifie les colonnes
        for i in range(length):
            win = True
            for j in range(length):
                if self.gamePlate[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # on vérifie les diagonales
        win = True
        for i in range(length):
            if self.gamePlate[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(length):
            if self.gamePlate[i][length - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

    def swapTurn(self, player):
        return 'X' if player == 'O' else 'O'
    
    def filledGamePlate(self):
        filled = True
        for i in range (len(self.gamePlate)) :
            for j in range (len(self.gamePlate)) :
                if self.gamePlate[i][j] == "*" :
                    filled = False
                    break
        if filled:
            return filled
        return False
        

    def ticTacToeGame(self):    #Le jeu commence 
        continuing=True   
        if self._iaMode :
            while continuing : #tant que personne ne gagne
                  
                self._playerCoords=self.playerTurn()
                if self.gamePlate[self._playerCoords[0]][self._playerCoords[1]] != "*" and self._playerCoords in self.takenCoords:
                    print("You cannot pick this used space... try again")
                    self._playerCoords=self.playerTurn()
                else :
                    self.takenCoords.append(self._playerCoords)
                
                self.gamePlate[self._playerCoords[0]].insert(self._playerCoords[1],"X")    
                self.gamePlate[self._playerCoords[0]].pop(self._playerCoords[1]+1)
                self.affiche(self.gamePlate)
                
                if self.playerWin(self._pointOwner) :
                        continuing = False
                        self.win(self._pointOwner)
                        break
                self._pointOwner = self.swapTurn(self._pointOwner)

                self._botCoords=self.AIExtreme.botTurn()
                while self.gamePlate[self._botCoords[0]][self._botCoords[1]] != "*" and not self.filledGamePlate():
                    self._botCoords=self.AIExtreme.botTurn()
                self.takenCoords.append(self._botCoords)
                
                print("AI played ",(self._botCoords[0]+1,self._botCoords[1]+1))
                
                self.gamePlate[self._botCoords[0]].insert(self._botCoords[1],"O")
                self.gamePlate[self._botCoords[0]].pop(self._botCoords[1]+1)
                self.affiche(self.gamePlate)
                 
                if self.playerWin(self._pointOwner) :
                    continuing = False
                    self.win(self._pointOwner)
                    break
                self._pointOwner = self.swapTurn(self._pointOwner)
                
                if self.filledGamePlate() :                                  
                    continuing = False
                    self.draw()
                    break
                
        else :
            while continuing :
            
                self._firstPlayerCoords=self.playerTurn()
                if self.gamePlate[self._firstPlayerCoords[0]][self._firstPlayerCoords[1]] != "*" and self._firstPlayerCoords in self.takenCoords:
                    print("You cannot pick this used space... try again")
                    self._firstPlayerCoords=self.playerTurn()
                else :
                    self.takenCoords.append(self._firstPlayerCoords)

                self.gamePlate[self._firstPlayerCoords[0]].insert(self._firstPlayerCoords[1],self._pointOwner)    
                self.gamePlate[self._firstPlayerCoords[0]].pop(self._firstPlayerCoords[1]+1)
                self.affiche(self.gamePlate)
                
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
                if self.gamePlate[self._secondPlayerCoords[0]][self._secondPlayerCoords[1]] != "*" and self._secondPlayerCoords in self.takenCoords:
                    print("You cannot pick this used space... try again")
                    self._secondPlayerCoords=self.playerTurn()
                else :
                    self.takenCoords.append(self._secondPlayerCoords)
            
                self.gamePlate[self._secondPlayerCoords[0]].insert(self._secondPlayerCoords[1],self._pointOwner)    
                self.gamePlate[self._secondPlayerCoords[0]].pop(self._secondPlayerCoords[1]+1)
                self.affiche(self.gamePlate)
                
                if self.playerWin(self._pointOwner) :
                    continuing = False
                    self.win(self._pointOwner)
                    break
                
                                                                             

                self._pointOwner = self.swapTurn(self._pointOwner)
                
                
class ExtremeIA(object) :

    def __init__(self,game:TicTacToe) :
        self.AICoords = []
        self.PlayerCoords = []
        self.game = game
        self.gameTab = game.gamePlate
        self.turnOne = True
        
    
    def rowCheck(self,player):  #On définit la méthodes rowCheck qui vérifieras
        length = len(self.gameTab)
        count = 0
        for i in range(length):
            for j in range(length):
                if self.gameTab[i][j] == player:
                    count = count + 1   
                if count ==2 and "*" in self.gameTab[i]:
                    emptyPlace = self.gameTab[i].index("*")
                    return (i,emptyPlace)
            count = 0
        return None

    def colCheck(self,player):   #On définit la méthode colCheck qui vérifieras les colonnes
        length = len(self.gameTab)
        count = 0
        for i in range(length):
            column = []
            for x in range (length) :
                column.append(self.gameTab[x][i])
            for j in range(length) :
                if column[j] == player :
                    count = count + 1
                if count ==2 and "*" in column:
                    emptyPlace = column.index("*")
                    return (emptyPlace,i)
            count = 0
        return None

    def diagonalCheck(self,player):  #On définit la méthode diagonalCheck qui vérfieras les diagonales
        length = len(self.gameTab)
        firstDiagonal = []
        secondDiagonal = []
        for x in range(length):
            firstDiagonal.append(((self.gameTab[x][x],(x,x))))   #première diagonale
            secondDiagonal.append(((self.gameTab[x][length - 1 - x]),(x,length-1-x)))   #deuxième diagonale
        count = 0
        for i in range(length): 
            if firstDiagonal[i][0] == player :
                count = count + 1
            if count == 2 :
                for z in range(length) :
                    if firstDiagonal[z][0] == "*" :
                        return firstDiagonal[z][1]
        count = 0
        for j in range(length):
            if secondDiagonal[j][0] == player :
                count = count + 1
            if count==2 :
                for z in range (length):
                    if secondDiagonal[z][0] == "*" :
                        return secondDiagonal[z][1]
        return None

    def botTurn(self)->tuple:
        coordsPlayed = self.game.takenCoords
        temp = None
        self.PlayerCoords.append(coordsPlayed[-1])   
        while self.turnOne :
            for i in range(len(coordsPlayed)):
                if coordsPlayed[i] not in self.AICoords or coordsPlayed[i] not in self.PlayerCoords:
                    self.PlayerCoords.append(coordsPlayed[i])
                    temp=coordsPlayed[i]
                if temp == (0,0) or temp == (0,2) or temp == (2,0) or temp == (2,2):
                    self.AICoords.append((1,1))
                    self.turnOne=False
                    return self.AICoords[-1]
                elif temp[0]==0:
                    self.AICoords.append((temp[0]+2,temp[1]))
                    self.turnOne=False
                    return self.AICoords[-1]
                elif temp[0]==2:
                    self.AICoords.append((temp[0]-2,temp[1]))
                    self.turnOne=False               
                    return self.AICoords[-1]
                elif temp[1]==0:
                    self.AICoords.append((temp[0],temp[1]+2))
                    self.turnOne=False               
                    return self.AICoords[-1]
                elif temp[1]==2:
                    self.AICoords.append((temp[0],temp[1]-2))
                    self.turnOne=False               
                    return self.AICoords[-1]
                elif temp == (1,1) :
                    x = random.randrange(0,2,2)
                    y = random.randrange(0,2,2)
                    self.AICoords.append((x,y))
                    self.turnOne=False
                    return self.AICoords[-1]
        temp = []
        tempATK = []
        if self.rowCheck("X") != None and self.rowCheck("X") not in temp :
            temp.append(self.rowCheck("X"))
        if self.colCheck("X") != None and self.colCheck("X") not in temp :     
            temp.append(self.colCheck("X"))
        if self.diagonalCheck("X") != None and self.diagonalCheck("X") not in temp :
            temp.append(self.diagonalCheck("X"))
        
        if self.rowCheck("O") != None and self.rowCheck("O") not in tempATK :
            tempATK.append(self.rowCheck("O"))
        if self.colCheck("O") != None and self.colCheck("O") not in tempATK :     
            tempATK.append(self.colCheck())
        if self.diagonalCheck("O") != None and self.diagonalCheck("O") not in tempATK :
            tempATK.append(self.diagonalCheck("O"))
        
        if len(tempATK) >= 1 :
            if len(tempATK) > 1 :
                x = random.randint(0,len(tempATK))
                self.AICoords.append(tempATK[x])
            elif len(tempATK) == 1 :
                self.AICoords += tempATK   
            elif tempATK == [] and not self.game.filledGamePlate() :
                AICoords = (random.randint(0,2),random.randint(0,2))
                self.AICoords.append(AICoords)
        else :
            if len(temp) > 1 :
                x = random.randint(0,len(temp))
                self.AICoords.append(temp[x])
            elif len(temp) == 1 :
                self.AICoords += temp   
            elif temp == [] and not self.game.filledGamePlate() :
                AICoords = (random.randint(0,2),random.randint(0,2))
                self.AICoords.append(AICoords)
        
        #print(temp)
        return self.AICoords[-1]
        
            

               

game=TicTacToe()
game.ticTacToeStart()
game.ticTacToeGame()



