"""
!/usr/bin/env python
#-*- coding: utf-8 -*-

Author: Charles TELLIER
"""

import pygame

BALL_SPEED = 15
BALL_RADIUS = 10


class Ball:

    def __init__(self, x, y):
        """
        :param x: Initial x position of the ball
        :param y: Initial y position of the ball
        """
        self.x = x
        self.y = y
        self.radius = BALL_RADIUS
        self.vector_list = [[1.0 / module(1.0, 2.0), 2.0 / module(1.0, 2.0)],
                            [1.0 / module(1.0, 1.0), 1.0 / module(1.0, 1.0)],
                            [2.0 / module(1.0, 2.0), 1.0 / module(1.0, 2.0)],
                            [2.0 / module(1.0, 2.0), -1.0 / module(1.0, 2.0)],
                            [1.0 / module(1.0, 1.0), -1.0 / module(1.0, 1.0)],
                            [1.0 / module(1.0, 2.0), -2.0 / module(1.0, 2.0)],
                            [-1.0 / module(1.0, 2.0), -2.0 / module(1.0, 2.0)],
                            [-1.0 / module(1.0, 1.0), -1.0 / module(1.0, 1.0)],
                            [-2.0 / module(1.0, 2.0), -1.0 / module(1.0, 2.0)],
                            [-2.0 / module(1.0, 2.0), 1.0 / module(1.0, 2.0)],
                            [-1.0 / module(1.0, 1.0), 1.0 / module(1.0, 1.0)],
                            [-1.0 / module(1.0, 2.0), 2.0 / module(1.0, 2.0)]]
        self.vector = self.vector_list[5]

    def draw(self, win):
        """
        :param win: pygame display surface
        """
        pygame.draw.circle(win, (204, 255, 0), (self.x, self.y), self.radius)

    def move(self, x_limit, racquet, wall):
        self.x = int(self.x + self.vector[0] * BALL_SPEED)
        self.y = int(self.y + self.vector[1] * BALL_SPEED)
        self.collide_screen(x_limit)
        self.collide_racquet(racquet)
        score = self.collide_wall(wall)
        return score

    def collide_screen(self, x_limit):
        if self.x - self.radius <= 0:
            self.x = self.radius
            if self.vector_list.index(self.vector) == 11:
                self.vector = self.vector_list[0]
            elif self.vector_list.index(self.vector) == 10:
                self.vector = self.vector_list[1]
            elif self.vector_list.index(self.vector) == 9:
                self.vector = self.vector_list[2]
            elif self.vector_list.index(self.vector) == 8:
                self.vector = self.vector_list[3]
            elif self.vector_list.index(self.vector) == 7:
                self.vector = self.vector_list[4]
            elif self.vector_list.index(self.vector) == 6:
                self.vector = self.vector_list[5]
        elif self.x + self.radius >= x_limit:
            self.x = x_limit - self.radius
            if self.vector_list.index(self.vector) == 0:
                self.vector = self.vector_list[11]
            elif self.vector_list.index(self.vector) == 1:
                self.vector = self.vector_list[10]
            elif self.vector_list.index(self.vector) == 2:
                self.vector = self.vector_list[9]
            elif self.vector_list.index(self.vector) == 3:
                self.vector = self.vector_list[8]
            elif self.vector_list.index(self.vector) == 4:
                self.vector = self.vector_list[7]
            elif self.vector_list.index(self.vector) == 5:
                self.vector = self.vector_list[6]
        if self.y - self.radius <= 0:
            self.y = self.radius
            if self.vector_list.index(self.vector) == 5:
                self.vector = self.vector_list[0]
            elif self.vector_list.index(self.vector) == 4:
                self.vector = self.vector_list[1]
            elif self.vector_list.index(self.vector) == 3:
                self.vector = self.vector_list[2]
            elif self.vector_list.index(self.vector) == 6:
                self.vector = self.vector_list[11]
            elif self.vector_list.index(self.vector) == 7:
                self.vector = self.vector_list[10]
            elif self.vector_list.index(self.vector) == 8:
                self.vector = self.vector_list[9]

    def collide_racquet(self, racquet):
        if self.y + self.radius >= racquet.y and self.y < racquet.y + 15 \
                and racquet.x <= self.x <= racquet.x + racquet.width:
            self.y = racquet.y - self.radius
            if self.x < racquet.x + racquet.width // 3:
                if self.vector_list.index(self.vector) == 0 or \
                        self.vector_list.index(self.vector) == 1 or \
                        self.vector_list.index(self.vector) == 2:
                    self.vector = self.vector_list[3]
                elif self.vector_list.index(self.vector) == 9 or \
                        self.vector_list.index(self.vector) == 10 or \
                        self.vector_list.index(self.vector) == 11:
                    self.vector = self.vector_list[8]
            elif racquet.x + racquet.width // 3 <= self.x < racquet.x + 2 * racquet.width // 3:
                if self.vector_list.index(self.vector) == 0 or \
                        self.vector_list.index(self.vector) == 1 or \
                        self.vector_list.index(self.vector) == 2:
                    self.vector = self.vector_list[4]
                elif self.vector_list.index(self.vector) == 9 or \
                        self.vector_list.index(self.vector) == 10 or \
                        self.vector_list.index(self.vector) == 11:
                    self.vector = self.vector_list[7]
            else:
                if self.vector_list.index(self.vector) == 0 or \
                        self.vector_list.index(self.vector) == 1 or \
                        self.vector_list.index(self.vector) == 2:
                    self.vector = self.vector_list[5]
                elif self.vector_list.index(self.vector) == 9 or \
                        self.vector_list.index(self.vector) == 10 or \
                        self.vector_list.index(self.vector) == 11:
                    self.vector = self.vector_list[6]

    def collide_wall(self, wall):
        for brick in wall.bricks:
            if brick.exists:
                if brick.x <= self.x <= brick.x + brick.width and self.y - self.radius <= brick.y + brick.height:
                    brick.exists = False
                    self.y = brick.y + brick.height + self.radius
                    if self.vector_list.index(self.vector) == 5:
                        self.vector = self.vector_list[0]
                    elif self.vector_list.index(self.vector) == 4:
                        self.vector = self.vector_list[1]
                    elif self.vector_list.index(self.vector) == 3:
                        self.vector = self.vector_list[2]
                    elif self.vector_list.index(self.vector) == 6:
                        self.vector = self.vector_list[11]
                    elif self.vector_list.index(self.vector) == 7:
                        self.vector = self.vector_list[10]
                    elif self.vector_list.index(self.vector) == 8:
                        self.vector = self.vector_list[9]
                    return brick.score
                elif brick.x <= self.x <= brick.x + brick.width and self.y + self.radius >= brick.y and self.y < brick.y:
                    brick.exists = False
                    self.y = brick.y - self.radius
                    if self.vector_list.index(self.vector) == 0:
                        self.vector = self.vector_list[5]
                    elif self.vector_list.index(self.vector) == 1:
                        self.vector = self.vector_list[4]
                    elif self.vector_list.index(self.vector) == 2:
                        self.vector = self.vector_list[3]
                    elif self.vector_list.index(self.vector) == 11:
                        self.vector = self.vector_list[6]
                    elif self.vector_list.index(self.vector) == 10:
                        self.vector = self.vector_list[7]
                    elif self.vector_list.index(self.vector) == 9:
                        self.vector = self.vector_list[8]
                    return brick.score
                elif brick.y <= self.y <= brick.y + brick.height and \
                        self.x + self.radius >= brick.x and self.x < brick.x:
                    brick.exists = False
                    self.x = brick.x - self.radius
                    if self.vector_list.index(self.vector) == 5:
                        self.vector = self.vector_list[6]
                    elif self.vector_list.index(self.vector) == 4:
                        self.vector = self.vector_list[7]
                    elif self.vector_list.index(self.vector) == 3:
                        self.vector = self.vector_list[8]
                    elif self.vector_list.index(self.vector) == 2:
                        self.vector = self.vector_list[9]
                    elif self.vector_list.index(self.vector) == 1:
                        self.vector = self.vector_list[10]
                    elif self.vector_list.index(self.vector) == 0:
                        self.vector = self.vector_list[11]
                    return brick.score
                elif brick.y <= self.y <= brick.y + brick.height and \
                        self.x - self.radius <= brick.x + brick.height and self.x > brick.x + brick.height:
                    brick.exists = False
                    self.x = brick.x + brick.height + self.radius
                    if self.vector_list.index(self.vector) == 11:
                        self.vector = self.vector_list[0]
                    elif self.vector_list.index(self.vector) == 10:
                        self.vector = self.vector_list[1]
                    elif self.vector_list.index(self.vector) == 9:
                        self.vector = self.vector_list[2]
                    elif self.vector_list.index(self.vector) == 8:
                        self.vector = self.vector_list[3]
                    elif self.vector_list.index(self.vector) == 7:
                        self.vector = self.vector_list[4]
                    elif self.vector_list.index(self.vector) == 6:
                        self.vector = self.vector_list[5]
                    return brick.score
        return 0


def module(x, y):
    return (x ** 2 + y ** 2) ** 0.5
