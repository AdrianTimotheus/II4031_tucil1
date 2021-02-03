from tkinter import *

root = Tk()

i = IntVar() #Basically Links Any Radiobutton With The Variable=i.
r1 = Radiobutton(root, text="option 1", value=1, variable=i)
r2 = Radiobutton(root, text="option 2", value=2, variable=i)
#
"""
If both values where equal, when one of the buttons
are pressed all buttons would be pressed.
If a button is pressed its value is true, or 1.
If you want to acess the data from the
radiobuttons, use a if statment like
"""
if (i.get() ==1):
       print("you picked option1")
else:
        print("you picked option2")
        
# :)

r1.pack()
r2.pack()

root.mainloop()