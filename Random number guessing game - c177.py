# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 20:04:35 2024

@author: ARV0002
"""

from tkinter import *
import random as r

root = Tk()
root.title('Random number guessing game')
root.geometry('500x500')

v1 = r.randint(1, 50)

l1 = Label(root, text='Guess the number!', font=(30))
l1.place(relx=0.5, rely=0.1, anchor=CENTER)

e1 = Entry(root)
e1.place(relx=0.5, rely=0.2, anchor=CENTER)

l2 = Label(root, text='')
l2.place(relx=0.5, rely=0.5, anchor=CENTER)

def random():
    if int(v1) == int(e1.get()):
        l2['text'] = 'Correct! You have found the number!'
    elif int(v1) > int(e1.get()):
        l2['text'] = 'Your answer is too small! Try again.'
    elif int(v1) < int(e1.get()):
        l2['text'] = 'Your answer is too big! Try again.'
        
b1 = Button(root, text='Check number', command=random)
b1.place(relx=0.5, rely=0.35, anchor=CENTER)
    
root.mainloop()