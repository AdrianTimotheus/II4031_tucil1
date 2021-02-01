from vigenere import Vigenere

class ExtendedVigenere(Vigenere):
    def __init__(self):
        super().__init__()

    def change_character(self):
        for i in range(len(self.input)):
            ascii_input = ord(self.input[i])
            ascii_key = ord(self.key[i])

            ascii_output = ((ascii_input+ascii_key)%256)
            self.output += chr(ascii_output)

    def change_character_reversed(self):
        for i in range(len(self.input)):
            ascii_input = ord(self.input[i])
            ascii_key = ord(self.key[i])

            ascii_output = ((ascii_input-ascii_key)%256)
            self.output += chr(ascii_output)
        
    
    def encrypt(self, input, key):
        self.clear_all()
        self.input = input
        self.adjust_key_length(key)
        self.change_character()
        self.display()

    def decrypt(self, input, key):
        self.clear_all()
        self.input = input
        self.adjust_key_length(key)
        self.change_character_reversed()
        self.display()
