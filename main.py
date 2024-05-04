
import pygame

import global_constants

from EnigmaMachine import EnigmaMachine
from Keyboard import Keyboard
from Plugboard import Plugboard
from Rotor import Rotor
from Reflector import Reflector
from Lampboard import Lampboard

from draw import draw

c = global_constants


# initialise pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Simulator")

SCREEN = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

# create fonts
MONO_FONT = pygame.font.SysFont("FreeMono", 25)
BOLD_FONT = pygame.font.SysFont("FreeMono", 25, bold = True)


# rotor configurations
ROTOR_I = Rotor(c.ROTOR_I_WIRING, c.ROTOR_I_NOTCH_POSITION)
ROTOR_II = Rotor(c.ROTOR_II_WIRING, c.ROTOR_II_NOTCH_POSITION)
ROTOR_III = Rotor(c.ROTOR_III_WIRING, c.ROTOR_III_NOTCH_POSITION)
ROTOR_IV = Rotor(c.ROTOR_IV_WIRING, c.ROTOR_IV_NOTCH_POSITION)
ROTOR_V = Rotor(c.ROTOR_V_WIRING, c.ROTOR_V_NOTCH_POSITION)

# reflector configurations
REFLECTOR_A = Reflector(c.REFLECTOR_A_WIRING)
REFLECTOR_B = Reflector(c.REFLECTOR_B_WIRING)
REFLECTOR_C = Reflector(c.REFLECTOR_C_WIRING)


KEYBOARD = Keyboard()
PLUGBOARD = Plugboard(["AB", "CD", "EF"])
REFLECTOR = REFLECTOR_A
LAMPBOARD = Lampboard()

# define enigma machine
ENIGMA = EnigmaMachine(REFLECTOR_B, ROTOR_I, ROTOR_II, ROTOR_III, PLUGBOARD, KEYBOARD)  # LAMPBOARD, KEYBOARD)

# set ring positions
ENIGMA.set_rings((1, 1, 1))

# set message key
ENIGMA.set_key("CAT")


"""
# encipher message
message = "TESTINGTESTINGTESTINGTESTING"
cipher_text = ""
formatted_text = ""
message_part = 1
for letter in message:
    cipher_text += ENIGMA.encipher_message(letter)
print(cipher_text)
for i in cipher_text:
    formatted_text += i[:4]
    message_part += 1
    if message_part > 4:
        message_part = 1
        formatted_text += " "
print(formatted_text)
"""

application_running = True

while application_running:

    # background colour
    SCREEN.fill("#333333")

    # text input
    text = BOLD_FONT.render(c.INPUT, True, "white")

    text_box = text.get_rect(center = (c.SCREEN_WIDTH / 2, c.TEXT_MARGIN["top"] / 3))

    SCREEN.blit(text, text_box)

    # text output
    text = MONO_FONT.render(c.OUTPUT, True, "white")

    text_box = text.get_rect(center = (c.SCREEN_WIDTH / 2, c.TEXT_MARGIN["top"] / 3 + 25))

    SCREEN.blit(text, text_box)

    # draw enigma machine
    draw(ENIGMA, c.PATH, SCREEN, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.TEXT_MARGIN, c.COMPONENT_SPACING, BOLD_FONT)

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            application_running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:

                ROTOR_III.rotate()

            elif event.key == pygame.K_SPACE:

                c.INPUT += " "

            else:

                key = event.unicode

                if key in c.ALPHABET.lower():

                    letter = key.upper()

                    c.INPUT += letter

                    c.PATH, cipher = ENIGMA.encipher_message(letter)

                    c.OUTPUT += cipher
