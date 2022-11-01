import math
import pygame

from BulletMain import BulletMain
from MonsterMain import MonsterMain
from PlayerMain import PlayerMain

def distance(X1, Y1, X2, Y2, compare):
    dic = math.sqrt((X1 - X2) ** 2 + (Y1 - Y2) ** 2)
    if dic < compare:
        return True
    return False

number = 1
score = 0
life = 3
x_player = 293
y_player = 500

def main(number_monster, x_player, y_player):
    pygame.init()
    global score
    global life

    screen = pygame.display.set_mode((650, 650))
    pygame.display.set_caption("Game by K~Hoàng")
    wallpaper = pygame.image.load("img/wall.jpg")

    player = PlayerMain(x_player, y_player)
    monster = MonsterMain(number_monster)
    bullet = BulletMain(player)

    font = pygame.font.SysFont('monospace', 50)
    x_font = pygame.font.SysFont('monospace', 25)

    game_loop = True
    player_move = True

    while game_loop:
        screen.blit(wallpaper, (0, 0))

        # Player
        for i in range(1):
            player.buttonPlayer(bullet, i)
        if player_move:
            player.movePlayer()
        player.appearPlayer(screen)

        for j in range(monster.n_monster):
            # điều kiện dừng game (Monster chạm Player)
            if distance(player.playerX, player.playerY, monster.monsterX[j], monster.monsterY[j], 35):
                player_move = False

                GAME_OVER = font.render("GAME OVER", True, (255, 255, 255))
                screen.blit(GAME_OVER, (190, 200))

                PLAY_AGAIN = x_font.render("PLAY AGAIN ~~~ Press v", True, (255, 255, 255))
                screen.blit(PLAY_AGAIN, (150, 300))

                if player.yPress == "Yes":
                    number_monster = 1
                    score = 0
                    life = 3
                    x_player = 293
                    y_player = 500
                    main(number_monster, x_player, y_player)
                break

            # điều kiện thắng (Bullet chạm Monster)
            if distance(monster.monsterX[j], monster.monsterY[j], bullet.bulletX, bullet.bulletY, 20):
                player.checkBullet = False
                bullet.bulletY= 700
                monster.alien_blood[j] -= 1
                monster.alien_dead -= 1
                score += 1

            # Monster
            if monster.alien_blood[j] == 0:
                monster.monsterX[j] = 293
                monster.monsterY[j] = 800

            monster.moveMonster(j)
            monster.appearMonster(screen, j)

        # Bullet

        bullet.moveBullet(player, screen)

        if monster.alien_dead == 0:
            number_monster += 1
            x_player = player.playerX
            y_player = player.playerY
            main(number_monster, x_player, y_player)

        SCORE = x_font.render("SCORE: " + str(score), True, (255, 255, 255))
        screen.blit(SCORE, (10, 10))

        pygame.display.update()

try:
    main(number, x_player, y_player)
except Exception as e:
    print(e)

input()

