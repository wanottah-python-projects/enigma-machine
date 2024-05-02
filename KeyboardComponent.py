
import pygame

import GlobalConstants

c = GlobalConstants


class Keyboard:

    def letter_input(self, key_pressed):

        signal_input = c.ALPHABET.find(key_pressed)

        return signal_input

    def draw_keyboard_component(self, screen, x_position, y_position, rectangle_width, rectangle_height, font):

        keyboard_component = pygame.Rect(x_position, y_position, rectangle_width, rectangle_height)

        pygame.draw.rect(screen, "white", keyboard_component, width = 2, border_radius = 15)

        # display letters
        for i in range(c.LETTERS_IN_ALPHABET):

            letter = c.ALPHABET[i]

            letter = font.render(letter, True, "grey")

            text_box = letter.get_rect(center = (x_position + rectangle_width / 2,
                                                 y_position + (i + 1) * rectangle_height /
                                                 (c.LETTERS_IN_ALPHABET + 1)))

            screen.blit(letter, text_box)


k = Keyboard()
i = k.letter_input("A")
print(i)
