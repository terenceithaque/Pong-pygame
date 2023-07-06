# Balle du jeu
import pygame


class Balle(pygame.sprite.Sprite):
    "Objet représentant une balle"

    def __init__(self, x, y, surface):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.surface = surface
        self.couleur = (255, 255, 255)
        self.vx = 3  # Vitesse horizontale de la balle
        self.vy = 3  # Vitesse verticale de la balle
        self.hit = False  # La balle est elle en collision avec le joueur ou l'adversaire ?

    def draw(self):
        "Dessiner la balle dans la fenêtre de jeu"
        pygame.draw.circle(self.surface, self.couleur,
                           self.rect.center, self.rect.width // 2)

    def update(self, sens, collision):
        # Mettre à jour la position et le comportement de la balle
        if collision == "joueur":
            # Inveser la direction de la balle
            self.vx *= -1
        elif collision == "adversaire":
            # Inverser la direction de la balle
            self.vx *= -1
        else:
            # Pas de collision, la balle continue d'avancer dans la direction actuelle
            pass

        # Mettre à jour la position de la balle en fonction de la direction
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Vérifier les collisions avec les bords de la fenêtre et changer la direction de la balle si besoin
        if self.rect.left < 0 or self.rect.right > self.surface.get_width():
            self.vx *= -1
        if self.rect.top < 0 or self.rect.bottom > self.surface.get_height():
            self.vy *= -1

   # print("Position de la balle :", self.rect.x)

    def reset_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
