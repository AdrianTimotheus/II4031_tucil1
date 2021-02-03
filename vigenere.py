from string import ascii_uppercase as asciiUppercase
from string import ascii_letters as ascii

class Vigenere:
    def __init__(self):
        # self.table = [asciiUppercase[i:]+asciiUppercase[:i] for i in range(len(asciiUppercase))]
        self.key = ""
        self.input = ""
        self.output = ""

    def change_key(self,key):
        self.key = key
    
    # def printTable(self):
    #     dummyvar = (self.table[0])
    #     print(dummyvar[0])

    #membuat spasi setiap 5 huruf untuk enkripsi
    def add_space(self, input, length):
        return ' '.join(input[i:i+length] for i in range(0,len(input),length))

    #menghapus seluruh isi variabel agar dapat digunakan kembali
    def clear_all(self):
        self.input = ""
        self.key = ""
        self.output = ""
    
    #buang semua karakter non alfabet termasuk spasi, simpan dalam sebuah string baru
    def format_input(self,input):
        uppercase_input = input.upper()
        uppercase_input = uppercase_input.rstrip()
        for i in uppercase_input:
            if(ord(i)>=65 and ord(i)<=90):
                self.input = self.input + i
        # print(self.input)

    #mengulang key hingga sama dengan panjang input
    def repeat_to_length(self, string_to_expand, length):
        return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

    #membuat panjang key sama dengan panjang input
    def adjust_key_length(self,key):

        uppercase_key = key.upper()
        uppercase_key = uppercase_key.rstrip()

        # print("uppercase key: "+uppercase_key)
        # print(len(self.input))
        # print(len(uppercase_key))

        if(len(self.input) > len(uppercase_key)):
            self.key = self.repeat_to_length(uppercase_key,len(self.input))
            # print(uppercase_key)

        elif(len(self.input) == len(key)):
            self.key = key

        else:
            sliced_string = key[0:len(self.input)-1]
            self.change_key(sliced_string)

    #mengubah karakter semula menjadi karakter yang sudah terenkripsi
    def change_character(self):
        for i in range (len(self.input)):
            idxInput = ord(self.input[i])-65
            idxKey = ord(self.key[i])-65
            charOutput = chr((idxInput+idxKey) % 26+65)

            self.output += charOutput
            # if(i==1):
            #     print(self.input)
            #     print(idxInput)
            #     print(idxKey)
            #     print(charOutput)
    
    #mengubah karakter yang terenkripsi menjadi karakter semula
    def change_character_reversed(self):
        for i in range (len(self.input)):
            idxEncrypted = ord(self.input[i])-65
            idxKey = ord(self.key[i])-65
            charOutput = chr((idxEncrypted-idxKey) % 26 + 65)

            self.output += charOutput 

    #tampilkan ke command prompt
    def display(self):
        temp_output = self.add_space(self.output,5)
        print(temp_output)
        # print(self.input)
        # print(self.output)
        # print(self.key)

    def getContent(self):
        return (self.output)

    #fungsi enkripsi vigenere
    def encrypt(self,input,key):
        self.clear_all()
        self.format_input(input)
        self.adjust_key_length(key)
        self.change_character()
        self.display()

    #fungsi dekripsi vigenere
    def decrypt(self,input,key):
        self.clear_all()
        self.format_input(input)
        self.adjust_key_length(key)
        self.change_character_reversed()
        self.display()




