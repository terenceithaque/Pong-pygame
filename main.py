# Programme principal du jeu
import pygame  # Importation du module Pygame
from pygame.sprite import Group, spritecollide
from joueur import *
from adversaire import *
from balle import *
from collision import *
pygame.init()  # Initialiser Pygame
pygame.display.init()
pygame.mixer.init

window = pygame.display.set_mode((800, 600))  # Créer une fenêtre de jeu
pygame.display.set_caption("Pong !")

musique = "Sons/musique/The Coasters Sh Boom Life Could Be A Dream-jEP224Sa4Rw.mp3"
pygame.mixer.music.load(musique)
pygame.mixer.music.play(-1)

joueur_x = 700  # Position x du joueur
joueur_y = 250  # Position y du joueur
joueur = Joueur(joueur_x, joueur_y)
# print("score lu :", joueur.getScore())
# pygame.time.wait(1500)

advesaire_x = 100  # Position x de l'adversaire
advesaire_y = 250  # Position y de l'adversaire
adversaire = Adversaire(advesaire_x, advesaire_y)

groupe_joueur = Group()
groupe_adversaire = Group()

groupe_joueur.add(joueur)
groupe_adversaire.add(adversaire)


balle = Balle(400, 300, window)

is_running = True  # Est-ce que le jeu est en cours d'exécution ?

while is_running:  # Tant que le jeu est exécuté
    for evenement in pygame.event.get():  # Pour chaque évènement intercepté
        if evenement == pygame.QUIT:  # Si cet évènement est "quitter Pygame"
            is_running = False  # Le jeu n'est plus exécuté

    window.fill((0, 0, 0))

    key = pygame.key.get_pressed()  # Détecter les touches pressées par le joueur

    joueur.update(key)

    adversaire.update(balle.rect)

    collision = verifier_collision(balle, joueur, adversaire)
    print("Collision :", collision)
    # pygame.time.wait(1500)
    if collision == "joueur":  # Si la balle rentre en collision avec le joueur
        print("Entrée en collision avec le joueur")
        balle.update(sens=1, collision=collision)
        joueur.updateScore(montant=1)  # Augmenter le score du joueur de 1
        print("score :", joueur.score)
        joueur.saveScore()
       # pygame.time.wait(1000)

    elif collision == "adversaire":
        print("Entrée en collision avec l'adversaire")
        balle.update(sens=0, collision=collision)

    else:

        balle.update(sens=0, collision=collision)

    balle.draw()  # Dessiner la balle du jeu

    # Dessiner le joueur à l'écran
    pygame.draw.rect(window, joueur.couleur, joueur)
    joueur.displayScore(window)

    # Dessiner l'adversaire à l'écran
    pygame.draw.rect(window, adversaire.couleur, adversaire)

    pygame.display.flip()
