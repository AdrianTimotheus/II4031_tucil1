import tkinter as tk
from tkinter import ttk

#create main window
mainwindow = tk.Tk()
mainwindow.title("Tucil 1")

#create tab window
tabwindow = ttk.Notebook(mainwindow)

#create the tabs
tabVigenere = ttk.Frame(tabwindow)
tabFullVigenere = ttk.Frame(tabwindow)
tabAutoKeyVigenere = ttk.Frame(tabwindow)
tabExtendedVigenere = ttk.Frame(tabwindow)
tabPlayfair = ttk.Frame(tabwindow)
tabAffine = ttk.Frame(tabwindow)

#add the tabs to tabwindow
tabwindow.add(tabVigenere,text="Vigenere")
tabwindow.add(tabFullVigenere,text="Full Vigenere")
tabwindow.add(tabAutoKeyVigenere,text="Auto Key Vigenere")
tabwindow.add(tabExtendedVigenere,text="Extended Vigenere")
tabwindow.add(tabPlayfair,text="Playfair")
tabwindow.add(tabAffine,text="Affine")

#expand and fill area of main window
tabwindow.pack(expand=1, fill="both")

#add something to each tab
labelVigenere = ttk.Label(tabVigenere,text="Vigenere Cipher").grid(column=0,row=0,padx=20,pady=20)
labelFull = ttk.Label(tabFullVigenere,text="Full Vigenere Cipher").grid(column=0,row=0,padx=20,pady=20)
labelAutoKey = ttk.Label(tabAutoKeyVigenere,text="Auto Key Vigenere Cipher").grid(column=0,row=0,padx=20,pady=20)
labelExtended = ttk.Label(tabExtendedVigenere,text="Extended Vigenere Cipher").grid(column=0,row=0,padx=20,pady=20)
labelPlayfair = ttk.Label(tabPlayfair,text="Playfair Cipher").grid(column=0,row=0,padx=20,pady=20)
labelAffine = ttk.Label(tabAffine,text="Affine Cipher").grid(column=0,row=0,padx=20,pady=20)

Radiobutton(root,text="Vigenere",variable=choice,value="vigenere").pack(side="left")
Radiobutton(root,text="Full",variable=choice,value="full").pack(side="left")
Radiobutton(root,text="Autokey",variable=choice,value="autokey").pack(side="left")
Radiobutton(root,text="Extended",variable=choice,value="vigenere").pack(side="left")
Radiobutton(root,text="Playfair",variable=choice,value="full").pack(side="left")

mainwindow.mainloop()

