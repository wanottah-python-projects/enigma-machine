
import pygame

import GlobalConstants

c = GlobalConstants


class Reflector:

    def __init__(self, wiring):

        self.left = c.ALPHABET

        self.right = wiring

    def signal_input(self, input_signal):

        input_letter = self.right[input_signal]

        input_signal = self.left.find(input_letter)

        return input_signal

    def draw_reflector_component(self, screen, x_position, y_position, component_width, component_height, font):

        reflector_component = pygame.Rect(x_position, y_position, component_width, component_height)

        pygame.draw.rect(screen, "white", reflector_component, width = 2, border_radius = 15)

        # display letters
        for i in range(c.LETTERS_IN_ALPHABET):

            # left side
            letter = self.left[i]

            letter = font.render(letter, True, "grey")

            text_box = letter.get_rect(center = (x_position + component_width / 4,
                                                 y_position + (i + 1) * component_height /
                                                 (c.LETTERS_IN_ALPHABET + 1)))

            screen.blit(letter, text_box)

            # right side
            letter = self.right[i]

            letter = font.render(letter, True, "grey")

            text_box = letter.get_rect(center = (x_position + component_width * 3 / 4,
                                                 y_position + (i + 1) * component_height /
                                                 (c.LETTERS_IN_ALPHABET + 1)))

            screen.blit(letter, text_box)
