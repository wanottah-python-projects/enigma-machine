
import pygame

import GlobalConstants

c = GlobalConstants


class Rotor:

    def __init__(self, wiring, notch_position):

        self.left = c.ALPHABET

        self.right = wiring

        self.notch_position = notch_position

    def signal_input(self, input_signal):

        input_letter = self.right[input_signal]

        input_signal = self.left.find(input_letter)

        return input_signal

    def signal_output(self, output_signal):

        encoded_output_letter = self.left[output_signal]

        output_signal = self.right.find(encoded_output_letter)

        return output_signal

    def show(self):

        print(self.left)

        print(self.right)

        print()

    def rotate(self, n = 1, forward = True):

        for i in range(n):

            if forward:

                self.left = self.left[1:] + self.left[0]

                self.right = self.right[1:] + self.right[0]

            else:

                self.left = self.left[c.LETTERS_IN_ALPHABET - 1] + self.left[:c.LETTERS_IN_ALPHABET - 1]

                self.right = self.right[c.LETTERS_IN_ALPHABET - 1] + self.right[:c.LETTERS_IN_ALPHABET - 1]

    def rotate_to_letter(self, letter):

        n = c.ALPHABET.find(letter)

        self.rotate(n)

    def set_ring(self, n):

        # rotate rotor backwards
        self.rotate(n - 1, forward = False)

        # adjust turnover notch
        n_notch = c.ALPHABET.find(self.notch_position)

        self.notch_position = c.ALPHABET[(n_notch - n) % c.LETTERS_IN_ALPHABET]

    def draw_rotor_component(self, screen, x_position, y_position, rectangle_width, rectangle_height, font):

        rectangle = pygame.Rect(x_position, y_position, rectangle_width, rectangle_height)

        pygame.draw.rect(screen, "white", rectangle, width = 2, border_radius = 15)

        # display letters
        for i in range(c.LETTERS_IN_ALPHABET):

            # left side
            letter = self.left[i]

            letter = font.render(letter, True, "grey")

            text_box = letter.get_rect(center = (x_position + rectangle_width / 4,
                                                 y_position + (i + 1) * rectangle_height /
                                                 (c.LETTERS_IN_ALPHABET + 1)))

            # highlight key
            if i == 0:

                pygame.draw.rect(screen, "teal", text_box, border_radius = 5)

            # highlight notch position
            if self.left[i] == self.notch_position:

                letter = font.render(self.notch_position, True, "#333333")

                pygame.draw.rect(screen, "white", text_box, border_radius = 5)

            screen.blit(letter, text_box)

            # right side
            letter = self.right[i]

            letter = font.render(letter, True, "grey")

            text_box = letter.get_rect(center = (x_position + rectangle_width * 3 / 4,
                                                 y_position + (i + 1) * rectangle_height /
                                                 (c.LETTERS_IN_ALPHABET + 1)))

            screen.blit(letter, text_box)
