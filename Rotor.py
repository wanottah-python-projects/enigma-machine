
import pygame

import global_constants

c = global_constants


class Rotor:

    def __init__(self, wiring, notch_position):

        # standard alphabet
        self.left = c.ALPHABET

        # transposed alphabet
        self.right = wiring

        # turnover notch position
        self.notch = notch_position

    def forward(self, signal):

        # standard alphabet
        letter = self.right[signal]

        # transposed alphabet
        signal = self.left.find(letter)

        return signal

    def backward(self, signal):

        # standard alphabet
        letter = self.left[signal]

        # transposed alphabet
        signal = self.right.find(letter)

        return signal

    def show(self):

        # standard alphabet
        print(self.left)

        # transposed alphabet
        print(self.right)

        print()

    def rotate(self, n = 1, rotating_forward = True):

        for i in range(n):

            if rotating_forward:

                # standard alphabet
                self.left = self.left[1:] + self.left[0]

                # transposed alphabet
                self.right = self.right[1:] + self.right[0]

            else:

                # standard alphabet
                self.left = self.left[c.LETTERS_IN_ALPHABET - 1] + self.left[:c.LETTERS_IN_ALPHABET - 1]

                # transposed alphabet
                self.right = self.right[c.LETTERS_IN_ALPHABET - 1] + self.right[:c.LETTERS_IN_ALPHABET - 1]

    def rotate_to_letter(self, letter):

        n = c.ALPHABET.find(letter)

        self.rotate(n)

    def set_ring(self, n):

        # rotate rotor backwards
        self.rotate(n - 1, rotating_forward = False)

        # adjust turnover notch in relation to wiring
        n_notch = c.ALPHABET.find(self.notch)

        self.notch = c.ALPHABET[(n_notch - n) % c.LETTERS_IN_ALPHABET]

    def draw(self, screen, component_x_position, component_y_position, component_width, component_height, font):

        rotor_component = pygame.Rect(component_x_position, component_y_position, component_width, component_height)

        pygame.draw.rect(screen, "white", rotor_component, width = 2, border_radius = 15)

        # display rotor letters
        for i in range(c.LETTERS_IN_ALPHABET):

            # left side
            rotor_letter = self.left[i]

            rotor_letter = font.render(rotor_letter, True, "grey")

            rotor_text_box = rotor_letter.get_rect(center = (component_x_position +
                                                             component_width / 4,
                                                             component_y_position + (i + 1) *
                                                             component_height /
                                                             (c.LETTERS_IN_ALPHABET + 1)))

            # highlight key
            if i == 0:

                pygame.draw.rect(screen, "teal", rotor_text_box, border_radius = 5)

            # highlight turnover notch position
            if self.left[i] == self.notch:

                rotor_letter = font.render(self.notch, True, "#333333")

                pygame.draw.rect(screen, "white", rotor_text_box, border_radius = 5)

            screen.blit(rotor_letter, rotor_text_box)

            # right side
            rotor_letter = self.right[i]

            rotor_letter = font.render(rotor_letter, True, "grey")

            rotor_text_box = rotor_letter.get_rect(center = (component_x_position +
                                                             component_width * 3 / 4,
                                                             component_y_position + (i + 1) *
                                                             component_height /
                                                             (c.LETTERS_IN_ALPHABET + 1)))

            screen.blit(rotor_letter, rotor_text_box)
