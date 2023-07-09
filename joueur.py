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
        # Fichier où le score du joueur est enregistré
        self.fichier_score = "score_joueur.txt"

        self.score = 0  # Score actuel du joueur

        self.best_score = self.getScore()  # Obtenir le meilleur score du joueur
        self.score_font = pygame.font.Font(None, 36)
        self.best_score_font = pygame.font.Font(None, 36)

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

    def checkScore(self):
        "Vérifier si le meilleur score est inférieur au score actuel"
        if self.best_score < self.score:
            self.best_score = self.score

    def updateScore(self, montant):
        "Mettre à jour le score du joueur"
        self.score += montant
        self.checkScore()
        return self.score

    def saveScore(self):
        "Sauvegarder le score du joueur"
        if self.score >= self.best_score:  # Si le score actuel est supérieur ou égal  au meilleur score
            # Ouvrir le fichier "score_joueur.txt" en écriture. wf = write file
            with open(self.fichier_score, "w") as wf:
                # Ecrire le score du joueur sous la forme d'une chaîne de caractères
                wf.write(str(self.score))
                wf.close()  # Fermer le fichier une fois l'écriture du score finie

        elif self.best_score > self.score:  # Si le meilleur score est supérieur au score actuel
            # Ouvrir le fichier "score_joueur.txt" en écriture. wf = write file
            with open(self.fichier_score, "w") as wf:
                # Ecrire le meilleur score sous la forme d'une chaîne de caractères
                wf.write(str(self.best_score))
                wf.close()  # Fermer le fichier une fois l'écriture du meilleur score finie

    def getScore(self):
        "Obtenir le score du joueur enregistré dans un fichier texte"
        # Ouvrir le fichier "score_joueur.txt" en lecture. rf = read file
        with open(self.fichier_score, "r") as rf:
            score_lu = int(rf.read())  # Score lu dans le fichier
            rf.close()  # Fermer le fichier une fois la lecture du score finie
            return score_lu

    def displayScore(self, screen):
        "Afficher le score du joueur à l'écran"
        # score = str(self.score)

        # str_score = "Score : {}".format(score)
        score = "Score : {}".format(self.score)
        afficher_score = self.score_font.render(
            score, True, pygame.Color("white"))

        screen.blit(afficher_score, (650, 560))

        if self.best_score == self.score:
            # best_score = str(self.best_score)
            # str_best_score = "Meilleur : {}".format(best_score)
            meilleur_score = "Meilleur :{}".format(self.best_score)

            afficher_meilleur_score = self.best_score_font.render(
                meilleur_score, True, pygame.Color("white"))

            screen.blit(afficher_meilleur_score, (650, 510))
