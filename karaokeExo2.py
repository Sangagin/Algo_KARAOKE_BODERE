

class Player:
    
    #constructeur
    
    def __init__(self, nom,position):
        self.name = nom
        self.score = [0,0,10,0,20]
        self.position=position
        
        
    
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
            
       # print("Votre score total est de " + str(accumul))
        return accumul
        
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

    def ajouterScore(self,nouvScore,listChanson,chanson):
        if(nouvScore>listChanson[chanson][self.position]):
            listChanson[chanson][self.position]=nouvScore    
            
        
            
            
            
            
    def afficherScores(self):
        print("Vos scores sont de :")
        for i in range (0,len(self.score)):
            print(self.score[i])

    
 
        
    
    
    
class Karaoke:
    
     
    #constructeur
    
    def __init__(self, listMusiques, listJoueurs):
        self.listChansons = listMusiques
        self.listPlayer = listJoueurs
        
        
        
    def getListChansons(self):
        return self.listChansons
    
    def getlistPlayer(self):
        return self.listPlayer
    
        
    def ajouterPlayer(self, nouvplayer):
        self.listPlayer.append(nouvplayer)
        
    def retirerPlayer(self, playerParti):
        self.listPlayer.remove(playerParti) 
        

    def afficherBestScoreChanson(self, chanson):
        best=0
        for i in range (0,len(self.listChansons[chanson])):
            if(best<=self.listChansons[chanson][i]):
                best=self.listChansons[chanson][i]
                pos=i
                
        
        print("Le meilleur score sur la chanson demandée est de " + str(best))
        print("C'est le joueur " + self.listPlayer[pos].getName() + " qui le détient")
            
        
    def afficherMeilleurPlayer(self):
        best=0
        for i in range (0,len(self.listPlayer)):
            if (best<self.listPlayer[i].afficherScoreTotal()):
                best=self.listPlayer[i].afficherScoreTotal()
                pos=i
        print("le joueur avec le score total le plus haut est " + self.listPlayer[pos].getName())
                    
                    
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#dico des chansons, avec en clé un tableau des scores
#il faudrait créer la liste dans la class pour mettre le nombre correct de 0, mais pas le temps
listeChansons = {
    "Let it go" : [0,0,0],
    "Les Lacs du Connemara" : [0,0,0],
    "Les prisons de Nantes" : [0,0,0]
}

bob=Player("bob",0)
jean =Player("Jean",1)
henri=Player("Henri 4",2)
nouv=Player("le petit kevin",3)

listeChanteurs = [bob,jean,henri]
        
leBaracuda = Karaoke(listeChansons,listeChanteurs)



listActuelle = leBaracuda.getlistPlayer()

print ("Les joueurs actuels sont :")
for i in range (0,len(listActuelle)):
    print (listActuelle[i].getName())
    
leBaracuda.ajouterPlayer(nouv)

print("")
print("un nouveau joueur arrive !")
print ("Les joueurs actuels sont :")
for i in range (0,len(listActuelle)):
    print (listActuelle[i].getName())
    
print("")
print("en fait non, il ne reste pas")

leBaracuda.retirerPlayer(nouv)    
for i in range (0,len(listActuelle)):
    print (listActuelle[i].getName())
        
        

print("Les chansons disponibles sont :")
print(listeChansons)
        
print("Le joueur " + listActuelle[0].getName() + " va chanter !")

listActuelle[0].ajouterScore(55,listeChansons,"Let it go")


leBaracuda.afficherBestScoreChanson("Let it go")





