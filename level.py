#! /usr/bin/env python3
# coding: utf-8

import os
import json

import pygame

from constants import *

class Level:
    """ This class creates the Labyrinth which will be used for the game
    from a Json file located in the folder named sources/ """

    def __init__(self, data_file):
        """ This method gives the different attributes to the Level's labyrinth """
        self.data_file = data_file
        self.structure = []
        self.wall_image = self.__get_wall_image()
        self.floor_image = self.__get_floor_image()
        self.wall_stripe_face = WALL_STRIPE
        self.floor_stripe_face = FLOOR_STRIPE

        self.__generate_labyrinth_from_json()

    def __get_wall_image(self):
        """ This private method selects the wall image to load """

        wall_selection_images = pygame.image.load(WALL_IMAGES).convert_alpha()
        wall_image = wall_selection_images.subsurface((300, 20, 40, 40))

        return wall_image

    def __get_floor_image(self):
        """ This private method selects the floor image to load """

        floor_selection_images = pygame.image.load(FLOOR_IMAGES).convert_alpha()
        floor_image = floor_selection_images.subsurface((240, 120, 40, 20))

        return floor_image

    def __generate_labyrinth_from_json(self):
        """ This private method loads the labyrinth's structure into a list
        containing each line. Each line is a list containing each stripe.
        example : structure = [[stripe1_from_line1, stripe2_from_line1,...],
        [stripe1_from_line2, stripe2_from_line2,...],...] """

        labyrinth_structure = []

        directory = os.path.dirname(__file__) # We get the right path
        path_to_file = os.path.join(directory, 'sources', self.data_file) # We build the path

        try:
            with open(path_to_file, "r") as file:
                data = json.load(file)
                for line in data:
                    labyrinth_lines = []
                    for stripe in line:
                        labyrinth_lines.append(stripe)
                    labyrinth_structure.append(labyrinth_lines)

            self.structure = labyrinth_structure
        except FileNotFoundError as error_message:
            print("The file was not found: ", error_message)
        except:
            print("Destination unknown")

    def get_stripe(self, x_index, y_index):
        """ This method returns the stripe of a specific case """

        return self.structure[y_index][x_index]

    def get_next_stripe(self, x_index, y_index, direction):
        """ This method returns the next strip according the direction
        of the character """

        next_stripe = ""
        if direction == "right":
            next_stripe = self.structure[y_index][x_index + 1]
        elif direction == "left":
            next_stripe = self.structure[y_index][x_index - 1]
        elif direction == "up":
            next_stripe = self.structure[y_index - 1][x_index]
        elif direction == "down":
            next_stripe = self.structure[y_index + 1][x_index]

        return next_stripe

    def set_stripe(self, x_index, y_index, stripe):
        """ This method changes the stripe of a specific case """

        self.structure[y_index][x_index] = stripe

    def update_labyrinth_structure(self, character):
        """ This method updates the structure of the level according the position
        and the direction of the character """

        self.set_stripe(character.x_index, character.y_index, character.stripe_face)

        if character.direction is not None and character.success_deplacement:
            if character.direction == "right":
                self.set_stripe(character.x_index - 1, character.y_index, FLOOR_STRIPE)
            elif character.direction == "left":
                self.set_stripe(character.x_index + 1, character.y_index, FLOOR_STRIPE)
            elif character.direction == "up":
                self.set_stripe(character.x_index, character.y_index + 1, FLOOR_STRIPE)
            elif character.direction == "down":
                self.set_stripe(character.x_index, character.y_index -1, FLOOR_STRIPE)
