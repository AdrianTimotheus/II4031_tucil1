from vigenere import Vigenere

class AutoKeyVigenere(Vigenere):
    def adjust_key_length(self,key):
        uppercase_key = key.upper()

        if(len(self.input) > len(uppercase_key)):
            sliced_string = self.input[0:len(self.input)-len(uppercase_key)]
            uppercase_key += sliced_string
            self.key = uppercase_key
            # print(self.input)
            # print(self.key)

        elif(len(self.input) == len(key)):
            pass

        else:
            sliced_string = key[0:len(self.input)-1]
            self.change_key(sliced_string)
    
    def change_character_reversed(self):
        key_length=len(self.key)
        upper_key = self.key.upper()

        self.output = ""

        for i in range (len(self.input)):

            idxEncrypted = ord(self.input[i])-65
            # print(i)
            # print(key_length)
            if(i<key_length):
                idxKey = ord(upper_key[i])-65
                # print(upper_key[i],end='')
                # print(idxEncrypted)
            else:
                idxKey = ord(self.output[i-key_length])-65
                # print(self.output[i-key_length],end='')
                # print(i-key_length)
            
            charOutput = chr((idxEncrypted-idxKey) % 26 + 65)

            self.output += charOutput 
        

    def decrypt(self, input, key):
        self.clear_all()
        self.format_input(input)
        self.key=key
        self.change_character_reversed()
        self.display()
        
        