# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:43:41 2023

@author: ARV0002
"""

from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
import random as r
from tkinter import filedialog
import os
from PIL import Image, ImageTk


root = Tk()
root.title('A paragraph about you!')
root.geometry('600x600')

image = ImageTk.PhotoImage(Image.open("python.png"))

list1 = ['blue', 'green', 'red', 'yellow', 'black', 'brown', 'pink', 'purple']
list2 = ['music', 'sport', 'puzzles', 'coding', 'nothing']

v11 = StringVar()
v22 = StringVar()

l1 = Label(root, text="What is your name?")
l1.place(relx=0.3, rely=0.1, anchor=CENTER)
t1 = Entry(root)
t1.place(relx=0.7, rely=0.1, anchor=CENTER)

l2 = Label(root, text="What is your age?")
l2.place(relx=0.3, rely=0.2, anchor=CENTER)
t2 = Entry(root)
t2.place(relx=0.7, rely=0.2, anchor=CENTER)

l3 = Label(root, text="What is your favourite food?")
l3.place(relx=0.3, rely=0.3, anchor=CENTER)
t3 = Entry(root)
t3.place(relx=0.7, rely=0.3, anchor=CENTER)

l4 = Label(root, text='What is your favourite colour?')
l4.place(relx=0.3, rely=0.4, anchor=CENTER)
t4 = ttk.Combobox(root, values=list1, textvariable=v11)
t4.place(relx=0.7, rely=0.4, anchor=CENTER)

l5 = Label(root, text="What do you like to do?")
l5.place(relx=0.3, rely=0.5, anchor=CENTER)
t5 = ttk.Combobox(root, values=list2, textvariable=v22)
t5.place(relx=0.7, rely=0.5, anchor=CENTER)

l6 = Label(root)
l6.place(relx=0.5, rely=0.7, anchor=CENTER)
l7 = Label(root)
l7.place(relx=0.5, rely=0.8, anchor=CENTER)
l8 = Label(root)
l8.place(relx=0.5, rely=0.9, anchor=CENTER)

l9 = Label(root, image=image)
l9.place(relx=0.9, rely=0.3, anchor=CENTER)
l10 = Label(root, image=image)
l10.place(relx=0.1, rely=0.3, anchor=CENTER)

def gen():
    v1 = t1.get()
    v2 = t2.get()
    v3 = t3.get()
    v4 = v11.get()
    v5 = v22.get()
    if v1 == "" :
        messagebox.showerror("Error", "It looks like you left out a space!")
    elif v2 == "" :
        messagebox.showerror("Error", "It looks like you left out a space!")
    elif v3 == "" :
        messagebox.showerror("Error", "It looks like you left out a space!")
    elif v4 == "" :
        messagebox.showerror("Error", "It looks like you left out a space!")
    elif v5 == "" :
        messagebox.showerror("Error", "It looks like you left out a space!")
    else:
        messagebox.showinfo("Gen info", "Successfully generated paragraph!")    
    
    l6['text'] = "Hey there! I'm "+v1+", "+v2+" years old, and I like eating "+v3+". Seriously, it's my absolute favorite!"
    l7['text'] = "In my free time, I like doing "+v5+", but I also try out new hobbies, hang out with friends, or just chill."
    l8['text'] = "When it comes to colors, I usually prefer "+v4+" – it just looks great on everything. Life's pretty cool, and I like to keep it simple and fun!"

b1 = Button(root, text='Generate!', command=gen)
b1.place(relx=0.5, rely=0.6, anchor=CENTER)

'''
Hey there! I'm [Name], [Age] years old, and I like eating [Favorite Food].
Seriously, it's my absolute favorite!
When it comes to colors, I usually prefer [Favorite Color] – it just looks great on everything. 
In my free time, I like doing [What I Like to Do], whether it's trying out new hobbies, hanging out with friends, or just chilling.
Life's pretty cool, and I like to keep it simple and fun!
'''


root.mainloop()