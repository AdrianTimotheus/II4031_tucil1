from itertools import chain

class Playfair:
    def __init__(self):
        self.input = ""
        self.key = ""
        self.output = ""
        self.keytable = []
        self.bigram = []

    # def get_distinct_character(self,key):
    #     uppercase_key = key.upper()

    #     NO_OF_CHARS = 256
    #     count = [0] * NO_OF_CHARS

    #     for i in range (len(uppercase_key)): 
    #         if(uppercase_key[i] != ' '): 
    #             count[ord(uppercase_key[i])] += 1
    #     n = i 

    #     for i in range(n+1): 
    #         if (count[ord(uppercase_key[i])] == 1): 
    #             self.key += uppercase_key[i]
    
    # def combine_key_with_remaining_alphabet(self):
    #     remaining_character = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    #     for i in range (25):
    #         if(remaining_character[i] in self.key):
    #             pass
    #         else:
    #             self.key += remaining_character[i]

    def clear_all(self):
        self.input = ""
        self.key = ""
        self.output = ""

    def turn_key_into_matrix(self,key):
        uppercase_key = key.upper()
        # print(uppercase_key)
        self.key = uppercase_key.replace("J", "")
        # print(self.key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # note no J

        # dedup the list of characters
        slots = []
        for x in chain(self.key, alphabet):
            if not x in slots: slots.append(x)

        # get our matrix using list slices
        self.keytable = [ slots[i:i+5] for i in range(0, 25, 5) ]
        # print(self.keytable)

    def create_bigram(self,input):

        #filter input only alphabet
        uppercase_input = input.upper()
        for i in uppercase_input:
            if(ord(i)>=65 and ord(i)<=90):
                self.input = self.input + i
        
        input_length = len(self.input)
        bigram_input = ""

        counter = 0
        while(counter < input_length):
            if(counter == input_length-1):
                bigram_input += self.input[counter]
                bigram_input += "X"
                break

            if(self.input[counter]!=self.input[counter+1]):
                bigram_input += self.input[counter]
                bigram_input += self.input[counter+1]
                counter = counter+2
            else:
                bigram_input += self.input[counter]
                bigram_input += "X"
                counter = counter+1

        self.input = bigram_input

        # print(self.input)

    def change_bigram(self):

        hashmap = {}

        for i in range (5):
            for j in range(5):
                hashmap[self.keytable[i][j]] = {'row':i,'column':j}

        for i in range(0,len(self.input),2):
            first_bigram_col = hashmap[self.input[i]]['column']
            first_bigram_row = hashmap[self.input[i]]['row']
            second_bigram_col = hashmap[self.input[i+1]]['column']
            second_bigram_row = hashmap[self.input[i+1]]['row']

            if(first_bigram_col == second_bigram_col):
                first_character = self.keytable[(first_bigram_row+1)%5][(first_bigram_col)]
                second_character = self.keytable[(second_bigram_row+1)%5][(second_bigram_col)]

            elif(first_bigram_row == second_bigram_row):
                first_character = self.keytable[first_bigram_row][(first_bigram_col+1)%5]
                second_character = self.keytable[second_bigram_row][(second_bigram_col+1)%5]

            else:
                first_character = self.keytable[first_bigram_row][second_bigram_col]
                second_character = self.keytable[second_bigram_row][first_bigram_col]

            self.output += first_character
            self.output += second_character

    def change_bigram_reversed(self):

        hashmap = {}

        for i in range (5):
            for j in range(5):
                hashmap[self.keytable[i][j]] = {'row':i,'column':j}

        for i in range(0,len(self.input),2):
            first_bigram_col = hashmap[self.input[i]]['column']
            first_bigram_row = hashmap[self.input[i]]['row']
            second_bigram_col = hashmap[self.input[i+1]]['column']
            second_bigram_row = hashmap[self.input[i+1]]['row']

            if(first_bigram_col == second_bigram_col):
                first_character = self.keytable[(first_bigram_row-1)%5][(first_bigram_col)]
                second_character = self.keytable[(second_bigram_row-1)%5][(second_bigram_col)]

            elif(first_bigram_row == second_bigram_row):
                first_character = self.keytable[first_bigram_row][(first_bigram_col-1)%5]
                second_character = self.keytable[second_bigram_row][(second_bigram_col-1)%5]

            else:
                first_character = self.keytable[first_bigram_row][second_bigram_col]
                second_character = self.keytable[second_bigram_row][first_bigram_col]

            self.output += first_character
            self.output += second_character



    def display_output(self):
        print(self.output)
    # def temp_func(self,input,key):
    #     # self.get_distinct_character(key)
    #     # self.combine_key_with_remaining_alphabet()
    #     self.turn_key_into_matrix(key)
    #     print(self.keytable)

    def encrypt(self,input,key):
        self.clear_all()
        self.create_bigram(input)
        self.turn_key_into_matrix(key)
        self.change_bigram()
        self.display_output()

    def decrypt(self,input,key):
        self.clear_all()
        self.create_bigram(input)
        self.turn_key_into_matrix(key)
        self.change_bigram_reversed()
        self.display_output()






