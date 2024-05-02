
import pygame


# create fonts
MONO_FONT = pygame.font.SysFont("FreeMono", 25)
BOLD_FONT = pygame.font.SysFont("FreeMono", 25, bold = True)

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

TEXT_MARGIN = {"top": 200, "bottom": 100, "left": 100, "right": 100}

COMPONENT_SPACING = 100


# standard alphabet
LETTERS_IN_ALPHABET = 26

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# number of enigma components
ENIGMA_COMPONENTS = 6


# rotor wiring configurations
ROTOR_I_WIRING = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_II_WIRING = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR_III_WIRING = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
ROTOR_IV_WIRING = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
ROTOR_V_WIRING = "VZBRGITYUPSDNHLXAWMJQOFECK"

# rotor notch positions
ROTOR_I_NOTCH_POSITION = "Q"
ROTOR_II_NOTCH_POSITION = "E"
ROTOR_III_NOTCH_POSITION = "V"
ROTOR_IV_NOTCH_POSITION = "J"
ROTOR_V_NOTCH_POSITION = "Z"


# reflector wiring configurations
REFLECTOR_A = "EJMZALYXVBWFCRQUONTSPIKHGD"
REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
REFLECTOR_C = "FVPJIAOYEDRZXWGCTKUQSBNMHL"


INPUT = ""
OUTPUT = ""

PATH = []