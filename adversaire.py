"Adversaire du joueur contrôlé par l'ordinateur"
import pygame
from random import randint


class Adversaire(pygame.sprite.Sprite):
    "Adversaire du joueur"

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 60))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.couleur = (255, 255, 255)  # Couleur d'affichage de l'adversaire

    def update(self):
        "Mettre à jour la position de l'adversaire"
        self.y = randint(-5, 5)  # Choisir un nombre entre -5 et 5
        self.rect.y += self.y

        if self.rect.y < 0:
            self.rect.y = 0

        elif self.rect.y > 500:
            self.rect.y = 500
