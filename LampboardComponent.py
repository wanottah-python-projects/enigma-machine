
import pygame

import GlobalConstants

c = GlobalConstants


class Lampboard:

    def letter_output(self, output_signal):

        encoded_output_letter = c.ALPHABET[output_signal]

        return encoded_output_letter

    def draw(self, screen, x_position, y_position, rectangle_width, rectangle_height, font):

        rectangle = pygame.Rect(x_position, y_position, rectangle_width, rectangle_height)

        pygame.draw.rect(screen, "white", rectangle, width = 2, border_radius = 15)

        # letters
        for i in range(c.LETTERS_IN_ALPHABET):

            letter = c.ALPHABET[i]

            letter = font.render(letter, True, "grey")

            text_box = letter.get_rect(center = (x_position + rectangle_width / 2,
                                                 y_position + (i + 1) * rectangle_height /
                                                 (c.LETTERS_IN_ALPHABET + 1)))

            screen.blit(letter, text_box)
