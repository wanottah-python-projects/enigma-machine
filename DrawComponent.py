
import pygame

import GlobalConstants

c = GlobalConstants


# draw enigma machine
def draw_component(enigma, path, screen, component_width, component_height, margin, component_spacing, font):

    x1_position = margin["left"]

    x2_position = margin["right"]

    y1_position = margin["top"]

    y2_position = margin["bottom"]

    width = ((component_width - x1_position - x2_position - (c.ENIGMA_COMPONENTS - 1) *
              component_spacing) / c.ENIGMA_COMPONENTS)

    height = component_height - y1_position - y2_position

    components = [enigma.reflector, enigma.rotor_1, enigma.rotor_2, enigma.rotor_3, enigma.plugboard, enigma.keyboard]

    for component in components:

        component.draw_component(screen, x1_position, y1_position, width, height, font)

        x1_position += width + component_spacing
