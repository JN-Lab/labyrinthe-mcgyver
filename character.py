#! /usr/bin/env python3
# coding: utf-8
import pygame

from constants import *

class Character:
    """ This class creates the characters for the game """

    def __init__(self, role):
        """ This method gives the different attributes to the character's object """
        self.x_index = 0
        self.y_index = 0
        self.role = role
        self.image = self.__get_image()
        self.stripe_face = self.__get_stripe_face()

        self.numb_items = 0
        self.direction = ""
        self.success_deplacement = False

    def __get_image(self):
        """ This method generates the image of the character according his role """

        if self.role == "hero":
            image = pygame.image.load(HERO_IMAGE).convert_alpha()
        else:
            image = pygame.image.load(BAD_GUY_IMAGE).convert_alpha()

        return image

    def __get_stripe_face(self):
        """ This method generate the stripe face of the character according his role """

        if self.role == "hero":
            stripe_face = HERO_STRIPE
        else:
            stripe_face = BAD_GUY_STRIPE

        return stripe_face

    def move(self, direction, labyrinth):
        """ This method allows the character to move on the top, the right, the bottom
        or the left if there is no wall. At the same time, it manages the evolution
        of the structure according the movement of the main character. If the
        character reachs the F case, he wins. """

        self.success_deplacement = False
        self.direction = direction
        next_case = labyrinth.get_next_stripe(self.x_index, self.y_index, direction)

        if next_case != WALL_STRIPE and direction == "right":
            self.x_index += 1
            self.success_deplacement = True
        elif next_case != WALL_STRIPE and direction == "left":
            self.x_index -= 1
            self.success_deplacement = True
        elif next_case != WALL_STRIPE and direction == "up":
            self.y_index -= 1
            self.success_deplacement = True
        elif next_case != WALL_STRIPE and direction == "down":
            self.y_index += 1
            self.success_deplacement = True

    def touch_something(self, direction, labyrinth):
        """ This method returns the game status when the character gets into contact
        with an item or another character """

        game_status = ""
        next_case = labyrinth.get_next_stripe(self.x_index, self.y_index, direction)

        if next_case == BAD_GUY_STRIPE:
            if self.numb_items < 3:
                game_status = "game_over"
            else:
                game_status = "win"
        elif next_case == NEEDLE_STRIPE:
            self.numb_items += 1
            game_status = "found_needle"
        elif next_case == ETHER_STRIPE:
            self.numb_items += 1
            game_status = "found_ether"
        elif next_case == TUBE_STRIPE:
            self.numb_items += 1
            game_status = "found_tube"
        else:
            game_status = "continue"

        return game_status
