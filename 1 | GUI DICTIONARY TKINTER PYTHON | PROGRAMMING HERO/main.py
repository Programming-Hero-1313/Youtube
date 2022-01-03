from tkinter import *
import PyDictionary # pip install pyDictionary

root = Tk()

root.geometry('325x150')
root.title("DICTIONARY")
root.config(background="black")

def find_meaning():
    word = e.get()
    meaning = PyDictionary.PyDictionary.meaning(word)
    print(meaning)

e = Entry(root, font=('ariel',30, 'bold'), bg="green", fg="black")
e.place(x=10, y=10)
btn = Button(root, text="FIND MEANING",  font=('ariel',30, 'bold'), bg="green", fg="black", command=find_meaning)
btn.place(x=85, y=75)

root.mainloop()
