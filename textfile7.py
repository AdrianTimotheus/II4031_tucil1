from tkinter import *

root = Tk()

choice = StringVar()

Radiobutton(root,text="Vigenere",variable=choice,value="vigenere").pack(side="left")
Radiobutton(root,text="Full",variable=choice,value="full").pack(side="left")
Radiobutton(root,text="Autokey",variable=choice,value="autokey").pack(side="left")
Radiobutton(root,text="Extended",variable=choice,value="vigenere").pack(side="left")
Radiobutton(root,text="Playfair",variable=choice,value="full").pack(side="left")

root.mainloop()