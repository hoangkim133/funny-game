import random
import pygame

class MonsterMain:
    def __init__(self, number_monster):
        self.Monster = []
        self.monsterX = []
        self.monsterY = []
        self.valueM_X = []
        self.valueM_Y = []
        self.alien_blood = []
        self.n_monster = number_monster
        self.blood = 1
        self.alien_dead = self.n_monster * self.blood
        self.ran = [0.3, 0.35, 0.4, 0.45, 0.25]

        for i in range(self.n_monster):
            self.Monster.append(pygame.image.load("img/ufo.png"))
            self.monsterX.append(random.randint(200, 300))
            self.monsterY.append(random.randint(70, 75))
            self.valueM_X.append(random.choice(self.ran))
            self.valueM_Y.append(random.choice(self.ran))
            self.alien_blood.append(self.blood)

    def moveMonster(self, i):
        self.monsterX[i] += self.valueM_X[i]
        self.monsterY[i] += self.valueM_Y[i]

        if self.monsterX[i] <= 0:
            self.valueM_X[i] = random.choice(self.ran)
        if self.monsterX[i] >= 586:
            self.valueM_X[i] = -random.choice(self.ran)
        if self.monsterY[i] <= 0:
            self.valueM_Y[i] = random.choice(self.ran)
        if self.monsterY[i] >= 586:
            self.valueM_Y[i] = -random.choice(self.ran)

    def appearMonster(self, screen, i):
        screen.blit(self.Monster[i], (self.monsterX[i], self.monsterY[i]))

