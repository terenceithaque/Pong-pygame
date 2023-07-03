# Programme principal du jeu
import pygame  # Importation du module Pygame
from joueur import *
pygame.init()  # Initialiser Pygame
pygame.display.init()

window = pygame.display.set_mode((800, 600))  # Créer une fenêtre de jeu
pygame.display.set_caption("Pong !")

is_running = True  # Est-ce que le jeu est en cours d'exécution ?

while is_running:  # Tant que le jeu est exécuté
    for evenement in pygame.event.get():  # Pour chaque évènement intercepté
        if evenement == pygame.QUIT:  # Si cet évènement est "quitter Pygame"
            is_running = False  # Le jeu n'est plus exécuté