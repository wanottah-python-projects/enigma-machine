
import pygame

import global_constants

c = global_constants


class Reflector:

    def __init__(self, wiring):

        # standard alphabet
        self.left = c.ALPHABET

        # transposed alphabet
        self.right = wiring

    def reflect(self, signal):

        # transposed alphabet
        letter = self.right[signal]

        # standard alphabet
        signal = self.left.find(letter)

        return signal

    def draw(self, screen, component_x_position, component_y_position, component_width, component_height, font):

        reflector_component = pygame.Rect(component_x_position, component_y_position, component_width, component_height)

        pygame.draw.rect(screen, "white", reflector_component, width = 2, border_radius = 15)

        # display reflector letters
        for i in range(c.LETTERS_IN_ALPHABET):

            # right side
            reflector_letter = self.right[i]

            reflector_letter = font.render(reflector_letter, True, "grey")

            reflector_text_box = reflector_letter.get_rect(center = (component_x_position +
                                                                     component_width * 3 / 4,
                                                                     component_y_position + (i + 1) *
                                                                     component_height /
                                                                     (c.LETTERS_IN_ALPHABET + 1)))

            screen.blit(reflector_letter, reflector_text_box)

            # left side
            reflector_letter = self.left[i]

            reflector_letter = font.render(reflector_letter, True, "grey")

            reflector_text_box = reflector_letter.get_rect(center = (component_x_position +
                                                                     component_width / 4,
                                                                     component_y_position + (i + 1) *
                                                                     component_height /
                                                                     (c.LETTERS_IN_ALPHABET + 1)))

            screen.blit(reflector_letter, reflector_text_box)
