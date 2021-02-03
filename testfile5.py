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

def openFile():
    chooseFile = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"),))
    textFile = open(chooseFile,"r") # must be in same directory
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

    if(choice.get() == "vigenere"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        vigenere.encrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        outputTextbox.insert(END,vigenere.getContent())
        # print("Hello")

    elif(choice.get() == "full"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        full.encrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        outputTextbox.insert(END,full.getContent())
        # print("Hello")

    elif(choice.get() == "autokey"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        autokey.encrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        outputTextbox.insert(END,autokey.getContent())
        # print("Hello")

    elif(choice.get() == "extended"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        extended.encrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        outputTextbox.insert(END,extended.getContent())
        # print("Hello")

    elif(choice.get() == "playfair"):
        input = inputTextbox.get(1.0,END)
        key = keyTextbox.get(1.0,END)
        playfair.encrypt(input,key)
        # print(vigenere.getContent())
        # print(vigenere.input)
        # print(vigenere.key)
        outputTextbox.insert(END,playfair.getContent())
        # print("Hello")

    else:
        print("error")

def decrypt():
    pass

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
buttonFrame.pack(side="top")

root.mainloop()