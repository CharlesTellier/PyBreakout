"""
!/usr/bin/env python
#-*- coding: utf-8 -*-

Author: Charles TELLIER
"""

import pygame
import os
from racquet import Racquet
from ball import Ball
from wall import Wall
from random import randint
import neat

pygame.font.init()

# ---------- Main Constant ----------
WIN_WIDTH = 1280
WIN_HEIGHT = 720
FRAMERATE = 30
RACQUET_SPEED = 20
SCORE_SEP = 620

STAT_FONT = pygame.font.SysFont("comicsans", 30)


def draw_window(win, racquets, balls, walls):
    win.fill((0, 0, 0))
    for racquet in racquets:
        racquet.draw(win)
    for ball in balls:
        ball.draw(win)
    for wall in walls:
        wall.draw(win)
    pygame.draw.line(win, (255, 255, 255), (0, SCORE_SEP), (WIN_WIDTH, SCORE_SEP))
    pygame.display.update()


def main(genomes, config):
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    nnets = []
    racquets = []
    balls = []
    walls = []
    ge = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        nnet = neat.nn.FeedForwardNetwork.create(genome, config)
        nnets.append(nnet)
        racquets.append(Racquet(randint(30, WIN_WIDTH - 30), WIN_HEIGHT - 150, 200))
        balls.append(Ball(randint(30, WIN_WIDTH - 30), 3 * SCORE_SEP // 4))
        walls.append(Wall(WIN_WIDTH, 300))
        ge.append(genome)

    for wall in walls:
        wall.set_lvl_1()

    clock = pygame.time.Clock()
    run_game = True

    while run_game and len(balls) > 0:
        clock.tick(FRAMERATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                pygame.quit()
                quit()
                break

        for x, racquet in enumerate(racquets):
            ge[x].fitness += 0.1
            ge[x].fitness += balls[x].move(WIN_WIDTH, racquet, walls[x])

            delta_y = racquet.y - balls[x].y
            delta_x_left = racquet.x - balls[x].x
            delta_x_right = racquet.x + racquet.width - balls[x].x
            output = nnets[x].activate((balls[x].x,
                                        balls[x].y,
                                        delta_y,
                                        delta_x_left,
                                        delta_x_right))

            if output[0] >= 0.5 and output[1] < 0.5:
                racquets[x].move_left(RACQUET_SPEED)
            elif output[1] >= 0.5 and output[0] < 0.5:
                racquets[x].move_right(RACQUET_SPEED, WIN_WIDTH)

        for x, ball in enumerate(balls):
            if ball.y > SCORE_SEP - ball.radius:
                ge[x].fitness -= 1
                nnets.pop(x)
                racquets.pop(x)
                balls.pop(x)
                walls.pop(x)
                ge.pop(x)

        continue_game = False
        for wall in walls:
            for brick in wall.bricks:
                if brick.exists:
                    continue_game = True
        if continue_game is False:
            run_game = False
            break

        draw_window(win, racquets, balls, walls)


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                config_path)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    winner = p.run(main, 50)

    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward")
    run(config_path)
