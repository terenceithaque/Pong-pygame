"Contient les éléments qui concernent le joueur."
import pygame  # Importer Pygame


class Joueur(pygame.sprite.Sprite):
    "Raquette contrôlée par le joueur"

    def __init__(self, x, y):
        super().__init__()
        # Image qui représente le joueur
        self.image = pygame.Surface((10, 60))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.couleur = (255, 255, 255)  # Couleur d'affichage du joueur

    def update(self):
        "Mettre à jour la position de la raquette du joueur"
        pass
