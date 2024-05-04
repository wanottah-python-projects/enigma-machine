
import pygame

import global_constants

c = global_constants


class Keyboard:

    def forward(self, letter):

        signal = c.ALPHABET.find(letter)

        return signal

    def backward(self, signal):

        letter = c.ALPHABET[signal]

        return letter

    def draw(self, screen, component_x_position, component_y_position, component_width, component_height, font):

        keyboard_component = pygame.Rect(component_x_position, component_y_position, component_width, component_height)

        pygame.draw.rect(screen, "white", keyboard_component, width = 2, border_radius = 15)

        # display keyboard letters
        for i in range(c.LETTERS_IN_ALPHABET):

            keyboard_letter = c.ALPHABET[i]

            keyboard_letter = font.render(keyboard_letter, True, "grey")

            keyboard_text_box = keyboard_letter.get_rect(center = (component_x_position +
                                                                   component_width / 2,
                                                                   component_y_position + (i + 1) *
                                                                   component_height /
                                                                   (c.LETTERS_IN_ALPHABET + 1)))

            screen.blit(keyboard_letter, keyboard_text_box)
