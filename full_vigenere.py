from vigenere import Vigenere
from string import ascii_uppercase as asciiUppercase
from string import ascii_letters as ascii

import numpy as np
from numpy import random

class Full_Vigenere(Vigenere):
    def __init__(self):
        super().__init__()
        self.table = [[asciiUppercase[i] for i in range (26)] for j in range (26)]

    def format_input_vigenere(self,input):
        uppercase_input = input.upper()
        self.input=""
        for i in uppercase_input:
            if(ord(i)>=65 and ord(i)<=90):
                self.input = self.input + i

    def change_character(self):
        for i in range (len(self.input)):
            idxInput = ord(self.input[i])-65
            idxKey = ord(self.key[i])-65
            self.output += self.table[idxKey][idxInput]
    
    def change_character_reversed(self):
        # print("CCR:"+self.input)
        # print("CCRSO:"+self.output)
        for i in range (len(self.input)):
            idxCipher = ord(self.input[i])-65
            idxKey = ord(self.key[i])-65

            j = 0
            while(self.table[idxKey][j] != self.input[i]):
                j = j+1
            
            self.output+=chr(j+65)

        # print("self output:" + self.output)

    def generate_table(self):
        for i in range (26):
            temp_array = self.table[i]
            random.shuffle(temp_array)
            self.table[i] = temp_array
        # print(self.table)
        # print(self.table[0][1])
        # print(self.table[1][0])

    def encrypt(self,input,key):
        self.clear_all()
        self.format_input(input)
        self.adjust_key_length(key)
        self.change_character()
        self.display()

    def decrypt(self,input,key):
        self.output=""
        self.format_input_vigenere(input)
        self.adjust_key_length(key)
        self.change_character_reversed()
        self.display()

    
