
import pygame

import global_constants

c = global_constants


class Plugboard:

    def __init__(self, pairs):

        # transposed alphabet
        self.left = c.ALPHABET

        # standard alphabet
        self.right = c.ALPHABET

        for pair in pairs:

            A = pair[0]
            B = pair[1]

            pos_A = self.left.find(A)
            pos_B = self.left.find(B)

            self.left = self.left[:pos_A] + B + self.left[pos_A + 1:]
            self.left = self.left[:pos_B] + A + self.left[pos_B + 1:]

    def forward(self, signal):

        # standard alphabet
        letter = self.right[signal]

        # transposed alphabet
        signal = self.left.find(letter)

        return signal

    def backward(self, signal):

        # transposed alphabet
        letter = self.left[signal]

        # standard alphabet
        signal = self.right.find(letter)

        return signal

    def draw(self, screen, component_x_position, component_y_position, component_width, component_height, font):

        plugboard_component = pygame.Rect(component_x_position, component_y_position, component_width, component_height)

        pygame.draw.rect(screen, "white", plugboard_component, width = 2, border_radius = 15)

        # display plugboard letters
        for i in range(c.LETTERS_IN_ALPHABET):

            # left side
            plugboard_letter = self.left[i]

            plugboard_letter = font.render(plugboard_letter, True, "grey")

            plugboard_text_box = plugboard_letter.get_rect(center = (component_x_position +
                                                                     component_width / 4,
                                                                     component_y_position + (i + 1) *
                                                                     component_height /
                                                                     (c.LETTERS_IN_ALPHABET + 1)))

            screen.blit(plugboard_letter, plugboard_text_box)

            # right side
            plugboard_letter = self.right[i]

            plugboard_letter = font.render(plugboard_letter, True, "grey")

            plugboard_text_box = plugboard_letter.get_rect(center = (component_x_position +
                                                                     component_width * 3 / 4,
                                                                     component_y_position + (i + 1) *
                                                                     component_height /
                                                                     (c.LETTERS_IN_ALPHABET + 1)))

            screen.blit(plugboard_letter, plugboard_text_box)
