"Adversaire du joueur contrôlé par l'ordinateur"
import pygame
from random import randint
import random


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

    def update(self, rect_balle):
        "Mettre à jour la position de l'adversaire"

        if random.random() < 0.6:  # 60 % de chances d'attraper la balle
            # Si la position y de l'adversaire est inférieure à la position y de la balle
            if self.rect.centery < rect_balle.centery:
                self.rect.y += 5  # Ajouter 5 à la position y de l'adversaire

            # Si la position y de l'adversaire est supérieure à la position y de la balle
            elif self.rect.centery > rect_balle.centery:
                self.rect.y -= 5

        if self.rect.y < 0:
            self.rect.y = 0

        elif self.rect.y > 500:
            self.rect.y = 500
