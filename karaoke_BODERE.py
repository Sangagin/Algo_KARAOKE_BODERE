

class Player:
    
    #constructeur
    
    def __init__(self, nom):
        self.name = nom
        self.score = [0,0,0,0,00]

        
        
    
    def getName(self):
        return self.name
    
    def getScore(self):
        return self.score

    
    
    
    def calculerMoyenne(self):
        accumul=0
        for i in range (0,len(self.score)):
            accumul+=self.score[i]
            
        moyenne = accumul/len(self.score)
        print("Votre moyenne est de " + str(moyenne))
        
        
    def afficherScoreTotal(self):
        accumul=0
        for i in range (0,len(self.score)):
            accumul+=self.score[i]
            
        print("Votre score total est de " + str(accumul))
        
        
    def afficherMeilleurChanson(self):
        best=0
        for i in range (0,len(self.score)):
            if(best<=self.score[i]):
                best=self.score[i]
                pos=i
                
        print("La meilleur chanson est la " + str(pos+1) + " avec un score de " + str(best))
    
    
    def afficherPireChanson(self):
        worst=9999
        for i in range (0,len(self.score)):
            if(worst>=self.score[i]):
                worst=self.score[i]
                pos=i
                
        print("La pire chanson est la " + str(pos+1) + " avec un score de " + str(worst))

    def ajouterScore(self,pos,nouvScore):
        if(nouvScore>self.score[pos]):
            self.score[pos]=nouvScore    
            
    def afficherScores(self):
        print("Vos scores sont de :")
        for i in range (0,len(self.score)):
            print(self.score[i])

    
 
        
        
        
        
      
        
bob = Player("bob") 


bob.calculerMoyenne()
bob.afficherScoreTotal()
bob.afficherMeilleurChanson()
bob.afficherPireChanson()


bob.afficherScores()


bob.ajouterScore(0,50)
bob.afficherScores()
bob.calculerMoyenne()

bob.ajouterScore(1,60)
bob.ajouterScore(2,65)
bob.ajouterScore(3,100)
bob.ajouterScore(4,55)

bob.afficherMeilleurChanson()
bob.afficherPireChanson()