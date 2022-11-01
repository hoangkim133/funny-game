import sys
import pygame

class PlayerMain:
    def __init__(self, x_player, y_player):
        self.Player = pygame.image.load("img/space-shuttle.png")
        self.playerX = x_player
        self.playerY = y_player
        self.valueX = 0
        self.valueY = 0
        self.yPress = "None"
        self.checkBullet = False

    def buttonPlayer(self, bullet, i):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.valueX = -0.5
                if event.key == pygame.K_RIGHT:
                    self.valueX = 0.5
                if event.key == pygame.K_UP:
                    self.valueY = -0.5
                if event.key == pygame.K_DOWN:
                    self.valueY = 0.5
                if event.key == pygame.K_SPACE:
                    if self.checkBullet == False:
                        bullet.bulletX = self.playerX
                        bullet.bulletY = self.playerY
                        self.checkBullet = True
                        i += 1

                        bullet.valueB_Y = -1
                if event.key == pygame.K_v:
                    self.yPress = "Yes"
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT \
                        or event.key == pygame.K_RIGHT \
                        or event.key == pygame.K_UP \
                        or event.key == pygame.K_DOWN:
                    self.valueX = 0
                    self.valueY = 0

    def movePlayer(self):
        self.playerX += self.valueX
        self.playerY += self.valueY

        if self.playerX <= -12:
            self.playerX = -12
        if self.playerX >= 598:
            self.playerX = 598
        if self.playerY <= 0:
            self.playerY = 0
        if self.playerY >= 586:
            self.playerY = 586

    def appearPlayer(self, screen):
        screen.blit(self.Player, (self.playerX, self.playerY))
