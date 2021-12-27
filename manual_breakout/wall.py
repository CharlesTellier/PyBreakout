"""
!/usr/bin/env python
#-*- coding: utf-8 -*-

Author: Charles TELLIER
"""

from brick import Brick


class Wall:
    """
    Contains the position of all the bricks of the game
    """

    def __init__(self, x_limit, y_limit):
        """
        :param x_limit: horizontal limit of the wall
        :param y_limit: Vertical limit of the wall
        """
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.bricks = []

    def set_lvl_1(self):
        block_width = self.x_limit // 16
        block_height = self.y_limit // 10
        # 1
        for i in range(0, 16):
            self.bricks.append(Brick(i * block_width, 0, block_width, block_height, (255, 255, 255), 100))

        # 2
        for i in range(0, 16):
            self.bricks.append(Brick(i * block_width, block_height, block_width, block_height, (225, 225, 225), 90))

        # 3
        for i in range(0, 16):
            self.bricks.append(Brick(i * block_width, 2 * block_height, block_width, block_height, (200, 200, 200), 80))

        # 4
        for i in range(0, 16):
            self.bricks.append(Brick(i * block_width, 3 * block_height, block_width, block_height, (175, 175, 175), 70))

        # 5
        for i in range(0, 16):
            self.bricks.append(Brick(i * block_width, 4 * block_height, block_width, block_height, (150, 150, 150), 60))

        # 6
        for i in range(0, 16):
            self.bricks.append(Brick(i * block_width, 5 * block_height, block_width, block_height, (125, 125, 125), 50))

        # 7
        for i in range(0, 16):
            self.bricks.append(Brick(i * block_width, 6 * block_height, block_width, block_height, (100, 100, 100), 40))

        # 8
        for i in range(0, 16):
            self.bricks.append(Brick(i * block_width, 7 * block_height, block_width, block_height, (75, 75, 75), 30))

        # 9
        for i in range(0, 16):
            self.bricks.append(Brick(i * block_width, 8 * block_height, block_width, block_height, (50, 50, 50), 20))

        # 10
        for i in range(0, 16):
            self.bricks.append(Brick(i * block_width, 9 * block_height, block_width, block_height, (30, 30, 30), 10))

    def draw(self, win):
        for brick in self.bricks:
            brick.draw(win)
