
import pygame

import global_constants

c = global_constants


class Lampboard:

    def backward(self, signal):

        letter = c.ALPHABET[signal]

        return letter

    def draw(self, screen, component_x_position, component_y_position, component_width, component_height, font):

        lampboard_component = pygame.Rect(component_x_position, component_y_position, component_width, component_height)

        pygame.draw.rect(screen, "white", lampboard_component, width = 2, border_radius = 15)

        # display keyboard letters
        for i in range(c.LETTERS_IN_ALPHABET):

            lampboard_letter = c.ALPHABET[i]

            lampboard_letter = font.render(lampboard_letter, True, "grey")

            lampboard_text_box = lampboard_letter.get_rect(center = (component_x_position +
                                                                     component_width / 2,
                                                                     component_y_position + (i + 1) *
                                                                     component_height /
                                                                     (c.LETTERS_IN_ALPHABET + 1)))

            screen.blit(lampboard_letter, lampboard_text_box)
