"""
!/usr/bin/env python
#-*- coding: utf-8 -*-

Author: Charles TELLIER
"""

import pygame


class Brick:

    def __init__(self, x, y, width, height, color, score):
        """
        :param x: Top left x position of the brick
        :param y: Top left y position of the brick
        :param width: Width of the brick
        :param height: Height of the brick
        :param color: Color of the brick
        :param score: Score if the brick is broken
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.score = score
        self.exists = True

    def draw(self, win):
        if self.exists:
            # pygame.draw.rect(win, self.color, pygame.rect(self.x, self.y, self.width, self.height), width=1)
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
