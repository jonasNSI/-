class Ennemi:
    def __init__ (self, x, y, taille) :
        self.x = x
        self.y = y
        self.taille = taille


    def dessine (self, canevas) :
        canevas.create_rectangle(self.x, self.y, self.x + 50, self.y + 35, outline="yellow", fill="red")

    def move (self) :
        self.y = 0.3