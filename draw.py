
import pygame

import global_constants

c = global_constants


def draw(enigma, path, screen, component_width, component_height, text_margin, component_spacing, font):

    left_margin = text_margin["left"]

    right_margin = text_margin["right"]

    top_margin = text_margin["top"]

    bottom_margin = text_margin["bottom"]

    component_width = (component_width - left_margin - right_margin - (c.ENIGMA_COMPONENTS - 1) * component_spacing) / c.ENIGMA_COMPONENTS

    component_height = component_height - top_margin - bottom_margin

    # initialise signal path coordinates
    signal_y_position = [top_margin + (signal + 1) * component_height / (c.LETTERS_IN_ALPHABET + 1) for signal in path]

    # from keyboard
    signal_x_position = [c.SCREEN_WIDTH - right_margin - component_width / 2]

    # signal path coordinates
    for i in [4, 3, 2, 1, 0]:

        # forward pass
        signal_x_position.append(left_margin + i * (component_width + c.COMPONENT_SPACING) + component_width * 3 / 4)
        signal_x_position.append(left_margin + i * (component_width + c.COMPONENT_SPACING) + component_width * 1 / 4)

    # reflector
    signal_x_position.append(left_margin + component_width * 3 / 4)

    for i in [1, 2, 3, 4]:

        # backward pass
        signal_x_position.append(left_margin + i * (component_width + c.COMPONENT_SPACING) + component_width * 1 / 4)
        signal_x_position.append(left_margin + i * (component_width + c.COMPONENT_SPACING) + component_width * 3 / 4)

    # to lampboard
    signal_x_position.append(c.SCREEN_WIDTH - right_margin - component_width / 2)

    # draw signal path
    if len(path) > 0:

        for i in range(1, 21):

            if i < 10:

                color = "#43aa8b" \

            elif i < 12:

                color = "#f9c74f"

            else:

                color = "#e63946"

            start = (signal_x_position[i - 1], signal_y_position[i - 1])

            end = (signal_x_position[i], signal_y_position[i])

            pygame.draw.line(screen, color, start, end, width = 5)

    # draw enigma machine
    components = [enigma.reflector,
                  enigma.rotor1,
                  enigma.rotor2,
                  enigma.rotor3,
                  enigma.plugboard,
                  # enigma.lampboard,
                  enigma.keyboard]

    component_x_position = left_margin

    for component in components:

        component.draw(screen,
                       component_x_position,
                       top_margin,
                       component_width,
                       component_height,
                       font)

        component_x_position += component_width + component_spacing

    # display component names
    component_name_y = top_margin * 0.8

    for name in range(len(c.COMPONENT_NAMES)):

        component_name_x = left_margin + component_width / 2 + name * (component_width + c.COMPONENT_SPACING)

        component_name = font.render(c.COMPONENT_NAMES[name], True, "white")

        component_text_box = component_name.get_rect(center = (component_name_x, component_name_y))

        screen.blit(component_name, component_text_box)
