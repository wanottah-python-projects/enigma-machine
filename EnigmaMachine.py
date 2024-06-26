
class EnigmaMachine:

    def __init__(self, reflector, rotor1, rotor2, rotor3, plugboard, keyboard):  # lampboard, keyboard):

        self.reflector = reflector
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.plugboard = plugboard
        # self.lampboard = lampboard
        self.keyboard = keyboard

    def set_rings(self, ring):

        self.rotor1.set_ring(ring[0])
        self.rotor2.set_ring(ring[1])
        self.rotor3.set_ring(ring[2])

    def set_key(self, key):

        self.rotor1.rotate_to_letter(key[0])
        self.rotor2.rotate_to_letter(key[1])
        self.rotor3.rotate_to_letter(key[2])

    def encipher_message(self, letter):

        # rotate rotors
        if self.rotor2.left[0] == self.rotor2.notch and self.rotor3.left[0] == self.rotor3.notch:

            self.rotor1.rotate()
            self.rotor2.rotate()
            self.rotor3.rotate()

        elif self.rotor2.left[0] == self.rotor2.notch:

            self.rotor1.rotate()
            self.rotor2.rotate()
            self.rotor3.rotate()

        elif self.rotor3.left[0] == self.rotor3.notch:

            self.rotor2.rotate()
            self.rotor3.rotate()

        else:

            self.rotor3.rotate()

        # pass signal through machine
        signal = self.keyboard.forward(letter)
        path = [signal, signal]

        signal = self.plugboard.forward(signal)
        path.append(signal)
        path.append(signal)

        signal = self.rotor3.forward(signal)
        path.append(signal)
        path.append(signal)

        signal = self.rotor2.forward(signal)
        path.append(signal)
        path.append(signal)

        signal = self.rotor1.forward(signal)
        path.append(signal)
        path.append(signal)

        signal = self.reflector.reflect(signal)
        path.append(signal)
        path.append(signal)
        path.append(signal)

        signal = self.rotor1.backward(signal)
        path.append(signal)
        path.append(signal)

        signal = self.rotor2.backward(signal)
        path.append(signal)
        path.append(signal)

        signal = self.rotor3.backward(signal)
        path.append(signal)
        path.append(signal)

        signal = self.plugboard.backward(signal)
        path.append(signal)
        path.append(signal)

        # letter = self.lampboard.backward(signal)
        letter = self.keyboard.backward(signal)

        return path, letter
