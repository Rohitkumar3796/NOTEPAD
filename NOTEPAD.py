# import tkinter as tk
from tkinter.filedialog import *

from tkinter import *
root=Tk()
root.geometry('400x600')
root['bg']='lightyellow'
root.title('NotePad')
# ********************************************
def SaveFile():
    new_file=asksaveasfile(mode='w',filetype=[('text files','.txt')])

    if new_file == "":
        return
    text=str(text1.get(1.0,END)) #whatever we write in entry, it takes the text from 0 to end
    new_file.write(text) #here we use write function and pass text file whatever we written in text file it will go to write
    new_file.close()

def OpenFile():
    #askopenfile() to use this function for if we want to open text file in the text so we can
    file=askopenfile(mode='r',filetype=[('text files','*.txt')])
    if file is not None:
        content=file.read() #here we use if because of if file is not empty so we can read the file
    text1.insert(INSERT,content) #if file is empty so whatever we write in the text so it will go to that file

def ClearFile():
    text1.delete(1.0,END)


# **********************************************
# HERE WE USE TKINTER WIDGET FOR USER INTERFACE
frame=Frame(root)
frame.pack(padx=5,pady=5,anchor=NW)

btn1=Button(root,text="Open",bg="white", command=OpenFile)
btn1.pack(in_=frame,side = LEFT) #anchor=NW mean your button will go to on top-left

btn2=Button(root,text="Save",bg="white", command=SaveFile)
btn2.pack(in_=frame,side = LEFT,)

btn3=Button(root,text="Clear",bg="white", command=ClearFile)
btn3.pack(in_=frame,side = LEFT,)

btn4=Button(root,text="Exit",bg="white", command=exit)
btn4.pack(in_=frame,ipadx=3,side = LEFT,)
# wrap=WORD (if your word is big then from wrap it will not go to second line( half on the first line and rest of the char in the second line))
text1=Text(root,wrap=WORD,bg='lightgrey',font=('poppins',15))
text1.pack(side=LEFT,expand=True,fill=BOTH)



root.mainloop()
