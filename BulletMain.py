import pygame


class BulletMain:
    def __init__(self, player):
        self.Bullet = pygame.image.load("img/bullet.png")
        self.bulletX = 0
        self.bulletY = player.playerY
        self.valueB_X = 0
        self.valueB_Y = 0

    def moveBullet(self, player, screen):
        if self.bulletY <= 0:
            player.checkBullet = False
        if player.checkBullet == True:
            screen.blit(self.Bullet, (self.bulletX + 16, self.bulletY + 10))
            self.bulletY += self.valueB_Y



