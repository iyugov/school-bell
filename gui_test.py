'''Test environment for GUI.'''

from tkinter import *

root = Tk()
ent = Entry(root, width=20)
but = Button(root, text="Преобразовать")
lab = Label(root, width=20, bg='black', fg='white')
ent.pack()
but.pack()
lab.pack()
root.mainloop()
