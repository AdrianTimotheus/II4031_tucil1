from string import ascii_uppercase as asciiUppercase
from string import ascii_letters as ascii

class Vigenere:
    def __init__(self):
        self.table = [asciiUppercase[i:]+asciiUppercase[:i] for i in range(len(asciiUppercase))]
        self.key = ""
        self.input = ""
        self.output = ""

    def change_key(self,key):
        self.key = key
    
    def printTable(self):
        dummyvar = (self.table[0])
        print(dummyvar[0])
    
    #buang semua karakter non alfabet termasuk spasi, simpan dalam sebuah string baru
    def format_input(self,input):
        input.upper()
        for i in input:
            if(ord(i)>=65 and ord(i)<=90):
                self.input = self.input + i

    def repeat_to_length(self, string_to_expand, length):
        return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

    def adjust_key_length(self,key):

        key.upper()

        if(len(self.input) > len(key)):
            self.repeat_to_length(self,key,len(self.input))

        elif(len(self.input) == len(key)):
            pass

        else:
            key.slice(0,len(self.input))

    def change_character(self):
        for i in range (len(self.input)):
            idxInput = ord(self.input[i])-95
            idxKey = ord(self.input[i])-95
            charOutput = chr(idxInput+idxKey+95)
            self.output += charOutput


    def encrypt(self,input,key):
        self.format_input(self,input)
        self.adjust_key_length(self,key)
        self.



