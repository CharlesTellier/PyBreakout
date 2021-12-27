"""
!/usr/bin/env python
#-*- coding: utf-8 -*-

Author: Charles TELLIER
"""

import pygame


class Racquet:

    def __init__(self, x, y, width):
        """
        :param x: Initial x position of the racquet on the screen, WIN_WIDTH // 2
        :param y: Initial y position of the racquet on the screen, WIN_HEIGHT - 50
        :param width: Initial width of the racquet, 200 px
        """
        self.x = x
        self.y = y
        self.width = width
        self.m_left = False
        self.m_right = False

    def draw(self, win):
        """
        :param win: pygame display surface
        """
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, 20))

    def move_left(self, npx):
        """
        :param npx: Number of pixel the racquet has to move left
        """
        if self.x - npx < 0:
            self.x = 0
        else:
            self.x -= npx

    def move_right(self, npx, x_limit):
        """
        :param npx: Number of pixel the racquet has to move right
        :param x_limit: Right limit of the screen
        """
        if self.x + npx + self.width > x_limit:
            self.x = x_limit - self.width
        else:
            self.x += npx
