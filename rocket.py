from joueur import Joueur
class Rocket:
    def __init__ (self, x , y) :
        self.x = x
        self.y = y

    def dessine (self,canevas) :
        canevas.create_rectangle(self.x, self.y, self.x+5, self.y+5, outline="#aaa", fill="#fb0")

#= Rocket(joueur.x,joueur.y)