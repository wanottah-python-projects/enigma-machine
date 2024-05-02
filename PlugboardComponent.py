
import pygame

import GlobalConstants

c = GlobalConstants


class Plugboard:

    def __init__(self, letter_pairs):

        self.left = c.ALPHABET

        self.right = c.ALPHABET

        for pair in letter_pairs:

            input_a = pair[0]

            output_b = pair[1]

            pos_A = self.left.find(input_a)

            pos_B = self.left.find(output_b)

            self.left = self.left[:pos_A] + output_b + self.left[pos_A + 1:]

            self.left = self.left[:pos_B] + input_a + self.left[pos_B + 1:]

    def letter_input(self, input_signal):

        input_letter = self.right[input_signal]

        input_signal = self.left.find(input_letter)

        return input_signal

    def letter_output(self, output_signal):

        encoded_output_letter = self.left[output_signal]

        output_signal = self.right.find(encoded_output_letter)

        return output_signal

    def draw(self, screen, x_position, y_position, rectangle_width, rectangle_height, font):

        rectangle = pygame.Rect(x_position, y_position, rectangle_width, rectangle_height)

        pygame.draw.rect(screen, "white", rectangle, width = 2, border_radius = 15)

        # letters
        for i in range(c.LETTERS_IN_ALPHABET):

            # left side
            letter = self.left[i]

            letter = font.render(letter, True, "grey")

            text_box = letter.get_rect(center = (x_position + rectangle_width / 4,
                                                 y_position + (i + 1) * rectangle_height /
                                                 (c.LETTERS_IN_ALPHABET + 1)))

            screen.blit(letter, text_box)

            # right side
            letter = self.right[i]

            letter = font.render(letter, True, "grey")

            text_box = letter.get_rect(center = (x_position + rectangle_width * 3 / 4,
                                                 y_position + (i + 1) * rectangle_height /
                                                 (c.LETTERS_IN_ALPHABET + 1)))

            screen.blit(letter, text_box)
