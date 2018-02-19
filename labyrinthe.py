#! /usr/bin/env python3
# coding: utf-8

import os
import sys
import json
import random

import pygame

from level import *

class Object:
    """ This class creates the object and position them on the labyrinth"""

    def __init__(self, face):
        """ This method gives the attribute to the Object's item """
        self.x_position = 0
        self.y_position = 0
        self.face = face
        self.direction = ""

    def get_position(self, labyrinth_structure):
        """ This method selects a random valid place in the labyrinth
         to get object position """
        valid_location = []
        for index_line, line in enumerate(labyrinth_structure):
            for index_stripe, stripe in enumerate(line):
                if stripe == "O":
                    valid_location.append([index_line, index_stripe])
                else:
                    pass
        winner_location = random.choice(valid_location)
        self.y_position = winner_location[0]
        self.x_position = winner_location[1]

def main():
    pygame.init()
    window = pygame.display.set_mode((1000, 1000))

    screen_play = pygame.Surface((600, 600))
    labyrinth = Level("labyrinthe.json", "line")

    game = 1
    while game:
        pygame.draw.rect(window, (255, 255, 255), (0, 0, 1000, 1000))
        window.blit(screen_play, (200, 200))
        labyrinth.print_level(screen_play)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                game = 0
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
