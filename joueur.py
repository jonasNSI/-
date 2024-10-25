class Joueur:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rockets = []

    def move(self, event):
        c = event.char
        print(c)
        if c == 'q' or c == 'Q':
            self.x = self.x - 10
        elif c == 'm' or c == 'M':
            self.x = self.x + 10
        elif c == 'x' or c == 'X':
            print("Shoot !!")

    def dessine(self, canevas):
        # Dessine le vaisseau du joueur sur un canevas passé en paramètre
        canevas.create_rectangle(self.x, self.y, self.x+20, self.y+10, outline="#aaa", fill="#fb0")

