from tkinter import *
from tkinter import messagebox as tkMessageBox
import os
window = Tk()
window.title('GUI')

window.configure(background="#ffb3ff")
label = Label(window,text="WELCOME TO GENDER RECOGNITION",fg = "blue",
              bg = "red",font = "Verdana 30 bold")
label.pack()

def record():
    os.system('voice.py')
    tkMessageBox.showinfo( "welcome to gender recognition", "Recording your voice successfully")

def ckgender():
      os.system('test.bat')
   
B = Button(window, text ="Record your voice", command = record)
B1 = Button(window, text ="Test Your Gender", command = ckgender)



B.pack()
B1.pack()
window.mainloop()








