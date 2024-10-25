from tkinter import *
from random import randint
from joueur import Joueur
from ennemi import Ennemi
from rocket import Rocket

class Game:
    def __init__(self):
        self.ennemis = [] # tableau des envahisseurs

        self.fen = Tk() # fenêtre de jeu
        self.fen.title('Envahisseurs') # titre de la fenêtre
        self.can = Canvas(self.fen, width = 1024, height = 768, background='black') # canevas de dessin
        self.can.pack()

        # instanciation du joueur ( position initiale x = 550 / y = 700 )
        self.joueur = Joueur(550, 700)

        self.fen.bind("<Key>", self.joueur.move) # gestion des déplacements clavier du joueur

        # instanciation des ennemis ( 3 rangées de 10, de taille 50 x 50 initialement en haut de l'écran)
        for i in range (3) :
            for j in range (10) :
                self.ennemis.append(Ennemi(60+j*90,60+i*90,50))

        self.rocket = Rocket(self.joueur.x, self.joueur.y)


        self.run() # lancement du jeu

        self.fen.mainloop() # boucle principale d'évènements Tkinter

    def run(self):
        # EFFACEMENT GENERAL
        self.can.delete('all')

        # AFFICHAGE DU VAISSEAU DU JOUEUR
        #self.can.create_rectangle(self.joueur.x, self.joueur.y, self.joueur.x+20, self.joueur.y+10, outline="#aaa", fill="#fb0")
        self.joueur.dessine(self.can)

        # DEPLACEMENT DES ROCKETS TIREES PAR LE JOUEUR
        for rocket in (self.joueur.rocket) :  # parcours du tableau des rockets déja tirées par le joueur

            rocket.dessine(self.can) # affichage de la roquette
        #    ... # déplacement de la roquette
        #    if (...): # si la roquette a atteint le haut de l'écran
        #        ... # on la supprime du tableau des roquettes

        #    for ennemi in ... : # parcours du tableau des ennemis encore en jeu
        #        if ... : # la rocket touche-t-elle l'ennemi ( destruction mutuelle ) ?
        #            ... # si oui, on retire l'ennemi du tableau des ennemis
        #            ... # et on retire la roquette du tableau des roquettes

        # DEPLACEMENT DES ENNEMIS, LARGAGE EVENTUEL D'UNE BOMBE, MOUVEMENT DES BOMBES DEJA LACHÉES PAR CHAQUE ENNEMI
        #for ennemi in self.ennemis : # parcours du tableau des ennemis
        #    ennemi.dessine(self.can) # affichage de l'ennemi
        #    ... # déplacement de l'ennemi
        #    if randint(1, 500) < 5: # larguage d'une bombe avec une probabilité de 5/500
        #        x, y = ... # coordonnées de l'ennemi
        #        ... # largage d'une bombe à partir de la position de l'ennemi ( un peu en dessous...)
        #    for bombe in ... : # pour chaque bombe déja larguée par l'ennemi
        #        ... # affichage de la bombe
        #        ... # déplacement de la bombe
        #        if (...): # si la bombe a atteint le bas de l'écran
        #            ... # on la supprime du tableau des bombes associé à l'ennemi

        #        if ... : # la bombe touche-t-elle le joueur ?
        #            self.fen.destroy() # et on ferme la fenêtre ( ou on affiche GAME OVER )

        self.fen.after(30,self.run) # boucle d'animation


# Corps du programme
g = Game()