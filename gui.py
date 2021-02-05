from tkinter import *
from tkinter import filedialog

from vigenere import Vigenere
from autokey_vigenere import AutoKeyVigenere
from full_vigenere import Full_Vigenere
from playfair import Playfair
from extended_vigenere import ExtendedVigenere

vigenere = Vigenere()
autokey = AutoKeyVigenere()
full = Full_Vigenere()
full.generate_table()
playfair = Playfair()
extended = ExtendedVigenere()

root = Tk()
root.title=('Tucil 1')
root.geometry("1200x350")

def add_space(self, input, length):
        return ' '.join(input[i:i+length] for i in range(0,len(input),length))

def openFile():
    chooseFile = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"),))
    textFile = open(chooseFile,"r") # must be in same directory
    file_content = textFile.read()
    inputTextbox.insert(END,file_content)
    textFile.close()

def openBinaryFile():
    chooseFile = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.bin"),))
    textFile = open(chooseFile,"rb") # must be in same directory
    file_content = textFile.read()
    inputTextbox.insert(END,file_content)
    textFile.close()

def saveFile():
    createNewFile = filedialog.asksaveasfilename(title="Save File")
    saveFile = open(createNewFile,"w")
    file_content = outputTextbox.get(1.0,END)
    saveFile.write(file_content)

def encrypt():
    # print(choice.get())
    outputTextbox.delete(1.0,END)

    if(choice.get() == "vigenere"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        vigenere.encrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        if(display_choice.get() == "fiveSpace"):
            vigenere.output = vigenere.add_space(vigenere.output,5)
        outputTextbox.insert(END,vigenere.output)
        # print("Hello")

    elif(choice.get() == "full"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        full.encrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        if(display_choice.get() == "fiveSpace"):
            full.output = full.add_space(full.output,5)
        outputTextbox.insert(END,full.output)
        # print("Hello")

    elif(choice.get() == "autokey"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        autokey.encrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        if(display_choice.get() == "fiveSpace"):
            autokey.output = autokey.add_space(autokey.output,5)
        outputTextbox.insert(END,autokey.output)
        # print("Hello")

    elif(choice.get() == "extended"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        extended.encrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        if(display_choice.get() == "fiveSpace"):
            extended.output = extended.add_space(extended.output,5)
        outputTextbox.insert(END,extended.output)
        # print("Hello")

    elif(choice.get() == "playfair"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        playfair.encrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        if(display_choice.get() == "fiveSpace"):
            playfair.output = playfair.add_space(playfair.output,5)
        outputTextbox.insert(END,playfair.output)
        # print("Hello")

    else:
        print("error")

def decrypt():
    outputTextbox.delete(1.0,END)

    if(choice.get() == "vigenere"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        vigenere.decrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        if(display_choice.get() == "fiveSpace"):
            vigenere.output = vigenere.add_space(vigenere.output,5)
        outputTextbox.insert(END,vigenere.output)
        # print("Hello")

    elif(choice.get() == "full"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        full.decrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        if(display_choice.get() == "fiveSpace"):
            full.output = full.add_space(full.output,5)
        outputTextbox.insert(END,full.output)
        # print("Hello")

    elif(choice.get() == "autokey"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        autokey.decrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        if(display_choice.get() == "fiveSpace"):
            autokey.output = autokey.add_space(autokey.output,5)
        outputTextbox.insert(END,autokey.output)
        # print("Hello")

    elif(choice.get() == "extended"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        extended.decrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        if(display_choice.get() == "fiveSpace"):
            extended.output = extended.add_space(extended.output,5)
        outputTextbox.insert(END,extended.output)
        # print("Hello")

    elif(choice.get() == "playfair"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        playfair.decrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        if(display_choice.get() == "fiveSpace"):
            playfair.output = playfair.add_space(playfair.output,5)
        outputTextbox.insert(END,playfair.output)
        # print("Hello")

    else:
        print("error")

LabelFrame = Frame(root)
inputLabel = Label(LabelFrame,text="Input:")
inputLabel.pack(side="left")
keyLabel = Label(LabelFrame,text="Key:")
keyLabel.pack(side="left",padx=335)
outputLabel = Label(LabelFrame,text="Output:")
outputLabel.pack(side="left")

LabelFrame.pack(side="top")

textboxFrame = Frame(root)

inputTextbox = Text(textboxFrame, width=30, height=10, font=("Helvetica",16))
inputTextbox.pack(side="left")
keyTextbox = Text(textboxFrame, width=30, height=10, font=("Helvetica",16))
keyTextbox.pack(side="left")
outputTextbox = Text(textboxFrame, width=30, height=10, font=("Helvetica",16))
outputTextbox.pack(side="left")

textboxFrame.pack(side="top")

buttonFrame = Frame(root)

open_button = Button(buttonFrame, text="Open File", command=openFile)
open_button.pack(side="left")

open_binary_button = Button(buttonFrame, text="Open Binary", command=openBinaryFile)
open_binary_button.pack(side="left")

save_button = Button(buttonFrame, text="Save File", command=saveFile)
save_button.pack(side="left")

encrypt_button = Button(buttonFrame, text="Encrypt!", command=encrypt)
encrypt_button.pack(side="left")

decrypt_button = Button(buttonFrame, text="Decrypt!", command=decrypt)
decrypt_button.pack(side="left")


choice = StringVar()
choice.set("vigenere")

radioFrame = Frame(root)

Radiobutton(radioFrame,text="Vigenere",variable=choice,value="vigenere").pack(side="left")
Radiobutton(radioFrame,text="Full",variable=choice,value="full").pack(side="left")
Radiobutton(radioFrame,text="Autokey",variable=choice,value="autokey").pack(side="left")
Radiobutton(radioFrame,text="Extended",variable=choice,value="extended").pack(side="left")
Radiobutton(radioFrame,text="Playfair",variable=choice,value="playfair").pack(side="left")

radioFrame.pack(side="top")

display_choice = StringVar()
display_choice.set("noSpace")

displayChoiceFrame = Frame(root)

Radiobutton(displayChoiceFrame,text="No spacing",variable=display_choice,value="noSpace").pack(side="left")
Radiobutton(displayChoiceFrame,text="5 spacing",variable=display_choice,value="fiveSpace").pack(side="left")

displayChoiceFrame.pack(side="top")

buttonFrame.pack(side="top")

root.mainloop()