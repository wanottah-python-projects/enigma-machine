
import pygame


# standard alphabet
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# rotor configurations
ROTOR_I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
ROTOR_IV = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
ROTOR_V = "VZBRGITYUPSDNHLXAWMJQOFECK"

# rotor notch positions
ROTOR_I_NOTCH = "Q"
ROTOR_II_NOTCH = "E"
ROTOR_III_NOTCH = "V"
ROTOR_IV_NOTCH = "J"
ROTOR_V_NOTCH = "Z"

# reflector configuration
REFLECTOR_A = "EJMZALYXVBWFCRQUONTSPIKHGD"
REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
REFLECTOR_C = "FVPJIAOYEDRZXWGCTKUQSBNMHL"


# setup pygame
pygame.init()

pygame.font.init()

pygame.display.set_caption("Enigma Simulator")

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Enigma:

    def __init__(self, keyboard, plugboard, rotor_3, rotor_2, rotor_1, reflector, lampboard):

        self.keyboard = keyboard

        self.plugboard = plugboard

        self.rotor_3 = rotor_3

        self.rotor_2 = rotor_2

        self.rotor_1 = rotor_1

        self.reflector = reflector

        self.lampboard = lampboard

    def set_rings(self, ring):

        self.rotor_1.set_ring(ring[0])

        self.rotor_2.set_ring(ring[1])

        self.rotor_3.set_ring(ring[2])

    def set_key(self, key):

        self.rotor_1.rotate_to_letter(key[0])

        self.rotor_2.rotate_to_letter(key[1])

        self.rotor_3.rotate_to_letter(key[2])

    def encipher(self, letter):

        # rotate rotors
        if self.rotor_2.left[0] == self.rotor_2.notch and self.rotor_3.left[0] == self.rotor_3.notch:

            self.rotor_1.rotate()

            self.rotor_2.rotate()

            self.rotor_2.rotate()

        elif self.rotor_2.left[0] == self.rotor_2.notch:

            self.rotor_1.rotate()

            self.rotor_2.rotate()

            self.rotor_3.rotate()

        elif self.rotor_3.left[0] == self.rotor_3.notch:

            self.rotor_2.rotate()

            self.rotor_3.rotate()

        else:

            self.rotor_3.rotate()

        signal = self.keyboard.letter_input(letter)

        signal = self.plugboard.letter_input(signal)

        signal = self.rotor_3.signal_input(signal)
        signal = self.rotor_2.signal_input(signal)
        signal = self.rotor_1.signal_input(signal)

        signal = self.reflector.signal_input(signal)

        signal = self.rotor_1.signal_output(signal)
        signal = self.rotor_2.signal_output(signal)
        signal = self.rotor_3.signal_output(signal)

        signal = self.plugboard.letter_output(signal)

        letter = self.lampboard.letter_output(signal)

        return letter


class Keyboard:

    def letter_input(self, input_letter):

        input_signal = ALPHABET.find(input_letter)

        return input_signal


class Plugboard:

    def __init__(self, letter_pairs):

        self.left = ALPHABET

        self.right = ALPHABET

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


class Rotor:

    def __init__(self, wiring, notch):

        self.left = ALPHABET

        self.right = wiring

        self.notch = notch

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

    def rotate(self, n=1, forward=True):

        for i in range(n):

            if forward:

                self.left = self.left[1:] + self.left[0]

                self.right = self.right[1:] + self.right[0]

            else:

                self.left = self.left[25] + self.left[:25]

                self.right = self.right[25] + self.right[:25]

    def rotate_to_letter(self, letter):

        n = ALPHABET.find(letter)

        self.rotate(n)

    def set_ring(self, n):

        # rotate rotor backwards
        self.rotate(n-1, forward=False)

        # adjust turnover notch
        n_notch = ALPHABET.find(self.notch)

        self.notch = ALPHABET[(n_notch - n) % 26]


class Reflector:

    def __init__(self, wiring):

        self.left = ALPHABET

        self.right = wiring

    def signal_input(self, input_signal):

        input_letter = self.right[input_signal]

        input_signal = self.left.find(input_letter)

        return input_signal


class Lampboard:

    def letter_output(self, output_signal):

        encoded_output_letter = ALPHABET[output_signal]

        return encoded_output_letter


# initialise rotors
rotor_i = Rotor(ROTOR_I, ROTOR_I_NOTCH)
rotor_ii = Rotor(ROTOR_II, ROTOR_II_NOTCH)
rotor_iii = Rotor(ROTOR_III, ROTOR_III_NOTCH)
rotor_iv = Rotor(ROTOR_IV, ROTOR_IV_NOTCH)
rotor_v = Rotor(ROTOR_V, ROTOR_V_NOTCH)

# initialise reflector
reflector_a = Reflector(REFLECTOR_A)
reflector_b = Reflector(REFLECTOR_B)
reflector_c = Reflector(REFLECTOR_C)



KEYBOARD = Keyboard()
PLUGBOARD = Plugboard(["AB", "CD", "EF"])
LAMPBOARD = Lampboard()

ENIGMA = Enigma(KEYBOARD, PLUGBOARD, rotor_i, rotor_ii, rotor_iv, reflector_b, LAMPBOARD)

# set ring position
ENIGMA.set_rings((5, 26, 2))

# set message key
ENIGMA.set_key("CAT")

"""
# encipher message
message = "THIS COOL ENIGMA MACHINE"

cipher_text = ""

for letter in message:

    cipher_text += ENIGMA.encipher(letter)

print(cipher_text)
"""

animating_display = True

while animating_display:

    SCREEN.fill("#333333")

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            animating_display = False
            

