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

    def update(self, key):
        "Mettre à jour la position de la raquette du joueur"
        if key[pygame.K_UP]:
            self.rect.y -= 5
            print(self.rect.y)
            pygame.time.wait(2)

            if self.rect.y < 15:
                self.rect.y = 15

        if key[pygame.K_DOWN]:
            self.rect.y += 5
            print(self.rect.y)
            pygame.time.wait(2)

            if self.rect.y > 500:
                self.rect.y = 500
