"""
!/usr/bin/env python
#-*- coding: utf-8 -*-

Author: Charles TELLIER
"""

import pygame
from racquet import Racquet
from ball import Ball
from wall import Wall

pygame.font.init()

# ---------- Main Constant ----------
WIN_WIDTH = 1280
WIN_HEIGHT = 720
FRAMERATE = 30
RACQUET_SPEED = 20
SCORE_SEP = 620

STAT_FONT = pygame.font.SysFont("comicsans", 30)


def draw_window(win, launched, racquet, ball, wall, score):
    win.fill((0, 0, 0))
    racquet.draw(win)
    ball.draw(win)
    wall.draw(win)
    pygame.draw.line(win, (255, 255, 255), (0, SCORE_SEP), (WIN_WIDTH, SCORE_SEP))
    score_banner = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(score_banner, (30, SCORE_SEP + 30))
    if launched is False:
        launch_banner = STAT_FONT.render("PRESS SPACE BAR TO START", 1, (255, 255, 255))
        win.blit(launch_banner, (WIN_WIDTH // 2 - launch_banner.get_width() // 2,
                                 WIN_HEIGHT // 2 - launch_banner.get_height() // 2))
    pygame.display.update()


def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    racquet = Racquet(WIN_WIDTH // 2, WIN_HEIGHT - 150, 200)
    ball = Ball(WIN_WIDTH // 2, 3 * SCORE_SEP // 4)
    wall = Wall(WIN_WIDTH, 300)
    wall.set_lvl_1()
    clock = pygame.time.Clock()
    score = 0
    run_game = True

    launched = False

    while run_game:
        clock.tick(FRAMERATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                pygame.quit()
                quit()
                break
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                racquet.m_left = True
                racquet.m_right = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                racquet.m_left = False
                racquet.m_right = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                racquet.m_left = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                racquet.m_right = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                launched = True

        if racquet.m_left:
            racquet.move_left(RACQUET_SPEED)
        elif racquet.m_right:
            racquet.move_right(RACQUET_SPEED, WIN_WIDTH)

        if launched:
            score += ball.move(WIN_WIDTH, racquet, wall)

        if ball.y > SCORE_SEP - ball.radius:
            run_game = False
            break

        if score == 8800:
            run_game = False
            break

        draw_window(win, launched, racquet, ball, wall, score)


if __name__ == "__main__":
    main()
