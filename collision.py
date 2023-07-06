# Script pour vérifier la collision entre la balle, le joueur, ou l'adversaire
import pygame
from pygame.sprite import spritecollide


def verifier_collision(balle, joueur, adversaire):
    "Vérifier s'il y a une collision entre la balle, le joueur ou l'adversaire"
    if spritecollide(balle, [joueur], False):
        # pygame.time.wait(100)
        return "joueur"
    elif spritecollide(balle, [adversaire], False):
       # pygame.time.wait(100)
        return "adversaire"
