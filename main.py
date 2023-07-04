# Programme principal du jeu
import pygame  # Importation du module Pygame
from joueur import *
from adversaire import *
pygame.init()  # Initialiser Pygame
pygame.display.init()

window = pygame.display.set_mode((800, 600))  # Créer une fenêtre de jeu
pygame.display.set_caption("Pong !")

joueur_x = 700  # Position x du joueur
joueur_y = 250  # Position y du joueur
joueur = Joueur(joueur_x, joueur_y)

advesaire_x = 100  # Position x de l'adversaire
advesaire_y = 250  # Position y de l'adversaire
adversaire = Adversaire(advesaire_x, advesaire_y)

is_running = True  # Est-ce que le jeu est en cours d'exécution ?

while is_running:  # Tant que le jeu est exécuté
    for evenement in pygame.event.get():  # Pour chaque évènement intercepté
        if evenement == pygame.QUIT:  # Si cet évènement est "quitter Pygame"
            is_running = False  # Le jeu n'est plus exécuté

    window.fill((0, 0, 0))

    key = pygame.key.get_pressed()  # Détecter les touches pressées par le joueur

    joueur.update(key)

    adversaire.update()

    # Dessiner le joueur à l'écran
    pygame.draw.rect(window, joueur.couleur, joueur)

    # Dessiner l'adversaire à l'écran
    pygame.draw.rect(window, adversaire.couleur, adversaire)

    pygame.display.flip()
